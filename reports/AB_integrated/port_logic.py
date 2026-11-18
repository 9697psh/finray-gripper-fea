"""Port the robot A detail design (탐색 · 재탐색 logic, Nav2 10 nodes, robot nodes) into PC1 of the team's integrated A·B diagram."""
import re, sys
from xml.etree import ElementTree as ET
SRC, DETAIL, OUT = sys.argv[1:4]
tree = ET.parse(SRC); root = tree.getroot(); MR = root.find('.//root')
cells = {c.get('id'): c for c in MR.iter('mxCell')}
D = ET.parse(DETAIL).getroot()
dcells = list(D.find('.//root').iter('mxCell'))

K = 2.2; OX, OY = 250, 3950          # pc1logic absolute origin
RX = lambda x: 20 + (x - 400) * K       # relative inside pc1logic
RY = lambda y: 70 + (y - 800) * K
AX = lambda x: OX + RX(x); AY = lambda y: OY + RY(y)

def remove(cid):
    c = cells.pop(cid, None)
    if c is not None: MR.remove(c)

# ---- 1. clear old PC1 logic (nodes, their internal edges, label cells, stray edges) ----
old = {c.get('id') for c in MR.iter('mxCell') if c.get('parent') == 'pc1logic'}
for c in list(MR.iter('mxCell')):
    if c.get('edge') and c.get('source') in old and (c.get('target') in old or c.get('target') is None):
        old.add(c.get('id'))
for e in ['e34', 'e35', 'e36', 'ClWFZT3JxWuRxpCHwhiY-13']: old.add(e)
for c in list(MR.iter('mxCell')):
    if c.get('parent') in old: old.add(c.get('id'))
keep_ext = {'e71', 'e255', 'e73', 'e203', 'e78', 'e79', 'e50', 'e51', 'e76'}
for cid in list(old):
    if cid not in keep_ext: remove(cid)
cells['pc1logic'].find('mxGeometry').set('height', '2400')

# ---- 2. copy the detail logic, scaled ----
def scale_style(st, edge=False):
    st = re.sub(r'fontSize=([\d.]+)', lambda m: f'fontSize={round(float(m.group(1)) * K, 1)}', st or '')
    st = re.sub(r'strokeWidth=([\d.]+)', lambda m: f'strokeWidth={round(float(m.group(1)) * 1.5, 1)}', st)
    if edge: st = st.replace('jumpSize=8', 'jumpSize=16')
    return st
def scale_html(v):
    return re.sub(r'font-size:\s*([\d.]+)px', lambda m: f'font-size:{round(float(m.group(1)) * K, 1)}px', v or '')
inside = lambda g: g is not None and 395 <= float(g.get('x', -1)) <= 1640 and 795 <= float(g.get('y', -1)) <= 1830
logic_ids, NEW = set(), {}
for c in dcells:
    g = c.find('mxGeometry')
    if c.get('vertex') and inside(g) and float(g.get('width')) < 1200:
        logic_ids.add(c.get('id'))
for c in dcells:
    g = c.find('mxGeometry'); cid = c.get('id'); nid = 'a1_' + cid
    if cid in logic_ids:
        n = ET.SubElement(MR, 'mxCell', {'id': nid, 'value': scale_html(c.get('value')), 'style': scale_style(c.get('style')), 'vertex': '1', 'parent': 'pc1logic'})
        x, y = float(g.get('x')), float(g.get('y'))
        ET.SubElement(n, 'mxGeometry', {'x': str(round(RX(x), 1)), 'y': str(round(RY(y), 1)), 'width': str(round(float(g.get('width')) * K, 1)),
                                         'height': str(round(float(g.get('height')) * K, 1)), 'as': 'geometry'})
        cells[nid] = n; NEW[cid] = n
    elif c.get('edge'):
        s, t = c.get('source'), c.get('target')
        sp = g.find("mxPoint[@as='sourcePoint']") if g is not None else None
        free = s is None and t is None and sp is not None and 395 <= float(sp.get('x')) <= 1640 and 795 <= float(sp.get('y')) <= 1830
        if not ((s in logic_ids and t in logic_ids) or free): continue
        attrs = {'id': nid, 'value': scale_html(c.get('value')), 'style': scale_style(c.get('style'), True), 'edge': '1', 'parent': '1'}
        if s: attrs['source'] = 'a1_' + s
        if t: attrs['target'] = 'a1_' + t
        n = ET.SubElement(MR, 'mxCell', attrs)
        ng = ET.SubElement(n, 'mxGeometry', {k: v for k, v in g.attrib.items()})
        for p in g:
            if p.tag == 'Array':
                arr = ET.SubElement(ng, 'Array', {'as': 'points'})
                for q in p: ET.SubElement(arr, 'mxPoint', {'x': str(round(AX(float(q.get('x'))), 1)), 'y': str(round(AY(float(q.get('y'))), 1))})
            elif p.get('as') == 'offset':
                ET.SubElement(ng, 'mxPoint', {'x': str(round(float(p.get('x', 0)) * K, 1)), 'y': str(round(float(p.get('y', 0)) * K, 1)), 'as': 'offset'})
            elif p.get('as') in ('sourcePoint', 'targetPoint'):
                ET.SubElement(ng, 'mxPoint', {'x': str(round(AX(float(p.get('x'))), 1)), 'y': str(round(AY(float(p.get('y'))), 1)), 'as': p.get('as')})
        cells[nid] = n

