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
box(40, 18, 760, 30, '<b style="font-size:20px">로봇 A 시스템 설계도</b>'
    '<span style="font-size:13px;color:#555">  TurtleBot4 · ROS 2 Jazzy · namespace /robot&lt;n&gt;</span>', TEXT)
for i, (col, dsh, wd, txt) in enumerate([(RED, False, 2, '외부 → PC (입력)'), (BLUE, False, 2, 'PC → 외부 (출력)'),
                                         (INK, False, 2, 'PC 내부 흐름'), (NAV_C, False, 3, 'Nav2 이동 요청 (goal ↔ result)'),
                                         (RED, True, 2, '점선 = 서버(SM)와 주고받음'), (GREY, True, 2, '선택 · 미사용')]):
    x = 900 + (i % 3) * 270
    y = 20 + (i // 3) * 24
    edge(None, None, color=col, dashed=dsh, spt=(x, y + 8), tpt=(x + 44, y + 8), width=wd)
    box(x + 52, y, 215, 16, txt, TEXT.replace('fontSize=12', 'fontSize=11'))

# ---------- external (left) ----------
# Robot A — what actually runs on the TurtleBot4 (turtlebot4_bringup standard.launch.py on the Pi + Create 3 firmware)
ROBOT = box(30, 105, 280, 452, '<b>로봇 A · TurtleBot4</b>  <span style="font-weight:normal;font-size:11px">(/robot&lt;n&gt;)</span>',
            S(rounded=1, whiteSpace='wrap', html=1, fillColor='#F4F4F4', strokeColor=INK, strokeWidth=2, fontSize=14, fontColor='#1A1A1A',
              align='center', verticalAlign='top', spacingTop=2, arcSize=4))
SUBG = lambda title: S(rounded=1, whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor='#888888', strokeWidth=1, dashed=1, fontSize=10,
                      fontStyle=1, fontColor='#444444', align='left', verticalAlign='top', spacingLeft=6, spacingTop=1, arcSize=4)
box(38, 128, 264, 262, 'Raspberry Pi 4 <span style="font-weight:normal">· turtlebot4_bringup (부팅 시 자동 실행)</span>', SUBG(''))
box(38, 400, 264, 150, 'Create 3 베이스 <span style="font-weight:normal">· 자체 펌웨어 (토픽은 republisher가 중계)</span>', SUBG(''))
RN = lambda col='#555555', fill='#FFFFFF': S(rounded=1, whiteSpace='wrap', html=1, fillColor=fill, strokeColor=col, strokeWidth=1.2, fontSize=10,
                                            fontColor='#1A1A1A', align='left', verticalAlign='middle', spacingLeft=6, arcSize=10)
RSP = box(48, 150, 244, 38, '<b>robot_state_publisher</b> · joint_state_publisher<br>→ /tf_static (라이다 · 카메라 위치)', RN())
LID = box(48, 194, 244, 40, '<b>rplidar_composition</b> (rplidar_ros)<br>라이다 드라이버 → /scan', RN())
REP = box(48, 240, 244, 40, '<b>create3_republisher</b><br>Create 3 토픽·액션을 /robot&lt;n&gt;/… 로 중계', RN())
box(48, 286, 244, 32, 'turtlebot4_node · base_node  <span style="color:#777">버튼 · 화면 · LED</span>', RN('#AAAAAA', '#FAFAFA'))
OAK = box(48, 324, 244, 66, '<b>oakd</b> (depthai_ros_driver)<br>카메라 드라이버 · 이미지를 <b>계속</b> 발행<br>/oakd/rgb/preview/image_raw', RN())
C1 = box(48, 422, 244, 38, '<b>바퀴 구동 · 주행거리</b><br>/cmd_vel 구독 → /odom · TF odom→base_link', RN())
C2 = box(48, 466, 244, 38, '<b>도킹</b><br>/dock · /undock 액션 서버 · /dock_status', RN())
C3 = box(48, 510, 244, 32, '<b>배터리 · 안전 센서</b>  /battery_state · /hazard_detection', RN())
MON = box(40, 575, 220, 150, '<b>System Monitor</b>', EXT)
DET = box(40, 1505, 220, 70, t('Detect', '비전 인식 팀 (YOLO)', sub=11), EXT)
SM = box(40, 850, 220, 620, t('SERVER', '', '작업 지시', '결과 저장', '재방문 목록', '(remission_list)', 'B 작업 상태', sub=11), EXT)
edge(SM, MON, '전달', color=RED, dashed=True, ex=0.5, ey=0, nx=0.5, ny=1, font=10)

# ---------- PC ----------
box(360, 80, 1320, 1530, 'PC  (원격 PC · ROS 2 Jazzy)',
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

# Our logic — the team's flowchart; every step is wired to the Nav2 / Bot / SM item it talks to
LG_Y, LG_H = 800, 760
LOGIC = box(400, LG_Y, 1240, LG_H, '우리의 로직  <span style="font-weight:normal;font-size:12px">Robot A 미션 흐름</span>',
            group(OUR_C, OUR_F, align='right').replace('verticalAlign=top', 'verticalAlign=bottom').replace('spacingTop=4', 'spacingBottom=6'))
STP = node(OUR_C, '#FFFFFF', fs=12)
def step(x, y, w, h, html): return box(x, y, w, h, html, STP)
def dec(x, y, w, h, html):
    return box(x, y, w, h, html, 'rhombus;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=OUR_C,
                                                strokeWidth=1.5, fontSize=11, fontColor='#1A1A1A'))
def go(a, b, label='', **kw):
    kw.setdefault('width', 1.4)
    return edge(a, b, label=label, color=kw.pop('color', '#444444'), **kw)
HL = lambda t_: f'<span style="background-color:#FFF176">&nbsp;{t_}&nbsp;</span>'
NAVL = dict(color=NAV_C, width=2.5, font=11, both=True)

# row A — start & patrol entry
S0 = box(430, 850, 140, 60, '<b>작업 시작</b>', 'ellipse;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=RED,
                                                                strokeWidth=1.8, fontSize=13, fontColor=RED))
