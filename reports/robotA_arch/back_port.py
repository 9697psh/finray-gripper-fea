"""Bring the PC1 robot-A logic of the team's final integrated diagram back into the robot A detail design (inverse of port_logic.py)."""
import re, sys
from xml.etree import ElementTree as ET
FINAL, BASE, OUT = sys.argv[1:4]
K = 2.2
F = ET.parse(FINAL).getroot(); FC = {c.get('id'): c for c in F.iter('mxCell')}
def absxy(cid):
    x = y = 0.0; i = cid
    while i in FC and i not in ('0', '1'):
        g = FC[i].find('mxGeometry'); x += float(g.get('x', 0)); y += float(g.get('y', 0)); i = FC[i].get('parent')
    return x, y
OX, OY = absxy('pc1logic')
IX = lambda rx: 400 + (rx - 20) / K          # pc1logic-relative → detail
IY = lambda ry: 800 + (ry - 70) / K
JX = lambda ax: IX(ax - OX); JY = lambda ay: IY(ay - OY)   # absolute → detail
def unscale_style(st, edge=False):
    st = re.sub(r'fontSize=([\d.]+)', lambda m: f'fontSize={round(float(m.group(1)) / K, 1)}', st or '')
    st = re.sub(r'strokeWidth=([\d.]+)', lambda m: f'strokeWidth={round(float(m.group(1)) / 1.5, 1)}', st)
    if edge: st = st.replace('jumpSize=16', 'jumpSize=8')
    return st
def unscale_html(v):
    return re.sub(r'font-size:\s*([\d.]+)px', lambda m: f'font-size:{round(float(m.group(1)) / K, 1)}px', v or '')

T = ET.parse(BASE); MR = T.getroot().find('.//root'); BC = list(MR.iter('mxCell'))
inside = lambda g: g is not None and g.get('x') is not None and 395 <= float(g.get('x')) <= 1660 and 795 <= float(g.get('y', -1)) <= 1830
logic = {c.get('id') for c in BC if c.get('vertex') and inside(c.find('mxGeometry')) and float(c.find('mxGeometry').get('width')) < 1200}
for c in BC:
    g = c.find('mxGeometry'); drop = c.get('id') in logic
    if c.get('edge'):
        s, t = c.get('source'), c.get('target'); sp = g.find("mxPoint[@as='sourcePoint']") if g is not None else None
        free = s is None and t is None and sp is not None and 395 <= float(sp.get('x')) <= 1660 and 795 <= float(sp.get('y')) <= 1830
        drop = (s in logic and t in logic) or free
    if drop: MR.remove(c)

kids = {i for i, c in FC.items() if c.get('parent') == 'pc1logic'}
nid = lambda i: 'L_' + i
n_v = n_e = 0
for i, c in FC.items():
    if i in kids and c.get('vertex'):
        g = c.find('mxGeometry')
        n = ET.SubElement(MR, 'mxCell', {'id': nid(i), 'value': unscale_html(c.get('value')), 'style': unscale_style(c.get('style')), 'vertex': '1', 'parent': '1'})
        ET.SubElement(n, 'mxGeometry', {'x': str(round(IX(float(g.get('x', 0))), 1)), 'y': str(round(IY(float(g.get('y', 0))), 1)),
                                         'width': str(round(float(g.get('width')) / K, 1)), 'height': str(round(float(g.get('height')) / K, 1)), 'as': 'geometry'}); n_v += 1
for i, c in FC.items():
    if not c.get('edge'): continue
    s, t = c.get('source'), c.get('target'); g = c.find('mxGeometry')
    sp = g.find("mxPoint[@as='sourcePoint']") if g is not None else None
    free = s is None and t is None and sp is not None and c.get('id', '').startswith('a1_')
    if not ((s in kids and t in kids) or free): continue
    a = {'id': nid(i), 'value': unscale_html(c.get('value')), 'style': unscale_style(c.get('style'), True), 'edge': '1', 'parent': '1'}
    if s: a['source'] = nid(s)
    if t: a['target'] = nid(t)
    n = ET.SubElement(MR, 'mxCell', a)
    ng = ET.SubElement(n, 'mxGeometry', {k: v for k, v in g.attrib.items()})
    for p in g:
        if p.tag == 'Array':
            arr = ET.SubElement(ng, 'Array', {'as': 'points'})
            for q in p: ET.SubElement(arr, 'mxPoint', {'x': str(round(JX(float(q.get('x'))), 1)), 'y': str(round(JY(float(q.get('y'))), 1))})
        elif p.get('as') == 'offset':
            ET.SubElement(ng, 'mxPoint', {'x': str(round(float(p.get('x', 0)) / K, 1)), 'y': str(round(float(p.get('y', 0)) / K, 1)), 'as': 'offset'})
        elif p.get('as') in ('sourcePoint', 'targetPoint'):
            ET.SubElement(ng, 'mxPoint', {'x': str(round(JX(float(p.get('x'))), 1)), 'y': str(round(JY(float(p.get('y'))), 1)), 'as': p.get('as')})
    n_e += 1
