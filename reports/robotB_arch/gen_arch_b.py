#!/usr/bin/env python3
"""Robot A system architecture diagram (draw.io) — localization 2 + nav2 10 + our logic."""
import sys
from xml.sax.saxutils import escape, quoteattr

RED, BLUE, INK, GREY = '#D62728', '#1F5FD6', '#333333', '#9A9A9A'
cells = []
_id = [1]


def nid():
    _id[0] += 1
    return f'c{_id[0]}'


def S(**kw):
    return ';'.join(f'{k}={v}' for k, v in kw.items()) + ';'


def box(x, y, w, h, html, style, cid=None, parent='1'):
    cid = cid or nid()
    cells.append(f'<mxCell id="{cid}" value={quoteattr(html)} style="{style}" vertex="1" parent="{parent}">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    return cid


def edge(src, tgt, label='', color=INK, dashed=False, points=(), ex=None, ey=None, nx=None, ny=None,
         lx=0, loff=(0, 0), both=False, width=2, font=10, end='block', spt=None, tpt=None, lbg='#FFFFFF'):
    st = dict(edgeStyle='orthogonalEdgeStyle', rounded=0, html=1, endArrow=end, endFill=1, strokeColor=color,
              strokeWidth=width, fontSize=font, fontColor=color if color != GREY else '#666666',
              labelBackgroundColor=lbg, jumpStyle='arc', jumpSize=8)
    if dashed:
        st['dashed'] = 1
    if both:
        st.update(startArrow='block', startFill=1)
    for k, v in (('exitX', ex), ('exitY', ey), ('entryX', nx), ('entryY', ny)):
        if v is not None:
            st[k] = v
    if ex is not None:
        st['exitPerimeter'] = 0
    if nx is not None:
        st['entryPerimeter'] = 0
    cid = nid()
    s = f' source="{src}"' if src else ''
    t = f' target="{tgt}"' if tgt else ''
    pts = ''.join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
    extra = ''
    arr = ('<Array as="points">' + pts + '</Array>') if pts else ''
    if spt:
        extra += f'<mxPoint x="{spt[0]}" y="{spt[1]}" as="sourcePoint"/>'
    if tpt:
        extra += f'<mxPoint x="{tpt[0]}" y="{tpt[1]}" as="targetPoint"/>'
    cells.append(f'<mxCell id="{cid}" value={quoteattr(label)} style="{S(**st)}" edge="1" parent="1"{s}{t}>'
                 f'<mxGeometry x="{lx}" relative="1" as="geometry">{extra}'
                 f'{arr}'
                 f'<mxPoint x="{loff[0]}" y="{loff[1]}" as="offset"/></mxGeometry></mxCell>')
    return cid


def t(name, *lines, sub=10):
    s = f'<b>{escape(name)}</b>'
    if lines:
        s += f'<br><span style="font-size:{sub}px">' + '<br>'.join(lines) + '</span>'
    return s


FONT = 'fontFamily=Helvetica'
def node(col, fill='#FFFFFF', dashed=False, align='center', fs=12):
    st = dict(rounded=1, whiteSpace='wrap', html=1, fillColor=fill, strokeColor=col, strokeWidth=1.5,
              fontSize=fs, fontColor='#1A1A1A', align=align, verticalAlign='middle', arcSize=10)
    if dashed:
        st.update(dashed=1, fontColor='#555555')
    if align == 'left':
        st['spacingLeft'] = 10
    return S(**st)


def group(col, fill, align='left'):
    return S(rounded=1, whiteSpace='wrap', html=1, fillColor=fill, strokeColor=col, strokeWidth=2, fontSize=15,
             fontStyle=1, fontColor=col, align=align, verticalAlign='top', spacingLeft=12, spacingTop=4, arcSize=3)


EXT = S(rounded=0, whiteSpace='wrap', html=1, fillColor='#F4F4F4', strokeColor=INK, strokeWidth=2, fontSize=13,
        fontColor='#1A1A1A', align='center', verticalAlign='middle')
TEXT = S(text=None, html=1, align='left', verticalAlign='middle', fontSize=12, fontColor='#1A1A1A', whiteSpace='wrap')
TEXT = 'text;' + TEXT.replace('text=None;', '')

LOC_C, LOC_F = '#C77700', '#FFF6E5'
NAV_C, NAV_F = '#2E7D4F', '#EEF7F0'
OUR_C, OUR_F = '#6A4BB0', '#F4F0FB'

# ---------- title & legend ----------
box(40, 18, 760, 30, '<b style="font-size:20px">로봇 B 시스템 설계도</b>'
    '<span style="font-size:13px;color:#555">  TurtleBot4 · ROS 2 Jazzy · namespace /robot&lt;m&gt; (PC2)</span>', TEXT)
for i, (col, dsh, wd, txt) in enumerate([(RED, False, 2, '외부 → PC (입력)'), (BLUE, False, 2, 'PC → 외부 (출력)'),
                                         (INK, False, 2, 'PC 내부 흐름'), (NAV_C, False, 3, 'Nav2 이동 요청 (goal ↔ result)'),
                                         (RED, True, 2, '점선 = SERVER와 주고받음'), (GREY, True, 2, '선택 · 미사용')]):
    x = 900 + (i % 3) * 270
    y = 20 + (i // 3) * 24
    edge(None, None, color=col, dashed=dsh, spt=(x, y + 8), tpt=(x + 44, y + 8), width=wd)
    box(x + 52, y, 215, 16, txt, TEXT.replace('fontSize=12', 'fontSize=11'))

# ---------- external (left) ----------
BOT = box(40, 160, 260, 300, t('Bot (로봇 B)', 'TurtleBot4 (/robot&lt;m&gt;)', '', 'Create3 베이스', '/odom · /tf · 배터리',
                                '/dock · /undock (action)', '', 'RPLIDAR → /scan', '',
                                'OAK-D → /oakd/rgb/preview/image_raw', sub=11), EXT)
MON = box(40, 560, 220, 110, '<b>System Monitor</b>', EXT)
SM = box(40, 850, 220, 600, t('SERVER', '', '섹터 이동 명령', '(섹터 번호 · 좌표 · yaw)', '', '정지 · 재개 신호', '', '사진 수신', '→ 수확 완료 판단', '',
                              '도킹 복귀 명령', sub=11), EXT)
PC3 = box(40, 1478, 105, 82, t('PC3', '웹캠 · 작업자', 'QR 인식', sub=10), EXT)
DET = box(155, 1478, 105, 82, t('Detect', '비전 인식 팀', '(YOLO)', sub=10), EXT)
edge(SM, MON, '전달', color=RED, dashed=True, ex=0.5, ey=0, nx=0.5, ny=1, font=10)
edge(PC3, SM, 'QR 인식<br>(확인 · 놓침)', color=RED, dashed=True, ex=0.5, ey=0, nx=round((92 - 40) / 220, 4), ny=1, font=9, loff=(-30, 0))
edge(SM, DET, '사진', color=BLUE, dashed=True, ex=round((185 - 40) / 220, 4), ey=1, nx=round((185 - 155) / 105, 4), ny=0, font=9, loff=(-14, 0))
edge(DET, SM, '판단 결과', color=RED, dashed=True, ex=round((240 - 155) / 105, 4), ey=0, nx=round((240 - 40) / 220, 4), ny=1, font=9, loff=(28, 0))

# ---------- PC ----------
box(360, 80, 1380, 1580, 'PC2  (원격 PC · ROS 2 Jazzy)',
    S(rounded=1, whiteSpace='wrap', html=1, fillColor='none', strokeColor=INK, strokeWidth=2.5, fontSize=17,
      fontStyle=1, fontColor=INK, align='left', verticalAlign='top', spacingLeft=14, spacingTop=6, arcSize=2))

# Localization
LOC = box(400, 120, 600, 210, 'Localization  <span style="font-weight:normal;font-size:12px">(localization.launch.py · 2개)</span>',
          group(LOC_C, LOC_F))
AMCL = box(430, 185, 200, 80, t('amcl', '맵 위 로봇 위치 추정', '구독 /scan · /map · /initialpose',
                                 '발행 /amcl_pose · TF map→odom'), node(LOC_C))
MAP = box(680, 185, 200, 80, t('map_server', '저장한 맵 (.yaml · .pgm) 불러오기', '발행 /map'), node(LOC_C))
box(430, 282, 450, 32, '<b>lifecycle_manager_localization</b>  <span style="font-size:10px">두 노드 켜기·끄기 (configure → activate)</span>',
    node('#B8A07A', '#FBF3E4', fs=11))
RVIZ = box(1080, 140, 230, 70, t('RViz2 (PC)', '2D Pose Estimate로 초기 위치 지정', 'Nav2 Goal · 맵 · 경로 보기'),
           node('#777777', '#FAFAFA'))

# Nav2
NAV = box(400, 380, 1240, 380, 'Navigation (Nav2)  <span style="font-weight:normal;font-size:12px">(nav2.launch.py · 10개)</span>',
          group(NAV_C, NAV_F, align='center'))
COL = node(NAV_C)
COLL = box(425, 550, 190, 70, t('collision_monitor', '장애물 가까우면 감속·정지', 'cmd_vel_smoothed → /cmd_vel'), COL)
VEL = box(665, 550, 190, 70, t('velocity_smoother', '가감속 제한', 'cmd_vel_nav → cmd_vel_smoothed'), COL)
PLAN = box(925, 412, 230, 56, t('planner_server', '전체 경로 계산 · NavFn · global costmap'), COL)
SMO = box(925, 480, 230, 56, t('smoother_server', '경로 다듬기 (smooth_path)'), COL)
CTRL = box(925, 550, 230, 56, t('controller_server', '경로 따라가기 · MPPI · local costmap'), COL)
BEH = box(925, 620, 230, 56, t('behavior_server', '막혔을 때 회복: spin · backup · wait'), COL)
BT = box(1265, 412, 170, 264, t('bt_navigator', '목표를 받는 창구', '', '행동 트리(BT)로', '왼쪽 서버들을', '순서대로 호출', '',
                                'action', 'navigate_to_pose', 'navigate_through_poses'), node(NAV_C, '#FFFFFF', fs=13))
WPF = box(1475, 470, 150, 100, t('waypoint_follower', '여러 지점 차례로 방문', 'follow_waypoints'), COL)
DOCKS = box(425, 650, 190, 62, t('docking_server', 'Nav2 도킹 (dock_robot)', '수업 방식은 Create3 /dock'),
            node(GREY, '#FFFFFF', dashed=True))
ROUTE = box(665, 650, 190, 62, t('route_server', '경로 그래프 계획', 'TurtleBot4 설정 없음 · 미사용'),
            node(GREY, '#FFFFFF', dashed=True))
box(925, 700, 290, 40, '<b>lifecycle_manager_navigation</b><br><span style="font-size:10px">10개 노드 켜기·끄기</span>',
    node('#86A98F', '#E3F0E6', fs=11))

for tg, yy in ((PLAN, 440), (SMO, 508), (CTRL, 578), (BEH, 648)):
    edge(BT, tg, color=INK, ex=0, ey=round((yy - 412) / 264, 4), nx=1, ny=0.5, width=1.5)
edge(CTRL, VEL, color=INK, ex=0, ey=0.5, nx=1, ny=0.4, points=((890, 578), (890, 578)), width=1.5)
edge(BEH, VEL, color=INK, dashed=True, ex=0, ey=0.5, nx=1, ny=0.8, points=((900, 648), (900, 606)), width=1.5)
edge(VEL, COLL, color=INK, ex=0, ey=0.4, nx=1, ny=0.4, width=1.5)
edge(WPF, BT, label='', color=INK, ex=0, ey=0.5, nx=1, ny=round((520 - 412) / 264, 4), width=1.5)

# separator (dashed) like the sketch
edge(None, None, color='#777777', dashed=True, end='none', width=1.5, spt=(400, 780), tpt=(1640, 780))

# separator (dashed) like the sketch
edge(None, None, color='#777777', dashed=True, end='none', width=1.5, spt=(400, 780), tpt=(1700, 780))

# Robot B logic — team flowchart (전체 흐름 · ① 섹터 이동 · ② 섹터 작업 · ③ 도킹 복귀) wired step by step
LOGIC = box(400, 800, 1300, 800, '우리의 로직  <span style="font-weight:normal;font-size:12px">Robot B 미션 흐름 (판단 주체: SERVER)</span>',
            group(OUR_C, OUR_F))
STP = node(OUR_C, '#FFFFFF', fs=12)
def step(x, y, w, h, html): return box(x, y, w, h, html, STP)
def dec(x, y, w, h, html):
    return box(x, y, w, h, html, 'rhombus;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=OUR_C,
                                                strokeWidth=1.5, fontSize=11, fontColor='#1A1A1A'))
def term(x, y, w, h, html):
    return box(x, y, w, h, html, 'ellipse;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=RED,
                                                strokeWidth=1.8, fontSize=13, fontColor=RED))