D0 = dec(610, 835, 160, 90, '<b>is initial pose<br>&amp; docked?</b>')
U0 = step(810, 857, 140, 46, '<b>언도킹</b>')
P1 = step(990, 850, 220, 60, HL('<b>순찰 자율주행</b>') + '<br><span style="font-size:11px">좌표 1,2,3,4 (i = 1부터)</span>')
M1 = step(1290, 857, 160, 46, '<b>좌표 i로 이동</b>')
# row B
D1 = dec(1280, 965, 180, 90, 'i 이동 완료?')
T1 = step(1140, 989, 110, 42, 'TB4 stop')
O1 = step(840, 975, 260, 70, HL('<b>oakd 캡처 실행</b>') + '<br>토마토 캡처 후 server에 전송')
FD = dec(620, 960, 170, 100, 'i = final<br>sector?')
# row C
VS = step(420, 1118, 180, 64, '<b>visit subscriber</b><br><span style="font-size:11px">remission_list에 좌표 저장</span>')
P2 = step(640, 1115, 240, 70, HL('<b>재방문 순찰 자율주행</b>') + '<br><span style="font-size:11px">(b에게서 방문한 좌표 수신)</span>')
M2 = step(1290, 1127, 160, 46, '<b>남은 좌표로 이동</b>')
# row D
D2 = dec(1280, 1245, 180, 90, 'list 좌표<br>이동 완료?')
T2 = step(1140, 1269, 110, 42, 'TB4 stop')
O2 = step(860, 1255, 240, 70, '<b>oakd 캡처 실행</b><br>캡처 후 server에 전송')
D3 = dec(620, 1240, 170, 100, 'list에 남은<br>좌표?')
# row E
WT = step(410, 1392, 170, 46, '잠시 대기 후<br>다시 확인')
BW = dec(620, 1370, 170, 90, 'B 작업<br>끝났나?')
EN = step(840, 1385, 220, 60, '<b>현 작업 종료 및</b><br><b>도킹 스테이션 이동</b>')
END = box(880, 1478, 140, 28, '<b>작업종료</b>', TEXT.replace('align=left', 'align=center').replace('fontSize=12', 'fontSize=14'))
SAFE = box(420, 1470, 420, 72, '<b>상시 감시 (전 과정)</b><br>배터리 부족 → 도킹 복귀 · 비상정지 → 즉시 정지<br>통신 3초 끊김 → 정지',
    node('#B58A00', '#FFFBEA', fs=11))