def find(text, ymax=None, ymin=None, exact=False):
    for cid, n in NEW.items():
        g = [c for c in dcells if c.get('id') == cid][0].find('mxGeometry'); y = float(g.get('y'))
        plain = re.sub(r'<[^>]+>', '', n.get('value') or '').strip()
        if (plain == text if exact else text in plain) and (ymax is None or y < ymax) and (ymin is None or y > ymin):
            return 'a1_' + cid, (AX(float(g.get('x'))), AY(y), float(g.get('width')) * K, float(g.get('height')) * K)
    raise SystemExit('not found: ' + text)
P0 = find('명령 확인'); P6 = find('정지 후 사진 캡처', ymax=1200); P7 = find('서버에 전송', ymax=1200)
R0 = find('받은 데이터'); R6 = find('서버에 전송', ymin=1200)
lab = find('① 탐색'); cells[lab[0]].find('mxGeometry').set('x', str(round(RX(560), 1)))   # keep the e255 riser clear of the title

# ---- 3. Nav2: add the two nodes the detail design shows (unused here) ----
DASH = 'whiteSpace=wrap;html=0;fontSize=24;spacing=12;fillColor=#FFFFFF;strokeColor=#9AA5AF;strokeWidth=2;dashed=1;rounded=1;fontColor=#6B7680;'
for cid, x, txt in [('pc1docksrv', 140, 'docking_server\nNav2 도킹 · 이번에는 미사용 (Create 3 /dock 사용)'),
                    ('pc1route', 1460, 'route_server\n경로 그래프 계획 · TurtleBot4 설정 없음 · 미사용')]:
    n = ET.SubElement(MR, 'mxCell', {'id': cid, 'value': txt, 'style': DASH, 'vertex': '1', 'parent': 'pc1nav'})
    ET.SubElement(n, 'mxGeometry', {'x': str(x), 'y': '1880', 'width': '700', 'height': '140', 'as': 'geometry'}); cells[cid] = n

# ---- 4. robot A: nodes that actually run on the TurtleBot4 ----
NODE = 'whiteSpace=wrap;html=0;fontSize=22;spacing=10;fillColor=#EDF4FA;strokeColor=#58748C;strokeWidth=2;rounded=1;'
GREY = 'whiteSpace=wrap;html=0;fontSize=20;spacing=10;fillColor=#F5F5F5;strokeColor=#A0A8B0;strokeWidth=1.5;rounded=1;fontColor=#666666;'
SUB = 'whiteSpace=wrap;html=0;fontSize=22;fontStyle=1;spacingLeft=16;spacingTop=6;align=left;verticalAlign=top;fillColor=#FFFFFF;strokeColor=#7D93A8;strokeWidth=2;dashed=1;rounded=1;arcSize=3;fontColor=#3E5468;'
NOTE = 'text;whiteSpace=wrap;html=0;fontSize=18;align=left;verticalAlign=middle;fontColor=#596B7B;'
LAYOUT = [('pi', 200, 7650, 1640, 520, SUB, 'Raspberry Pi 4 · turtlebot4_bringup (부팅 시 자동 실행)'),
 ('c3', 1880, 7650, 1200, 520, SUB, 'Create 3 베이스 · 자체 펌웨어'),
 ('lidar', 240, 7740, 460, 150, NODE, 'rplidar_composition\n라이다 드라이버 → /scan'),
 ('hmi', 740, 7740, 360, 150, GREY, 'turtlebot4_node\n버튼 · 화면 · LED'),
 ('oakd', 1260, 7740, 540, 150, NODE, 'oakd (depthai_ros_driver)\n카메라 영상을 계속 발행\n(사진 1장 추출은 PC 로직)'),
 ('rsp', 240, 7990, 860, 150, NODE, 'robot_state_publisher · joint_state_publisher\n→ /tf_static (라이다 · 카메라 위치)'),
 ('repub', 1180, 7990, 620, 150, NODE, 'create3_republisher\nCreate 3 토픽 · 액션을\n로봇 namespace로 중계'),
 ('dock', 1920, 7740, 340, 150, NODE, '도킹\n/dock · /undock 액션 서버\n/dock_status'),
 ('drive', 2300, 7740, 320, 150, NODE, '바퀴 구동 · 주행거리\n/cmd_vel 구독 →\n/odom · TF'),
 ('batt', 2660, 7740, 400, 150, NODE, '배터리 · 안전 센서\n/battery_state\n/hazard_detection'),
 ('c3note', 2140, 7990, 920, 150, NOTE, 'Create 3의 토픽 · 액션은 Pi의 create3_republisher를 거쳐\nPC에서 로봇 namespace로 보입니다.')]