def conn(x, y, w, h, direction):
    return box(x, y, w, h, '', 'shape=triangle;perimeter=trianglePerimeter;' + S(direction=direction, whiteSpace='wrap', html=1, fillColor='#EDE7F6', strokeColor=OUR_C, strokeWidth=1.3))
def sec(x, y, w, txt):
    box(x, y, w, 18, f'<b>{txt}</b>', TEXT.replace('fontSize=12', 'fontSize=12') + f'fontColor={OUR_C};')
def go(a, b, label='', **kw):
    kw.setdefault('width', 1.4)
    kw.setdefault('font', 10)
    return edge(a, b, label=label, color=kw.pop('color', '#444444'), **kw)
NAVL = dict(color=NAV_C, width=2.5, font=11)

# row A — 전체 흐름 → ① 섹터 이동 시작
S0 = term(430, 855, 90, 50, '<b>시작</b>')
W0 = step(545, 852, 165, 56, '<b>도킹 상태로 대기</b><br><span style="font-size:10px">초기 상태 · 충전 중</span>')
C1 = dec(735, 835, 150, 90, '섹터 이동<br>명령 받음?')
D0 = dec(905, 840, 140, 80, '<b>도킹 상태?</b>')
U0 = step(1070, 857, 150, 46, '<b>언도킹</b><br><span style="font-size:10px">undock 액션</span>')
G0 = step(1290, 852, 160, 56, '<b>Nav2 목표 전송</b><br><span style="font-size:10px">섹터 좌표 · 방향(yaw)</span>')
CIN = conn(961, 812, 28, 26, 'south')
box(835, 806, 115, 24, '<span style="font-size:10px;color:#6A4BB0">③에서 다음 섹터</span>', TEXT.replace('align=left', 'align=right'))
# row B/C — 이동 중 정지 · 재개
ST = dec(1290, 965, 160, 90, '정지 신호<br>받음?')
CX = step(1480, 985, 150, 50, '<b>Nav2 목표 취소</b><br><span style="font-size:10px">정지 유지</span>')
RS = dec(1480, 1070, 150, 90, '재개 신호 받음?<br><span style="font-size:10px">(QR 다시 인식)</span>')
RG = step(1480, 1185, 150, 50, '<b>같은 목표 재전송</b><br><span style="font-size:10px">이동 재개</span>')
AR = dec(1290, 1105, 160, 90, '섹터 도착?')
# row D — ② 섹터 작업
YAW = step(1290, 1262, 160, 56, '<b>토마토 방향 확인</b><br><span style="font-size:10px">도착 yaw 유지 · 정지</span>')
CAP = step(1090, 1265, 160, 50, '<b>OAK-D 촬영</b><br><span style="font-size:10px">0.5fps (2초에 1장)</span>')
SEND = box(860, 1262, 200, 56, '<b>사진 서버로 전송</b><br><span style="font-size:10px">압축 이미지 + 촬영 시각</span>',
           'shape=parallelogram;perimeter=parallelogramPerimeter;fixedSize=1;size=14;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF',
                                                                                         strokeColor=OUR_C, strokeWidth=1.5, fontSize=12))