# flow
go(S0, D0); go(D0, U0, 'yes', lx=-0.3); go(U0, P1)
go(D0, P1, 'no (바로 출발)', ex=0.5, ey=1, nx=0.5, ny=1, points=((690, 940), (1100, 940)), lx=-0.55, font=10)
go(P1, M1, '<b>nav2</b>', font=11, lbg='#F4A3A3')
go(M1, D1, ex=0.5, ey=1, nx=0.5, ny=0)
go(D1, M1, 'no (재확인 ·<br>3회 실패 시 건너뜀)', ex=1, ey=0.5, nx=1, ny=0.5, points=((1490, 1010), (1490, 880)), loff=(48, 0), font=9)
go(D1, T1, 'yes', lx=-0.2); go(T1, O1); go(O1, FD)
go(FD, P1, 'no · i = i+1', ex=0.5, ey=0, nx=0.5, ny=1, points=((705, 940), (1100, 940)), lx=0.0, loff=(0, 10), font=10)
go(FD, P2, 'yes', ex=0.5, ey=1, nx=round((705 - 640) / 240, 4), ny=0, lx=-0.2)
go(VS, P2, '다시<br>재방문', font=10)
go(P2, M2, '<b>nav2</b>', font=11, lbg='#F4A3A3')
go(M2, D2, ex=0.5, ey=1, nx=0.5, ny=0)
go(D2, M2, 'no (재확인 ·<br>3회 실패 시 건너뜀)', ex=1, ey=0.5, nx=1, ny=0.75, points=((1490, 1290), (1490, 1162)), loff=(48, 0), font=9)
go(D2, T2, 'yes', lx=-0.2); go(T2, O2); go(O2, D3)
go(D3, VS, 'yes · 방문한 좌표 remove<br>(DB에도 반영)', ex=0, ey=0.5, nx=round((510 - 420) / 180, 4), ny=1, points=((510, 1290),), lx=-0.45, loff=(0, 0), font=9)
go(D3, BW, 'no', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.2)
go(BW, EN, 'yes', lx=-0.2)
go(BW, WT, 'no', lx=-0.2)
go(WT, D3, '', ex=round((495 - 410) / 170, 4), ey=0, nx=0.25, ny=0.75, points=((495, 1315),))
go(EN, END, ex=round((950 - 840) / 220, 4), ey=1, nx=0.5, ny=0)

# logic <-> Nav2 (bt_navigator): each move step individually
edge(M1, BT, 'goal ↔ result', ex=round((1330 - 1290) / 160, 4), ey=0, nx=round((1330 - 1265) / 170, 4), ny=1, loff=(-42, 0), **NAVL)
edge(M2, BT, 'goal ↔ result', ex=1, ey=0.25, nx=round((1390 - 1265) / 170, 4), ny=1, points=((1520, 1138), (1520, 790), (1390, 790)),
     lx=-0.35, loff=(40, 0), **NAVL)
edge(EN, BT, '도킹 위치 goal ↔ result', ex=1, ey=0.2, nx=round((1420 - 1265) / 170, 4), ny=1,
     points=((1545, 1397), (1545, 775), (1420, 775)), lx=-0.75, loff=(0, -10), **NAVL)

# localization internals & interplay
edge(MAP, AMCL, color=INK, ex=0, ey=0.375, nx=1, ny=0.375, width=1.5)
edge(RVIZ, AMCL, label='/initialpose', color=INK, ex=0, ey=round((165 - 140) / 70, 4), nx=0.5, ny=0,
     points=((530, 165),), width=1.5, lx=0.3)
edge(LOC, NAV, label='/map → global costmap<br>TF map→odom (로봇 위치)', color=INK, ex=round((780 - 400) / 600, 4), ey=1,
     nx=round((780 - 400) / 1240, 4), ny=0, width=2.5, font=11, loff=(95, 0))

# Robot nodes <-> Localization / Nav2
ry = lambda node_y, h, y: round((y - node_y) / h, 4)
edge(RSP, LOC, '/tf_static', color=RED, ex=1, ey=ry(150, 38, 169), nx=0, ny=round((169 - 120) / 210, 4), lx=0.1, loff=(0, -9), font=10)
edge(LID, AMCL, '/scan', color=RED, ex=1, ey=ry(194, 40, 205), nx=0, ny=round((205 - 185) / 80, 4), lx=0.1, loff=(0, -9), font=10)
edge(LID, NAV, '/scan (costmap · collision_monitor)', color=RED, ex=1, ey=ry(194, 40, 224), nx=round((410 - 400) / 1240, 4), ny=0,
     points=((410, 224),), lx=0.7, loff=(95, 0), font=10)
