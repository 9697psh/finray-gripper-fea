#!/usr/bin/env python3
"""Robot A '우리의 로직' — the team's hand-drawn flowchart, redrawn as-is (same layout, same wording)."""
import sys
from xml.sax.saxutils import quoteattr

RED, BLUE, INK = '#D62728', '#1F5FD6', '#222222'
YEL, NAVBG = '#FFF176', '#F4A3A3'
cells, _id = [], [1]

def nid():
    _id[0] += 1
    return f'c{_id[0]}'

def S(**kw):
    return ';'.join(f'{k}={v}' for k, v in kw.items()) + ';'

def box(x, y, w, h, html, style):
    cid = nid()
    cells.append(f'<mxCell id="{cid}" value={quoteattr(html)} style="{style}" vertex="1" parent="1">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    return cid

def edge(src, tgt, label='', color=INK, points=(), ex=None, ey=None, nx=None, ny=None, lx=0, loff=(0, 0),
         width=1.8, font=12, lbg='#FFFFFF', fcol=None):
    st = dict(edgeStyle='orthogonalEdgeStyle', rounded=1, html=1, endArrow='block', endFill=1, strokeColor=color,
              strokeWidth=width, fontSize=font, fontColor=fcol or color, labelBackgroundColor=lbg, jumpStyle='arc')
    for k, v in (('exitX', ex), ('exitY', ey), ('entryX', nx), ('entryY', ny)):
        if v is not None:
            st[k] = v
    if ex is not None: st['exitPerimeter'] = 0
    if nx is not None: st['entryPerimeter'] = 0
    cid = nid()
    pts = ''.join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
    arr = f'<Array as="points">{pts}</Array>' if pts else ''
    cells.append(f'<mxCell id="{cid}" value={quoteattr(label)} style="{S(**st)}" edge="1" parent="1" source="{src}" target="{tgt}">'
                 f'<mxGeometry x="{lx}" relative="1" as="geometry">{arr}<mxPoint x="{loff[0]}" y="{loff[1]}" as="offset"/></mxGeometry></mxCell>')

STEP = S(rounded=1, whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor='#555555', strokeWidth=1.3, fontSize=15,
         fontColor=INK, arcSize=14)
def step(x, y, w, h, html): return box(x, y, w, h, html, STEP)
def dia(x, y, w, h, html, col=INK):
    return box(x, y, w, h, html, 'rhombus;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=col, strokeWidth=1.8,
                                                  fontSize=14, fontColor=col))
def oval(x, y, w, h, html, col=INK):
    return box(x, y, w, h, html, 'ellipse;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=col, strokeWidth=1.8,
                                                  fontSize=15, fontColor=col))
def text(x, y, w, h, html, size=15, col=INK, align='center'):
    return box(x, y, w, h, html, 'text;' + S(html=1, whiteSpace='wrap', align=align, verticalAlign='middle', fontSize=size,
                                               fontColor=col))
OR = '#D97A00'
ADD = S(rounded=1, whiteSpace='wrap', html=1, fillColor='#FFF6E8', strokeColor=OR, strokeWidth=1.6, dashed=1, fontSize=14, fontColor=INK, arcSize=14)
add_note = lambda s: f'<span style="color:{OR}">{s}</span>'
hl = lambda s: f'<span style="background-color:{YEL}">&nbsp;{s}&nbsp;</span>'
blue = lambda s, size=13: f'<span style="color:{BLUE};font-size:{size}px">{s}</span>'

# ---- main PC / server ----
box(35, 20, 195, 70, '<b>main PC</b>', S(rounded=0, whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=INK,
                                         strokeWidth=2, fontSize=22, fontColor=INK))
text(35, 98, 195, 26, 'server', size=19)
ST = oval(35, 140, 180, 70, '<b>작업 시작</b>', RED)
D0 = dia(400, 125, 250, 90, '<b>is docked?</b><br><span style="font-size:11px">(dock_status · is_docked)</span>', RED)
UD = box(625, 66, 150, 40, '<b>언도킹</b> (/undock)', ADD)
edge(ST, D0, color=RED, width=2)

# ---- 1단계: 순찰 ----
text(905, 26, 220, 26, 'Robot A', size=17)
P1 = step(905, 58, 220, 56, hl('<b>순찰 자율주행</b>') + '<br><span style="font-size:13px">좌표 1,2,3,4 (i = 1부터)</span>')
M1 = step(1320, 64, 200, 44, '좌표 i로 이동')
D1 = dia(1300, 170, 240, 120, 'i 이동 완료?')
T1 = step(955, 250, 160, 42, 'TB4 stop')
O1 = step(870, 405, 330, 104, hl('<b>oakd 캡처 실행</b>') + '<br>토마토 캡처 후 server에 전송<br>' + blue('publish'))
text(1215, 420, 330, 30, blue('a_mission / 좌표 / image topic', 15), align='left')
FD = dia(615, 245, 245, 115, 'i = final<br>sector?')

edge(D0, UD, 'yes', color=RED, ex=0.5, ey=0, nx=0, ny=0.5, points=((525, 86),), lx=-0.3, width=2)
edge(UD, P1, ex=1, ey=0.5, nx=0, ny=0.5, color=OR)
edge(D0, P1, 'no<br>' + add_note('바로 출발'), color=RED, ex=1, ey=0.5, nx=0, ny=0.85, points=((820, 170), (820, 106)), lx=-0.55, width=2, font=12)
edge(FD, P1, 'no &nbsp; · &nbsp; i = i+1', ex=0.5, ey=0, nx=0.5, ny=1, points=((737, 200), (1015, 200)), lx=0.1, loff=(0, -12))
edge(P1, M1, '<b>nav2</b>', lbg=NAVBG, fcol=INK, font=14)
edge(M1, D1, ex=0.5, ey=1, nx=0.5, ny=0)
edge(D1, M1, 'no<br>(재확인)<br>' + add_note('3회 실패 시 건너뛰고<br>서버에 기록'), ex=1, ey=0.5, nx=1, ny=0.5, points=((1590, 230), (1590, 86)), lx=-0.2, loff=(58, 0), font=11)
edge(D1, T1, 'yes', ex=0, ey=0.5, nx=1, ny=0.5, lx=-0.3)
edge(T1, O1, ex=0.5, ey=1, nx=round((1035 - 870) / 330, 4), ny=0)
edge(O1, FD, '', ex=0, ey=0.5, nx=0.5, ny=1, points=((737, 457),))