NC = dec(660, 1245, 170, 90, '새 이동 명령<br>받음?')
sec(1292, 1324, 220, '② 섹터 작업 (촬영 · 전송)')
# row E — 다음 명령 종류
STOP = step(660, 1372, 170, 46, '<b>촬영 중지</b><br><span style="font-size:10px">명령을 받으면 즉시</span>')
K0 = dec(430, 1350, 170, 90, '다음 명령<br>종류?')
COUT = conn(501, 1322, 28, 28, 'north')
box(533, 1322, 130, 24, '<span style="font-size:10px;color:#6A4BB0">섹터 이동 → ① 도킹 상태?로</span>', TEXT)
# row F — ③ 도킹 복귀
DG = step(430, 1478, 170, 46, '<b>도킹 스테이션으로 이동</b><br><span style="font-size:10px">Nav2</span>')
DA = dec(640, 1455, 160, 90, '도킹 스테이션<br>앞 도착?')
DK = step(840, 1478, 140, 46, '<b>도킹</b><br><span style="font-size:10px">dock 액션</span>')
DS = dec(1010, 1455, 150, 90, '도킹 성공?')
END = term(1040, 1556, 90, 34, '<b>끝</b>')
sec(600, 1560, 200, '③ 도킹 복귀 · 종료')
box(1200, 1462, 470, 120, '<b>미정 사항</b> (흐름도 기준)<br>• QR 유예 시간 값 — 비전 파트 테스트 후<br>• 다음 작업이 아직 없을 때 대기 방식 (제자리 / 도킹 복귀)<br>'
    '• 도킹 복귀 중 QR 추종 적용 여부 · 도킹 결과 서버 보고 여부<br>• 이동 명령에 작업 번호 포함 여부 · ④ 비상 상황은 이번 범위 제외',
    S(rounded=1, whiteSpace='wrap', html=1, fillColor='#FFFBEA', strokeColor='#C9A400', strokeWidth=1, dashed=1, fontSize=10,
      fontColor='#333333', align='left', verticalAlign='top', spacingLeft=10, spacingTop=6, arcSize=6))