GEO = {}
ra = cells['ra']; rg = ra.find('mxGeometry'); ox, oy = float(rg.get('x')), float(rg.get('y')); rg.set('height', '700')
for c in list(MR):
    if c.get('parent') == 'ra':
        for l in list(MR):
            if l.get('parent') == c.get('id'): MR.remove(l)
        MR.remove(c); cells.pop(c.get('id'), None)
for suf, x, y, w, h, st, txt in LAYOUT:
    cid = 'ra_' + suf; n = ET.SubElement(MR, 'mxCell', {'id': cid, 'value': txt, 'style': st, 'vertex': '1', 'parent': 'ra'})
    ET.SubElement(n, 'mxGeometry', {'x': str(x - ox), 'y': str(y - oy), 'width': str(w), 'height': str(h), 'as': 'geometry'}); cells[cid] = n; GEO[cid] = (x, y, w, h)

def absgeo(cid):
    if cid in GEO: return GEO[cid]
    x = y = 0; i = cid
    while i in cells and i not in ('0', '1'):
        g = cells[i].find('mxGeometry'); x += float(g.get('x', 0)); y += float(g.get('y', 0)); i = cells[i].get('parent')
    g = cells[cid].find('mxGeometry'); return x, y, float(g.get('width')), float(g.get('height'))
def frac(cid, px, py):
    x, y, w, h = absgeo(cid); return round((px - x) / w, 4), round((py - y) / h, 4)
BASE = 'edgeStyle=none;noEdgeStyle=1;rounded=0;endArrow=block;jumpStyle=arc;jumpSize=16;strokeColor=#596B7B;fontColor=#596B7B;fontSize=20;labelBackgroundColor=#FFFFFF;strokeWidth=2;'
def set_edge(eid, src, tgt, exitp, entryp, points, label, both=False, extra=''):
    c = cells.get(eid)
    if c is None:
        c = ET.SubElement(MR, 'mxCell', {'id': eid, 'edge': '1', 'parent': '1'}); cells[eid] = c
    for ch in list(c): c.remove(ch)
    ex, ey = frac(src, *exitp); nx, ny = frac(tgt, *entryp)
    c.set('style', BASE + extra + ('startArrow=block;startFill=1;' if both else '') + f'exitX={ex};exitY={ey};entryX={nx};entryY={ny};exitPerimeter=0;entryPerimeter=0;')
    c.set('source', src); c.set('target', tgt); c.set('parent', '1')
    lab = cells.get(eid + '_label')
    if lab is not None: lab.set('value', label); c.set('value', '')
    else: c.set('value', label)
    geo = ET.SubElement(c, 'mxGeometry', {'relative': '1', 'as': 'geometry', 'y': '-18'})
    arr = ET.SubElement(geo, 'Array', {'as': 'points'})
    for px, py in points: ET.SubElement(arr, 'mxPoint', {'x': str(round(px, 1)), 'y': str(round(py, 1))})