# ---- 2단계: 재방문 ----
text(800, 600, 200, 28, 'Robot A', size=17)
P2 = step(765, 632, 330, 78, hl('<b>재방문 순찰 자율주행</b>') + '<br>(b에게서 방문한 좌표 수신)')
M2 = step(1300, 630, 240, 62, blue('remission_list에', 13) + '<br>남은 좌표로 이동')
D2 = dia(1275, 770, 290, 125, 'list 좌표 이동 완료?')
T2 = step(840, 885, 160, 42, 'TB4 stop')
O2 = step(840, 990, 280, 100, 'oakd 캡처 실행<br>캡처 후 server에 전송<br>' + blue('publish'))
text(1140, 990, 360, 60, blue('a_remission / 좌표 / image topic', 15) + '<br>' + blue('└→ (재순찰 파일이라는 뜻)', 13), align='left')
D3 = dia(380, 980, 260, 110, 'list에 남은<br>좌표?')
VS = step(680, 755, 470, 70, 'visit subscriber ' + blue('(remission_list에 좌표 저장)', 12) + '<br>' + blue('DB에서 받아오기', 13))
EN = oval(115, 600, 200, 180, '현 작업 종료 및<br>도킹 스테이션<br>이동')
END = text(140, 530, 150, 34, '<b>작업종료</b>', size=17)

edge(FD, P2, 'yes', ex=0, ey=0.5, nx=0, ny=0.5, points=((600, 302), (600, 671)), lx=-0.1)
edge(P2, M2, '<b>nav2</b>', lbg=NAVBG, fcol=INK, font=14)
edge(M2, D2, ex=0.5, ey=1, nx=0.5, ny=0)
edge(D2, M2, 'no<br>(재확인)<br>' + add_note('3회 실패 시 건너뛰고<br>서버에 기록'), ex=1, ey=0.5, nx=1, ny=0.5, points=((1600, 832), (1600, 661)), lx=-0.2, loff=(58, 0), font=11)
edge(D2, T2, 'yes', ex=0, ey=0.5, nx=1, ny=0.5, lx=-0.3)
edge(T2, O2, ex=0.5, ey=1, nx=round((920 - 840) / 280, 4), ny=0)
edge(O2, D3, f'<span style="color:{BLUE}">server에서 b 방문 좌표</span><br><br><span style="color:{BLUE}">subscribe</span>',
     ex=0, ey=0.5, nx=1, ny=0.5, lbg='none', font=12)
edge(D3, VS, '방문한 좌표 remove<br>' + add_note('(서버 DB에도 방문 완료 표시)'), ex=0.5, ey=0, nx=0, ny=0.5, points=((510, 790),), lx=0.55, loff=(0, -22), font=11)
BW = box(130, 985, 210, 100, '<b>B 작업<br>끝났나?</b>', 'rhombus;' + S(whiteSpace='wrap', html=1, fillColor='#FFF6E8', strokeColor=OR, strokeWidth=1.8, dashed=1, fontSize=13, fontColor=INK))
WT = box(140, 1135, 190, 48, '잠시 대기 후 다시 확인<br>' + add_note('<span style="font-size:11px">(새 좌표가 오면 재방문)</span>'), ADD.replace('fontSize=14', 'fontSize=13'))
edge(D3, BW, 'no', ex=0, ey=0.5, nx=1, ny=0.5, lx=-0.2)
edge(BW, EN, 'yes', ex=0.5, ey=0, nx=0.5, ny=1, color=OR, lx=-0.3)
edge(BW, WT, 'no', ex=0.5, ey=1, nx=0.5, ny=0, color=OR)
edge(WT, D3, '', ex=1, ey=0.5, nx=0.5, ny=1, points=((510, 1159),), color=OR)
text(25, 1088, 110, 40, add_note('<span style="font-size:11px">서버의 B 상태로 판단</span>'), size=11)
edge(EN, END, ex=0.5, ey=0, nx=0.5, ny=1)
edge(VS, P2, '다시 재방문', ex=round((930 - 680) / 470, 4), ey=0, nx=0.5, ny=1, lx=0, loff=(42, 0), font=12)
text(470, 880, 50, 24, 'yes', size=12)

box(1180, 1080, 470, 70, '<b>상시 감시 (전 과정)</b><br>배터리 부족 → 도킹 복귀 · 비상정지 → 즉시 정지 · 통신 3초 끊김 → 정지', ADD.replace('fontSize=14', 'fontSize=12'))
text(1240, 12, 400, 22, add_note('주황 점선 · 주황 글씨 = 이번에 추가 · 수정한 부분'), size=12, align='right')

xml = ('<mxfile host="app.diagrams.net"><diagram id="robotA-logic" name="우리의 로직">'
       '<mxGraphModel dx="1640" dy="1160" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
       'fold="1" page="1" pageScale="1" pageWidth="1660" pageHeight="1160" math="0" shadow="0"><root>'
       '<mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1], 'w', encoding='utf-8').write(xml)
print('cells', len(cells))
