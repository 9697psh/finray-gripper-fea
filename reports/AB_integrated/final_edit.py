"""Edit the team's final integrated diagram (PC1 robot A) to match a_remission_list.py / a_mission.py (11/22)."""
import sys
from xml.etree import ElementTree as ET
SRC, OUT = sys.argv[1:3]
tree = ET.parse(SRC); MR = tree.getroot().find('.//root'); C = {c.get('id'): c for c in MR.iter('mxCell')}
def ab(cid):
    x = y = 0.0; i = cid
    while i in C and i not in ('0', '1'):
        g = C[i].find('mxGeometry'); x += float(g.get('x', 0)); y += float(g.get('y', 0)); i = C[i].get('parent')
    g = C[cid].find('mxGeometry'); return x, y, float(g.get('width')), float(g.get('height'))
S = lambda col, txt: f'<br><span style="font-size:18.7px;color:{col}">{txt}</span>'
R, B, K = '#D62728', '#1F5FD6', '#666666'

# 1. a_remission_list box: topics only (no 성공 / 뺌 wording) + the B work-sector hand-off
rl = C['a1_rlist']
rl.set('value', '<b>a_remission_list.py</b>' + S(K, '처음부터 켜 둠 · 임시: 서버 대체')
       + S(R, '← /farm/robot_b/arrival (B 도착)') + S(R, '← /farm/robot_a/recheck_photo (재확인 사진)')
       + S(B, '→ 서비스 /robot5/remission_list')
       + S(R, '← /farm/robot_a/arrival_error (첫 순찰 섹터 저장)') + S(R, '← /farm/robot_a/force_next_sector (Bool)')
       + S(B, '→ /farm/robot_b/work_target (섹터 하나씩)'))
rl.find('mxGeometry').set('height', '250')

# 2. photo-send steps: cmd_audio beep right after sending (a_mission v13 · a_remission v9), arrival_error also feeds a_remission_list
def grow(cid, dh):
    g = C[cid].find('mxGeometry'); g.set('y', str(round(float(g.get('y')) - dh / 2, 1))); g.set('height', str(round(float(g.get('height')) + dh, 1)))
p7 = C['a1_c65']; v = p7.get('value')
v = v + S(K, '→ cmd_audio 알림음')
p7.set('value', v); grow('a1_c65', 30)
r6 = C['a1_c113']; r6.set('value', r6.get('value') + S(K, '→ cmd_audio 알림음')); grow('a1_c113', 30)
# 3. ② checks the battery before leaving for each point
r7 = C['a1_c116']; r7.set('value', r7.get('value').replace('배터리<br>20% 이하?', '출발 전 배터리<br>20% 이하?'))

# 4. new edges: System Monitor button → force_next_sector → a_remission_list → work_target → robot B
BASE = 'edgeStyle=none;noEdgeStyle=1;rounded=0;endArrow=block;jumpStyle=arc;jumpSize=16;fontSize=20;labelBackgroundColor=#FFFFFF;strokeWidth=2.5;'
def frac(cid, px, py):
    x, y, w, h = ab(cid); return round((px - x) / w, 4), round((py - y) / h, 4)
def edge(eid, src, tgt, exitp, entryp, pts, label, col, lx):
    ex, ey = frac(src, *exitp); nx, ny = frac(tgt, *entryp)
    e = C.get(eid)
    if e is None: e = ET.SubElement(MR, 'mxCell', {'id': eid}); C[eid] = e
    for ch in list(e): e.remove(ch)
    e.attrib.update({'edge': '1', 'parent': '1', 'source': src, 'target': tgt, 'value': label,
                     'style': BASE + f'strokeColor={col};fontColor={col};exitX={ex};exitY={ey};entryX={nx};entryY={ny};exitPerimeter=0;entryPerimeter=0;'})
    g = ET.SubElement(e, 'mxGeometry', {'relative': '1', 'as': 'geometry', 'x': str(lx)})
    arr = ET.SubElement(g, 'Array', {'as': 'points'})
    for px, py in pts: ET.SubElement(arr, 'mxPoint', {'x': str(px), 'y': str(py)})
rx, ry, rw, rh = ab('a1_rlist')
edge('e_force_next', 'api', 'a1_rlist', (7420, 5130), (rx + rw, 5690), [(3560, 5130), (3560, 5690)],
     'System Monitor 버튼\n/farm/robot_a/force_next_sector (Bool)', R, 0.226)
cx, cy, cw, ch = ab('pc2m_cmd')
edge('e_work_target', 'a1_rlist', 'pc2m_cmd', (1097, ry), (13840, cy + ch), [(1097, 5090), (3580, 5090), (3580, 4910), (13840, 4910)],
     '로봇 B 다음 작업 섹터 · /farm/robot_b/work_target (WorkTarget)', B, 0.482)
for e in ('e_force_next', 'e_work_target'): C[e].set('style', C[e].get('style').replace('html=1;', '') + 'html=0;')
tree.write(OUT, encoding='utf-8', xml_declaration=True)
print('ok')