# flow
go(S0, W0); go(W0, C1)
go(C1, D0, '예')
go(C1, W0, '아니오 · 계속 대기', ex=0.5, ey=1, nx=0.5, ny=1, points=((810, 940), (627, 940)), lx=-0.1)
go(D0, U0, '예')
go(D0, G0, '아니오 (섹터에서 출발)', ex=0.5, ey=1, nx=0, ny=0.75, points=((975, 945), (1275, 945), (1275, 894)), lx=-0.2)
go(U0, G0, nx=0, ny=0.25)
go(G0, ST, ex=0.5, ey=1, nx=0.5, ny=0)
go(ST, CX, '예')
go(CX, RS, ex=round((1555 - 1480) / 150, 4), ey=1, nx=0.5, ny=0)
go(RS, CX, '아니오<br>정지 유지', ex=1, ey=0.5, nx=1, ny=0.5, points=((1652, 1115), (1652, 1010)), loff=(24, 0), font=9)
go(RS, RG, '예', ex=0.5, ey=1, nx=0.5, ny=0)
go(ST, AR, '아니오', ex=0.5, ey=1, nx=0.5, ny=0)
go(RG, AR, ex=0, ey=0.5, nx=1, ny=0.5, points=((1465, 1210), (1465, 1150)))
go(AR, ST, '아니오<br>이동 계속', ex=0, ey=0.5, nx=0, ny=0.5, points=((1270, 1150), (1270, 1010)), loff=(-24, 0), font=9)
go(AR, YAW, '예', ex=0.5, ey=1, nx=0.5, ny=0)
go(YAW, CAP); go(CAP, SEND); go(SEND, NC)
go(NC, CAP, '아니오 · 계속 촬영', ex=0.5, ey=0, nx=0.5, ny=0, points=((745, 1232), (1170, 1232)), lx=0.1)
go(NC, STOP, '예', ex=0.5, ey=1, nx=0.5, ny=0)
go(STOP, K0)
go(K0, DG, '도킹 복귀', ex=0.5, ey=1, nx=round((515 - 430) / 170, 4), ny=0, font=9, loff=(-30, 0))
go(DG, DA); go(DA, DK, '예'); go(DK, DS)
go(DA, DG, '아니오 · 이동 계속', ex=0.5, ey=0, nx=round((565 - 430) / 170, 4), ny=0, points=((720, 1446), (565, 1446)), lx=-0.2, font=9)
go(DS, DK, '아니오 · 다시 시도', ex=0.5, ey=0, nx=0.5, ny=0, points=((1085, 1446), (910, 1446)), lx=0.0, font=9)
go(DS, END, '예', ex=0.5, ey=1, nx=0.5, ny=0)