# label cells that hang off logic edges (parent = an edge we copied)
for i, c in FC.items():
    if c.get('vertex') and c.get('parent') in FC and FC[c.get('parent')].get('edge') and nid(c.get('parent')) in {x.get('id') for x in MR.iter('mxCell')} and c.get('parent') not in kids:
        n = ET.SubElement(MR, 'mxCell', {k: v for k, v in c.attrib.items()}); n.set('id', nid(i)); n.set('parent', nid(c.get('parent')))
        n.set('style', unscale_style(c.get('style'))); n.append(c.find('mxGeometry'))
# the integrated version slid the ① title right to clear an outside riser; in the detail design put it back at the left edge, above the 'no' bypass line
for c in MR.iter('mxCell'):
    if c.get('id') == 'L_a1_c57':
        g = c.find('mxGeometry'); g.set('x', '430'); g.set('y', '801')
# links that live outside the logic box in the detail design: System Monitor button → a_remission_list → robot B
ids = {c.get('id'): c for c in MR.iter('mxCell')}
mon = next(c.get('id') for c in MR.iter('mxCell') if 'System Monitor' in (c.get('value') or ''))
rl = ids['L_a1_rlist']; g = rl.find('mxGeometry'); rx_, ry_, rw_, rh_ = (float(g.get(k)) for k in ('x', 'y', 'width', 'height'))
def vtx(cid, x, y, w, h, val, st):
    n = ET.SubElement(MR, 'mxCell', {'id': cid, 'value': val, 'style': st, 'vertex': '1', 'parent': '1'})
    ET.SubElement(n, 'mxGeometry', {'x': str(x), 'y': str(y), 'width': str(w), 'height': str(h), 'as': 'geometry'})
def edg(cid, s_, t_, ex, ey, nx, ny, pts, val, col, both=False, lx=0, loff=(0, 0)):
    st = (f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor={col};strokeWidth=1.6;fontSize=9;fontColor={col};'
          f'labelBackgroundColor=#FFFFFF;jumpStyle=arc;jumpSize=8;exitX={ex};exitY={ey};entryX={nx};entryY={ny};exitPerimeter=0;entryPerimeter=0;')
    if both: st += 'startArrow=block;startFill=1;'
    n = ET.SubElement(MR, 'mxCell', {'id': cid, 'value': val, 'style': st, 'edge': '1', 'parent': '1', 'source': s_, 'target': t_})
    gg = ET.SubElement(n, 'mxGeometry', {'relative': '1', 'as': 'geometry', 'x': str(lx)})
    arr = ET.SubElement(gg, 'Array', {'as': 'points'})
    for px, py in pts: ET.SubElement(arr, 'mxPoint', {'x': str(px), 'y': str(py)})
    ET.SubElement(gg, 'mxPoint', {'x': str(loff[0]), 'y': str(loff[1]), 'as': 'offset'})
vtx('RB', 40, 1600, 220, 70, '<b>로봇 B (PC2)</b><br><span style="font-size:10px">robot_b_follow_move<br>← /farm/robot_b/work_target<br>→ /farm/robot_b/arrival</span>',
    'rounded=0;whiteSpace=wrap;html=1;fillColor=#F4F4F4;strokeColor=#333333;strokeWidth=2;fontSize=12;fontColor=#1A1A1A;')
mg = ids[mon].find('mxGeometry'); mx, my, mw, mh = (float(mg.get(k)) for k in ('x', 'y', 'width', 'height'))
y1, y2 = ry_ + rh_ * 0.71, ry_ + rh_ * 0.9
edg('E_force_next', mon, 'L_a1_rlist', 1, round((690 - my) / mh, 4), 0, round((y1 - ry_) / rh_, 4), [(335, 690), (335, y1)],
    'force_next_sector', '#D62728', lx=0.72, loff=(0, 8))
edg('E_b_link', 'L_a1_rlist', 'RB', 0, round((y2 - ry_) / rh_, 4), 1, round((1631 - 1600) / 70, 4), [(348, y2), (348, 1631)],
    'work_target → / ← arrival', '#1F5FD6', both=True, lx=-0.62, loff=(0, 9))
T.write(OUT, encoding='utf-8', xml_declaration=False)
print('removed', len(logic), 'logic vertices · added', n_v, 'vertices', n_e, 'edges · pc1logic origin', OX, OY)