# robot ↔ Localization / Nav2 / logic
set_edge('e47', 'ra_lidar', 'pc1cost', (360, 7740), (680, 3400), [(360, 3440), (680, 3440)], '/robot_a/scan')
set_edge('e48', 'ra_lidar', 'pc1amcl', (340, 7740), (1780, 940), [(340, 1520), (1860, 1520), (1860, 980), (1780, 980)], '/robot_a/scan')
set_edge('e49', 'pc1collision', 'ra_drive', (2080, 3020), (2460, 7740), [(2080, 3060), (2460, 3060)], '/robot_a/cmd_vel')
set_edge('e50', 'ra_oakd', 'pc1logic', (1640, 7740), (1640, OY + 2400), [], '카메라 영상\n/robot_a/oakd/rgb/preview/image_raw')
set_edge('e51', 'pc1logic', 'ra_dock', (2090, OY + 2400), (2090, 7740), [], '/robot_a/undock · dock\n· dock_status', both=True)
set_edge('e_ra_batt', 'ra_batt', 'pc1logic', (2700, 7740), (2700, OY + 2400), [], '/robot_a/battery_state')
# logic ↔ bt_navigator: every '→ Nav2' step sends a NavigateToPose goal
set_edge('e76', 'pc1logic', 'pc1bt', (2480, OY), (2120, 1880), [(2480, 1940), (2120, 1940)], '→ Nav2 단계마다 NavigateToPose goal ↔ result\n(/robot_a/navigate_to_pose)', both=True,
         extra='strokeColor=#2E7D4F;fontColor=#2E7D4F;strokeWidth=3;')

# server ↔ logic steps
(p0, (x0, y0, w0, h0)), (p6, (x6, y6, w6, h6)), (p7, (x7, y7, w7, h7)) = P0, P6, P7
(r0, (xr, yr, wr, hr)), (r6, (x8, y8, w8, h8)) = R0, R6
set_edge('e71', 'srvStart' if 'srvStart' in cells else cells['e71'].get('source'), p0, (3780, 860), (x0, y0 + h0 / 2),
         [(3740, 860), (3740, 2060), (290, 2060), (290, y0 + h0 / 2)], '시작')
set_edge('e255', p0, cells['e255'].get('target'), (x0 + w0 * 0.92, y0), (7420, 940), [(x0 + w0 * 0.92, 3930), (7280, 3930), (7280, 940)], '로봇 A 토픽 (/robot_a/…)\nstatus · battery_state · current_zone · zone_result\ndetections · detection_image · amcl_pose')
set_edge('e73', p7, cells['e73'].get('target'), (1900, y7), (3780, 1360), [(1900, 4260), (3720, 4260), (3720, 1360)], '사진 · 위치 (352×352)')
set_edge('e203', cells['e203'].get('source'), p6, (5440, 980), (x6 + w6 / 2, y6), [(2520, 980), (2520, 4240), (x6 + w6 / 2, 4240)], '아니요: 재촬영 요청')
c2 = find('②', ymin=1290, exact=True)  # the ② circle that starts 재탐색
(c2i, (xc, yc, wc, hc)) = c2
set_edge('e78', cells['e78'].get('source'), c2i, (3780, 4320), (xc + wc / 2, yc),
         [(3600, 4320), (3600, 5110), (xc + wc / 2, 5110)], 'B 순찰 구역 · 재방문 목록 → ② 재탐색')
set_edge('e79', r6, cells['e79'].get('target'), (x8 + w8, y8 + h8 / 2), (3780, 4820), [(3700, y8 + h8 / 2), (3700, 4820)], '재확인 결과')
# robot B monitoring topics (team topic request) and robot A namespace in the robot box title
lb = cells.get('e256_label')
if lb is not None: lb.set('value', '로봇 B 토픽 (/robot_b/…)\nstatus · battery_state · current_zone\namcl_pose · harvest_status')
v = cells['ra'].get('value') or ''
if '/robot_a' not in v: cells['ra'].set('value', v.replace('로봇 A · TurtleBot4', '로봇 A · TurtleBot4 (/robot_a)', 1))
# robot topic labels: put them halfway between the logic box and the robot box (clear of the Create 3 header)
for lid, w in (('e50_label', 360), ('e51_label', 230)):
    lc = cells.get(lid)
    if lc is not None:
        g = lc.find('mxGeometry'); g.set('x', '0'); g.set('width', str(w)); g.set('height', '50')
        o = g.find('mxPoint')
        if o is not None: o.set('x', str(-w / 2)); o.set('y', '-25')
tree.write(OUT, encoding='utf-8', xml_declaration=True)
print('ok', len(NEW), 'logic vertices')