# logic <-> Nav2 (bt_navigator)
edge(G0, BT, 'goal ↔ result', ex=0.25, ey=0, nx=round((1330 - 1265) / 170, 4), ny=1, loff=(-42, 0), both=True, **NAVL)
edge(CX, BT, '목표 취소 (cancel)', ex=0.5, ey=0, nx=round((1400 - 1265) / 170, 4), ny=1, points=((1555, 775), (1400, 775)),
     lx=-0.55, loff=(46, 0), **NAVL)
edge(RG, BT, '같은 goal 재전송 ↔ result', ex=1, ey=0.5, nx=round((1420 - 1265) / 170, 4), ny=1,
     points=((1672, 1210), (1672, 765), (1420, 765)), lx=-0.45, loff=(52, 0), both=True, **NAVL)
edge(DG, BT, '도킹 위치 goal ↔ result', ex=0.5, ey=1, nx=1, ny=round((650 - 412) / 264, 4),
     points=((515, 1600), (1690, 1600), (1690, 650)), lx=-0.1, loff=(0, -10), both=True, **NAVL)

# localization internals & interplay
edge(MAP, AMCL, color=INK, ex=0, ey=0.375, nx=1, ny=0.375, width=1.5)
edge(RVIZ, AMCL, label='/initialpose', color=INK, ex=0, ey=round((165 - 140) / 70, 4), nx=0.5, ny=0,
     points=((530, 165),), width=1.5, lx=0.3)