edge(C1, NAV, '/odom · TF odom→base_link', color=RED, ex=1, ey=ry(422, 38, 434), nx=0, ny=round((434 - 380) / 380, 4), lx=0.1, loff=(0, -9), font=10)
edge(COLL, C1, '/cmd_vel', color=BLUE, ex=0, ey=0.5, nx=1, ny=ry(422, 38, 452), points=((408, 585), (408, 452)), lx=0.75, loff=(0, 9), width=2.5, font=11)

# Robot nodes <-> logic steps (each individually)
edge(C2, D0, 'dock_status', color=RED, ex=1, ey=ry(466, 38, 494), nx=0.5, ny=0, points=((370, 494), (370, 828), (690, 828)), lx=0.55, loff=(0, -9), font=10)
edge(U0, C2, '/undock', color=BLUE, ex=0.5, ey=0, nx=1, ny=ry(466, 38, 478), points=((880, 818), (382, 818), (382, 478)), lx=-0.7, loff=(0, -9), font=10)
edge(OAK, O1, '카메라 이미지', color=RED, ex=1, ey=ry(324, 66, 386), nx=round((975 - 840) / 260, 4), ny=0,
     points=((394, 386), (394, 808), (975, 808)), lx=0.62, loff=(0, -9), font=10)
edge(OAK, O2, '카메라 이미지', color=RED, ex=0, ey=ry(324, 66, 340), nx=round((1090 - 860) / 240, 4), ny=1,
     points=((8, 340), (8, 1600), (1090, 1600)), lx=0.55, loff=(0, 10), font=10)
edge(EN, C2, '/dock', color=BLUE, ex=1, ey=0.75, nx=0, ny=ry(466, 38, 485), points=((1075, 1430), (1075, 1592), (16, 1592), (16, 485)),
     lx=-0.62, loff=(0, -9), font=10)
edge(C3, SAFE, '/battery_state · /hazard_detection', color=RED, ex=0, ey=0.5, nx=round((630 - 420) / 420, 4), ny=1,
     points=((24, 526), (24, 1584), (630, 1584)), lx=0.75, loff=(0, -9), font=10)

# SM <-> logic steps (dashed = server)
sy = lambda y: round((y - 850) / 620, 4)
SMD = dict(dashed=True, font=10)
edge(SM, S0, '작업 시작', color=RED, ex=1, ey=sy(880), nx=0, ny=0.5, lx=-0.3, loff=(0, -9), **SMD)
edge(O1, SM, 'a_mission · 좌표 · image', color=BLUE, ex=round((960 - 840) / 260, 4), ey=1, nx=1, ny=sy(1085),
     points=((960, 1085),), lx=0.55, loff=(0, -9), **SMD)
edge(SM, VS, 'remission_list<br>(DB에서 받아오기)', color=RED, ex=1, ey=sy(1150), nx=0, ny=0.5, lx=-0.1, loff=(0, -16), **SMD)
edge(SM, P2, 'b가 방문한 좌표', color=RED, ex=1, ey=sy(1206), nx=round((800 - 640) / 240, 4), ny=1, points=((800, 1206),), lx=-0.55, loff=(0, -9), **SMD)
edge(SM, D3, 'server에서 b 방문 좌표 subscribe', color=RED, ex=1, ey=sy(1226), nx=0.5, ny=0, points=((705, 1226),), lx=-0.25, loff=(0, 10), **SMD)
edge(O2, SM, 'a_remission · 좌표 · image', color=BLUE, ex=round((980 - 860) / 240, 4), ey=1, nx=1, ny=sy(1352),
     points=((980, 1352),), lx=0.6, loff=(0, -9), **SMD)
edge(SM, BW, 'B 작업 상태', color=RED, ex=1, ey=sy(1455), nx=0.25, ny=0.75, points=((662, 1455),), lx=-0.5, loff=(0, 10), **SMD)

# SM <-> Detect
edge(SM, DET, 'image', color=BLUE, ex=0.3, ey=1, nx=0.3, ny=0, loff=(-24, 0), **SMD)
edge(DET, SM, '탐지 결과 → DB', color=RED, ex=0.7, ey=0, nx=0.7, ny=1, loff=(46, 0), **SMD)

xml = ('<mxfile host="app.diagrams.net"><diagram id="robotA-arch" name="로봇 A 시스템 설계도">'
       '<mxGraphModel dx="1720" dy="1640" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
       'fold="1" page="1" pageScale="1" pageWidth="1720" pageHeight="1640" math="0" shadow="0"><root>'
       '<mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1], 'w', encoding='utf-8').write(xml)
print('cells', len(cells))
