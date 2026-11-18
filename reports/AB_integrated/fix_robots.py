"""Replace the robot A/B boxes of the team's A·B integrated diagram with the nodes that actually run on a TurtleBot4."""
import sys, copy
from xml.etree import ElementTree as ET
SRC, OUT = sys.argv[1], sys.argv[2]
tree = ET.parse(SRC); root = tree.getroot()
model_root = root.find('.//root')
cells = {c.get('id'): c for c in model_root.iter('mxCell')}

NODE = 'whiteSpace=wrap;html=0;fontSize=22;spacing=10;fillColor=#EDF4FA;strokeColor=#58748C;strokeWidth=2;rounded=1;align=center;verticalAlign=middle;'
GREY = 'whiteSpace=wrap;html=0;fontSize=20;spacing=10;fillColor=#F5F5F5;strokeColor=#A0A8B0;strokeWidth=1.5;rounded=1;fontColor=#666666;'
SUB = 'whiteSpace=wrap;html=0;fontSize=22;fontStyle=1;spacingLeft=16;spacingTop=6;align=left;verticalAlign=top;fillColor=#FFFFFF;strokeColor=#7D93A8;strokeWidth=2;dashed=1;rounded=1;arcSize=3;fontColor=#3E5468;'
NOTE = 'text;whiteSpace=wrap;html=0;fontSize=18;align=left;verticalAlign=middle;fontColor=#596B7B;'

# absolute layout for robot A (robot B = same + DX)
DX = 11120
LAYOUT = [  # id-suffix, x, y, w, h, style, text
 ('pi', 200, 7650, 1640, 520, SUB, 'Raspberry Pi 4 · turtlebot4_bringup (부팅 시 자동 실행)'),
 ('c3', 1880, 7650, 1200, 520, SUB, 'Create 3 베이스 · 자체 펌웨어'),
 ('lidar', 240, 7740, 460, 150, NODE, 'rplidar_composition\n라이다 드라이버 → /scan'),
 ('hmi', 740, 7740, 360, 150, GREY, 'turtlebot4_node\n버튼 · 화면 · LED'),
 ('oakd', 1260, 7740, 540, 150, NODE, 'oakd (depthai_ros_driver)\n카메라 영상을 계속 발행\n(사진 1장 추출은 PC 로직)'),
 ('rsp', 240, 7990, 860, 150, NODE, 'robot_state_publisher · joint_state_publisher\n→ /tf_static (라이다 · 카메라 위치)'),
 ('repub', 1180, 7990, 620, 150, NODE, 'create3_republisher\nCreate 3 토픽 · 액션을\n로봇 namespace로 중계'),
 ('dock', 1920, 7740, 340, 150, NODE, '도킹\n/dock · /undock 액션 서버\n/dock_status'),
 ('drive', 2300, 7740, 320, 150, NODE, '바퀴 구동 · 주행거리\n/cmd_vel 구독 →\n/odom · TF'),
 ('batt', 2660, 7740, 400, 150, NODE, '배터리 · 안전 센서\n/battery_state\n/hazard_detection'),
 ('c3note', 2140, 7990, 920, 150, NOTE, 'Create 3의 토픽 · 액션은 Pi의 create3_republisher를 거쳐\nPC에서 로봇 namespace로 보입니다.'),
]
GEO = {}

def rebuild(robot, prefix, dx):
    box = cells[robot]; g = box.find('mxGeometry')
    ox, oy = float(g.get('x')), float(g.get('y'))
    g.set('height', '700')
    for c in list(model_root):
        if c.get('parent') == robot:
            model_root.remove(c); cells.pop(c.get('id'), None)
    for suf, x, y, w, h, st, txt in LAYOUT:
        cid = f'{prefix}_{suf}'
        c = ET.SubElement(model_root, 'mxCell', {'id': cid, 'value': txt, 'style': st, 'vertex': '1', 'parent': robot})
        ET.SubElement(c, 'mxGeometry', {'x': str(x + dx - ox), 'y': str(y - oy), 'width': str(w), 'height': str(h), 'as': 'geometry'})
        cells[cid] = c; GEO[cid] = (x + dx, y, w, h)

rebuild('ra', 'ra', 0); rebuild('rb', 'rb', DX)