edge(LOC, NAV, label='/map → global costmap<br>TF map→odom (로봇 위치)', color=INK, ex=round((780 - 400) / 600, 4), ey=1,
     nx=round((780 - 400) / 1240, 4), ny=0, width=2.5, font=11, loff=(95, 0))

# Bot <-> PC
edge(BOT, AMCL, label='/scan · /tf', color=RED, ex=1, ey=round((200 - 160) / 300, 4), nx=0, ny=round((200 - 185) / 80, 4))
edge(COLL, BOT, label='/cmd_vel', color=BLUE, ex=0.5, ey=0, nx=1, ny=round((355 - 160) / 300, 4), points=((520, 355),),
     lx=0.55, width=2.5, font=11)
edge(BOT, NAV, label='/scan · /odom · /tf', color=RED, ex=1, ey=round((388 - 160) / 300, 4), nx=0,
     ny=round((388 - 380) / 380, 4), loff=(0, -10))
# Bot <-> logic steps
by = lambda y: round((y - 160) / 300, 4)
edge(U0, BOT, '/undock', color=BLUE, ex=0.5, ey=0, nx=1, ny=by(398), points=((1145, 790), (394, 790), (394, 398)), lx=-0.75, loff=(0, -9), font=10)
edge(BOT, D0, 'dock_status', color=RED, ex=1, ey=by(410), nx=0.75, ny=0.25, points=((380, 410), (380, 797), (1010, 797)), lx=-0.05, loff=(0, -9), font=10)
edge(BOT, CAP, '카메라 이미지', color=RED, ex=0, ey=by(430), nx=0.5, ny=1, points=((14, 430), (14, 1640), (1170, 1640)), lx=0.55, loff=(0, 10), font=10)
edge(DK, BOT, '/dock', color=BLUE, ex=round((910 - 840) / 140, 4), ey=1, nx=0, ny=by(445), points=((910, 1630), (22, 1630), (22, 445)),
     lx=-0.6, loff=(0, -9), font=10)

# SERVER <-> logic steps (dashed)
sy = lambda y: round((y - 850) / 600, 4)
SMD = dict(dashed=True, font=10)
edge(SM, C1, '섹터 이동 명령', color=RED, ex=1, ey=sy(862), nx=0.25, ny=0.25, points=((335, 862), (335, 836), (772, 836)), lx=-0.88, loff=(0, -9), **SMD)
edge(SM, ST, '정지 신호', color=RED, ex=1, ey=sy(960), nx=0.25, ny=0.25, points=((1330, 960),), lx=-0.75, loff=(0, -9), **SMD)
edge(SM, RS, '재개 신호 (QR 다시 인식)', color=RED, ex=1, ey=sy(1070), nx=0, ny=0.5, points=((1465, 1070), (1465, 1115)), lx=-0.7, loff=(0, -9), **SMD)
edge(SEND, SM, '사진 (압축 이미지 + 촬영 시각 · 0.5fps)', color=BLUE, ex=0.5, ey=0, nx=1, ny=sy(1240), points=((960, 1240),), lx=0.45, loff=(0, -9), **SMD)
edge(SM, NC, '새 이동 명령', color=RED, ex=1, ey=sy(1290), nx=0, ny=0.5, lx=-0.4, loff=(0, -9), **SMD)
edge(SM, K0, '다음 명령<br>(섹터 이동 / 도킹 복귀)', color=RED, ex=1, ey=sy(1395), nx=0, ny=0.5, lx=-0.1, loff=(0, -16), **SMD)

xml = ('<mxfile host="app.diagrams.net"><diagram id="robotB-arch" name="로봇 B 시스템 설계도">'
       '<mxGraphModel dx="1720" dy="1680" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
       'fold="1" page="1" pageScale="1" pageWidth="1720" pageHeight="1680" math="0" shadow="0"><root>'
       '<mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1], 'w', encoding='utf-8').write(xml)
print('cells', len(cells))