def absgeo(cid):
    if cid in GEO: return GEO[cid]
    x = y = 0; i = cid
    while i in cells and i not in ('0', '1'):
        gg = cells[i].find('mxGeometry'); x += float(gg.get('x', 0)); y += float(gg.get('y', 0)); i = cells[i].get('parent')
    gg = cells[cid].find('mxGeometry')
    return x, y, float(gg.get('width')), float(gg.get('height'))

def frac(cid, px, py):
    x, y, w, h = absgeo(cid)
    return round((px - x) / w, 4), round((py - y) / h, 4)

BASE = 'edgeStyle=none;noEdgeStyle=1;rounded=0;endArrow=block;jumpStyle=arc;jumpSize=16;strokeColor=#596B7B;fontColor=#596B7B;fontSize=20;labelBackgroundColor=#FFFFFF;strokeWidth=2;'
def set_edge(eid, src, tgt, exitp, entryp, points, label, both=False, new=False):
    if new:
        c = ET.SubElement(model_root, 'mxCell', {'id': eid, 'edge': '1', 'parent': '1'}); cells[eid] = c
    else:
        c = cells[eid]
        for ch in list(c): c.remove(ch)
    ex, ey = frac(src, *exitp); nx, ny = frac(tgt, *entryp)
    st = BASE + (f'startArrow=block;startFill=1;' if both else '') + f'exitX={ex};exitY={ey};entryX={nx};entryY={ny};exitPerimeter=0;entryPerimeter=0;'
    lab = cells.get(eid + '_label')
    if lab is not None: lab.set('value', label); label = ''
    c.set('style', st); c.set('source', src); c.set('target', tgt); c.set('value', label)
    geo = ET.SubElement(c, 'mxGeometry', {'relative': '1', 'as': 'geometry', 'y': '-18'})
    arr = ET.SubElement(geo, 'Array', {'as': 'points'})
    for px, py in points: ET.SubElement(arr, 'mxPoint', {'x': str(px), 'y': str(py)})

def wire(p, dx, eids, logic):
    e_cost, e_amcl, e_cmd, e_cam, e_undock = eids
    L = lambda n: f'{logic}_{n}'
    # /scan → costmaps (left margin lane) and → amcl (outer left lane, corridor y 1520)
    set_edge(e_cost, f'{p}_lidar', f'{p[:0]}{"pc1" if dx == 0 else "pc2"}cost', (360 + dx, 7740), (680 + dx, 3400), [(360 + dx, 3440), (680 + dx, 3440)], '/scan')
    set_edge(e_amcl, f'{p}_lidar', f'{"pc1" if dx == 0 else "pc2"}amcl', (340 + dx, 7740), (1780 + dx, 940),
             [(340 + dx, 1520), (1860 + dx, 1520), (1860 + dx, 980), (1780 + dx, 980)], '/scan')
    # collision_monitor → wheels (/cmd_vel), same right-margin lane as before
    set_edge(e_cmd, f'{"pc1" if dx == 0 else "pc2"}collision', f'{p}_drive', (2080 + dx, 3020), (2460 + dx, 7740),
             [(2080 + dx, 3060), (2460 + dx, 3060)], '/cmd_vel')
    # camera stream → capture step
    cap = 'pc1m_capture' if dx == 0 else 'pc2m_capture'
    set_edge(e_cam, f'{p}_oakd', cap, (1640 + dx, 7740), (1720 + dx, 5200), [(1640 + dx, 5200)], '카메라 영상')
    # undock step ↔ dock action (goal → result)
    und = 'pc1m_undock' if dx == 0 else 'pc2m_undock'
    set_edge(e_undock, und, f'{p}_dock', (1100 + dx, 4760), (2090 + dx, 7890),
             [(1140 + dx, 4760), (1140 + dx, 8200), (2090 + dx, 8200)], '/undock 요청 · 결과', both=True)

wire('ra', 0, ('e47', 'e48', 'e49', 'e50', 'e51'), 'pc1m')
wire('rb', DX, ('e52', 'e53', 'e54', 'e55', 'e56'), 'pc2m')
# robot A only: battery decision ← /battery_state, and → /dock when returning
set_edge('e_ra_batt', 'ra_batt', 'pc1m_battery', (2700, 7740), (2420, 5700), [(2700, 5700)], '/battery_state', new=True)
set_edge('e_ra_dock', 'pc1m_battery', 'ra_dock', (2100, 5760), (2100, 7740), [], '/dock (복귀)', new=True)

tree.write(OUT, encoding='utf-8', xml_declaration=True)
print('ok', OUT)
