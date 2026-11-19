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
    '<span style="font-size:13px;color:#555">  TurtleBot4 · ROS 2 Jazzy · namespace /robot_a · 토픽명은 팀별 토픽 요청서 기준</span>', TEXT)
for i, (col, dsh, wd, txt) in enumerate([(RED, False, 2, '외부 → PC (입력)'), (BLUE, False, 2, 'PC → 외부 (출력)'),
                                         (INK, False, 2, 'PC 내부 흐름'), (NAV_C, False, 3, 'Nav2 이동 요청 (goal ↔ result)'),
                                         (RED, True, 2, '점선 = SERVER와 주고받음'), (GREY, True, 2, '선택 · 미사용')]):
    x = 900 + (i % 3) * 270
    y = 20 + (i // 3) * 24
    edge(None, None, color=col, dashed=dsh, spt=(x, y + 8), tpt=(x + 44, y + 8), width=wd)
    box(x + 52, y, 215, 16, txt, TEXT.replace('fontSize=12', 'fontSize=11'))

# ---------- external (left) ----------
# Robot A — what actually runs on the TurtleBot4 (turtlebot4_bringup standard.launch.py on the Pi + Create 3 firmware)
ROBOT = box(30, 105, 280, 452, '<b>로봇 A · TurtleBot4</b>  <span style="font-weight:normal;font-size:11px">(/robot_a)</span>',
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
REP = box(48, 240, 244, 40, '<b>create3_republisher</b><br>Create 3 토픽·액션을 /robot_a/… 로 중계', RN())
box(48, 286, 244, 32, 'turtlebot4_node · base_node  <span style="color:#777">버튼 · 화면 · LED</span>', RN('#AAAAAA', '#FAFAFA'))
OAK = box(48, 324, 244, 66, '<b>oakd</b> (depthai_ros_driver)<br>카메라 드라이버 · 이미지를 <b>계속</b> 발행<br>/oakd/rgb/preview/image_raw', RN())
C1 = box(48, 422, 244, 38, '<b>바퀴 구동 · 주행거리</b><br>/cmd_vel 구독 → /odom · TF odom→base_link', RN())
C2 = box(48, 466, 244, 38, '<b>도킹</b><br>/dock · /undock 액션 서버 · /dock_status', RN())
C3 = box(48, 510, 244, 32, '<b>배터리 · 안전 센서</b>  /battery_state · /hazard_detection', RN())
MON = box(40, 572, 268, 150, '<b style="font-size:13px">System Monitor</b> <span style="font-size:10px">(모니터링팀)</span><br><span style="font-size:9.5px;color:#C0392B">구독하는 로봇 A 토픽 (6개)</span><span style="font-size:9px"><br><b>/robot_a/status</b> <span style="color:#666">String(JSON) · 주행·작업 상태</span><br><b>/robot_a/battery_state</b> <span style="color:#666">BatteryState · 배터리</span><br><b>/robot_a/current_zone</b> <span style="color:#666">String · 현재 탐색 구역</span><br><b>/robot_a/detection_image</b> <span style="color:#666">CompressedImage · 사진 352×352</span><br><b>/robot_a/zone_result</b> <span style="color:#666">String(JSON) · 구역 이력·진행률</span><br><b>/robot_a/amcl_pose</b> <span style="color:#666">PoseWithCovarianceStamped (amcl)</span></span><br><span style="font-size:8.5px;color:#666">숙과·미숙과·병충해 수는 서버 비전팀 · 공통 지도는 제외</span>', S(rounded=0, whiteSpace='wrap', html=1, fillColor='#F4F4F4', strokeColor=INK, strokeWidth=2, fontSize=9, fontColor='#1A1A1A', align='left', verticalAlign='middle', spacingLeft=6))
DET = box(40, 1505, 220, 70, t('Detect', '비전 인식 팀 (YOLO)', sub=11), EXT)
SM = box(40, 850, 220, 620, t('SERVER', '', '작업 지시', '결과 저장', '재방문 목록', '(remission_list)', 'B 작업 상태', sub=11), EXT)
edge(SM, MON, '전달', color=RED, dashed=True, ex=0.5, ey=0, nx=round((150 - 40) / 268, 4), ny=1, font=10)

# ---------- PC ----------
box(360, 80, 1320, 1780, 'PC  (원격 PC · ROS 2 Jazzy)',
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
DOCKS = box(425, 640, 190, 92, t('docking_server', '(opennav_docking) Nav2 도킹 액션', 'dock_robot · undock_robot', 'nav2.launch.py로 함께 실행됨',
                                 '<span style="color:#B5481C">도크 위치 미설정 → Create 3 /dock 사용</span>'), COL)
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

# Our logic — ① 탐색 (patrol) and ② 재탐색 (re-patrol) from the team's hand-drawn flowcharts; each step is tagged with what it talks to
LOGIC = box(400, 800, 1240, 1030, '우리의 로직  <span style="font-weight:normal;font-size:12px">Robot A 미션 흐름 · ① 탐색 → ② 재탐색</span>',
            group(OUR_C, OUR_F, align='right').replace('verticalAlign=top', 'verticalAlign=bottom').replace('spacingTop=4', 'spacingBottom=6'))
G_, R_, B_, K_ = NAV_C, RED, BLUE, '#666666'
def tg(txt, col): return f'<br><span style="font-size:9.5px;color:{col}">{txt}</span>'
def st(x, y, w, h, title, *tags, col=OUR_C, fill='#FFFFFF'):
    return box(x, y, w, h, f'<b>{title}</b>' + ''.join(tg(a_, c_) for a_, c_ in tags),
               S(rounded=1, whiteSpace='wrap', html=1, fillColor=fill, strokeColor=col, strokeWidth=1.5, fontSize=11, fontColor='#1A1A1A', arcSize=12))
def dc(x, y, w, h, title, *tags):
    return box(x, y, w, h, title + ''.join(tg(a_, c_) for a_, c_ in tags),
               'rhombus;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=OUR_C, strokeWidth=1.5, fontSize=10.5, fontColor='#1A1A1A'))
def cc(x, y, txt):
    return box(x, y, 30, 30, f'<b>{txt}</b>', 'ellipse;' + S(whiteSpace='wrap', html=1, fillColor='#EDE7F6', strokeColor=OUR_C, strokeWidth=1.3, fontSize=12, fontColor=OUR_C))
def lb(x, y, w, txt, size=12, col=OUR_C):
    return box(x, y, w, 18, txt, TEXT.replace('fontSize=12', f'fontSize={size}') + f'fontColor={col};')
def go(a_, b_, label='', **kw):
    kw.setdefault('width', 1.4); kw.setdefault('font', 9.5)
    return edge(a_, b_, label=label, color=kw.pop('color', '#444444'), **kw)

# ---------- ① 탐색 ----------
lb(430, 806, 400, '<b>① 탐색</b>  <span style="font-size:11px;color:#666">순찰 명령 · 섹터 A1 → A4</span>', size=13)
P0 = st(430, 845, 140, 50, '명령 확인', ('← /robot_a/mission_cmd', R_))
P1 = dc(596, 832, 160, 76, '<b>docking?</b>', ('/robot_a/dock_status', R_))
P2 = st(780, 845, 140, 50, 'undock', ('→ /robot_a/undock', B_))
P3 = st(960, 845, 140, 50, '순찰 실행', ('섹터 좌표 목록', K_), col='#C0392B')
P4 = st(430, 965, 150, 50, '순찰 좌표로 이동', ('→ Nav2: goal', G_))
P5 = dc(600, 948, 170, 84, 'Nav2 결과<br><b>SUCCEEDED?</b>', ('goal checker 판정', G_))
P6 = st(785, 956, 160, 68, '정지 후 사진 캡처', ('← Bot: 카메라 → 352×352', R_), ('↺ recapture_request 오면 재촬영', R_))
P7 = st(975, 955, 190, 70, '이미지 · 위치 · 섹터 · 시각<br>서버에 전송 (352×352)', ('→ /robot_a/detection_image', B_), ('→ /robot_a/capture_info', B_))
P8 = dc(1185, 950, 170, 80, '배터리<br>20% 이하?', ('/robot_a/battery_state', R_))
P9 = st(1380, 960, 200, 60, '작업 저장 후 복귀 (도킹)', ('작업 위치 저장', K_), ('→ Nav2 · /robot_a/dock', B_))
P12 = dc(615, 1060, 140, 70, '재탐색<br>3회 초과?')
P10 = dc(1200, 1060, 140, 70, '섹터 모두<br>방문?')
P13 = dc(615, 1160, 140, 70, '현재 위치<br>A1?')
P14 = st(430, 1170, 150, 50, '도킹 위치로 이동', ('(0, 0, 0) · → Nav2', G_))
P15 = st(790, 1170, 150, 50, '이전 좌표로 이동', ('→ Nav2: goal', G_))
P11 = st(1195, 1165, 150, 56, 'docking으로 이동', ('→ Nav2 · /robot_a/dock', B_))
C2a = cc(1370, 1178, '②'); lb(1405, 1184, 200, '재순찰 명령 실행', size=11)
CA1 = cc(1465, 1040, 'A'); lb(1500, 1046, 130, '충전 후 이전 좌표로', size=9.5, col='#666')
CA2 = cc(955, 1180, 'A')
CB1 = cc(1465, 915, 'B'); lb(1500, 921, 130, '② 재탐색에서 복귀', size=9.5, col='#666')

go(P0, P1); go(P1, P2, 'yes', lx=-0.3); go(P2, P3)
go(P1, P3, 'no', ex=0.5, ey=0, nx=0.5, ny=0, points=((675, 822), (1030, 822)), lx=-0.85)
go(P3, P4, ex=0.5, ey=1, nx=0.5, ny=0, points=((1030, 928), (505, 928)))
go(P4, P5); go(P5, P6, 'yes', lx=-0.3); go(P6, P7); go(P7, P8); go(P8, P9, 'yes', lx=-0.3)
go(P5, P12, 'no', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(P12, P4, 'no', ex=0, ey=0.5, nx=round((545 - 430) / 150, 4), ny=1, points=((545, 1095),), lx=-0.5)
go(P12, P13, 'yes', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(P13, P14, 'yes', lx=-0.2)
go(P14, P4, ex=round((480 - 430) / 150, 4), ey=0, nx=round((480 - 430) / 150, 4), ny=1)
go(P13, P15, 'no', lx=-0.2)
go(P15, P4, ex=0.5, ey=1, nx=0, ny=0.5, points=((865, 1260), (415, 1260), (415, 990)))
go(P8, P10, 'no', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(P10, P4, 'no · 다음 섹터', ex=1, ey=0.5, nx=0, ny=0.5, points=((1600, 1095), (1600, 1260), (415, 1260), (415, 990)), lx=-0.78)
go(P10, P11, 'yes', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(P11, C2a)
go(P9, CA1, ex=round((1480 - 1380) / 200, 4), ey=1, nx=0.5, ny=0)
go(CA2, P15, ex=0, ey=0.5, nx=1, ny=0.5)
go(CB1, P9, ex=0.5, ey=1, nx=0.5, ny=0)

# ---------- ② 재탐색 ----------
edge(None, None, color='#B9A9D9', dashed=True, end='none', width=1.2, spt=(410, 1288), tpt=(1630, 1288))
lb(520, 1300, 520, '<b>② 재탐색</b>  <span style="font-size:11px;color:#666">재순찰 명령 실행 · SERVER가 보낸 B 순찰 구역</span>', size=13)
C2b = cc(485, 1300, '②')
R0 = dc(420, 1352, 170, 76, '받은 데이터 있음?', ('← /robot_a/remission_list', R_))
R2 = st(600, 1365, 170, 50, 'remission_list에<br>재순찰 구역 저장')
R3 = st(800, 1365, 150, 50, '순찰 좌표로 이동', ('→ Nav2: goal', G_))
R4 = dc(970, 1348, 160, 84, 'Nav2 결과<br><b>SUCCEEDED?</b>', ('goal checker 판정', G_))
R5 = st(1145, 1352, 175, 76, '정지 후 사진 캡처', ('← Bot: 카메라 → 352×352', R_), ('↺ recapture_request 오면 재촬영', R_), ('list에서 방문 위치 업데이트', K_))
R6 = st(1345, 1352, 210, 76, '이미지 · 위치 · 섹터 · 시각<br>서버에 전송 (352×352)', ('→ detection_image · capture_info', B_), ('mode = recheck', B_))
R1 = st(430, 1470, 150, 50, 'docking station<br>이동 · 대기', ('→ Nav2 · /robot_a/dock', B_))
R11 = dc(985, 1460, 130, 70, '재탐색<br>3회 초과?')
R7 = dc(1365, 1455, 170, 80, '배터리<br>20% 이하?', ('/robot_a/battery_state', R_))
CB2 = cc(1550, 1480, 'B')
R13 = st(800, 1580, 150, 50, '전 위치로 이동', ('→ Nav2: goal', G_))
R12 = dc(985, 1570, 130, 70, '현 위치<br>A1?')
R8 = dc(1380, 1570, 140, 70, 'remission_list에<br>남은 좌표?')
R10 = dc(1180, 1680, 140, 70, '리스트에<br>좌표 있음?')
R9 = st(1370, 1690, 170, 50, '30초 동안<br>자리에서 수신 대기', ('← /robot_a/remission_list', R_))
PUBN = box(1170, 1755, 300, 42, '<b>토픽 발행 시점 (안)</b><br>status: 상태 바뀔 때 · current_zone: 섹터 이동 시작<br>detection_image·capture_info·zone_result: 사진 촬영 후', node('#1F5FD6', '#EEF3FC', fs=9))
SAFE = box(430, 1765, 720, 40, '<b>상시 감시 (전 과정)</b>  비상정지 → 즉시 정지 · 통신 3초 끊김 → 정지 · 배터리는 흐름 안에서 확인',
           node('#B58A00', '#FFFBEA', fs=11))

go(C2b, R0, ex=0.5, ey=1, nx=0.5, ny=0)
go(R0, R2, 'yes', lx=-0.3); go(R2, R3); go(R3, R4); go(R4, R5, 'yes', lx=-0.3); go(R5, R6)
go(R0, R1, 'no', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(R1, R0, '데이터 확인', ex=0, ey=0.5, nx=0, ny=0.5, points=((415, 1495), (415, 1390)), lx=0.0, loff=(-2, 0))
go(R6, R7, ex=round((1450 - 1345) / 210, 4), ey=1, nx=0.5, ny=0)
go(R7, CB2, 'yes', ex=1, ey=0.5, nx=0, ny=0.5, lx=-0.2)
go(R7, R8, 'no', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(R8, R3, 'yes', ex=1, ey=0.5, nx=0.5, ny=0, points=((1600, 1605), (1600, 1340), (875, 1340)), lx=-0.9)
go(R8, R9, 'no', ex=0.5, ey=1, nx=round((1450 - 1370) / 170, 4), ny=0, lx=-0.3)
go(R9, R10)
go(R10, R8, 'yes', ex=0.5, ey=0, nx=1, ny=0.5, points=((1250, 1550), (1600, 1550), (1600, 1605)), lx=-0.8)
go(R10, R1, 'no', ex=0, ey=0.5, nx=round((470 - 430) / 150, 4), ny=1, points=((470, 1715),), lx=-0.3)
go(R4, R11, 'no', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(R11, R3, 'no', ex=0, ey=0.5, nx=round((915 - 800) / 150, 4), ny=1, points=((915, 1495),), lx=-0.4)
go(R11, R12, 'yes', ex=0.5, ey=1, nx=0.5, ny=0, lx=-0.3)
go(R12, R13, 'no', lx=-0.2)
go(R13, R3, ex=round((850 - 800) / 150, 4), ey=0, nx=round((850 - 800) / 150, 4), ny=1)
go(R12, R1, 'yes', ex=0.5, ey=1, nx=round((530 - 430) / 150, 4), ny=1, points=((1050, 1660), (530, 1660)), lx=-0.3)

# logic → Nav2: every '→ Nav2' step sends a NavigateToPose goal to bt_navigator
edge(None, BT, '→ Nav2 단계마다 goal ↔ result · /robot_a/navigate_to_pose<br>(nav2_msgs/NavigateToPose · 순찰 좌표 · 이전 좌표 · 도킹 위치)', color=NAV_C, width=2.5, font=11, both=True,
     nx=round((1350 - 1265) / 170, 4), ny=1, spt=(1350, 800), loff=(0, 0))

# localization internals & interplay
edge(MAP, AMCL, color=INK, ex=0, ey=0.375, nx=1, ny=0.375, width=1.5)
edge(RVIZ, AMCL, label='/robot_a/initialpose', color=INK, ex=0, ey=round((165 - 140) / 70, 4), nx=0.5, ny=0,
     points=((530, 165),), width=1.5, lx=0.3)
edge(LOC, NAV, label='/map → global costmap<br>TF map→odom (로봇 위치)', color=INK, ex=round((780 - 400) / 600, 4), ey=1,
     nx=round((780 - 400) / 1240, 4), ny=0, width=2.5, font=11, loff=(95, 0))

# Robot nodes <-> Localization / Nav2
ry = lambda node_y, h, y: round((y - node_y) / h, 4)
edge(RSP, LOC, '/robot_a/tf_static', color=RED, ex=1, ey=ry(150, 38, 169), nx=0, ny=round((169 - 120) / 210, 4), lx=0.1, loff=(0, -9), font=10)
edge(LID, AMCL, '/robot_a/scan', color=RED, ex=1, ey=ry(194, 40, 205), nx=0, ny=round((205 - 185) / 80, 4), lx=0.1, loff=(0, -9), font=10)
edge(LID, NAV, '/robot_a/scan (costmap · collision_monitor)', color=RED, ex=1, ey=ry(194, 40, 224), nx=round((410 - 400) / 1240, 4), ny=0,
     points=((410, 224),), lx=0.7, loff=(95, 0), font=10)
edge(C1, NAV, '/robot_a/odom · TF odom→base_link', color=RED, ex=1, ey=ry(422, 38, 434), nx=0, ny=round((434 - 380) / 380, 4), lx=0.1, loff=(0, -9), font=10)
edge(COLL, C1, '/robot_a/cmd_vel', color=BLUE, ex=0, ey=0.5, nx=1, ny=ry(422, 38, 452), points=((408, 585), (408, 452)), lx=0.75, loff=(0, 9), width=2.5, font=11)

# Robot nodes <-> logic (group level; each step's tag says which one it uses)
edge(OAK, LOGIC, '/robot_a/oakd/rgb/preview/image_raw (sensor_msgs/Image)', color=RED, ex=1, ey=ry(324, 66, 386), nx=round((880 - 400) / 1240, 4), ny=0,
     points=((394, 386), (394, 764), (880, 764)), lx=0.3, loff=(0, -9), font=10)
edge(C2, LOGIC, '/robot_a/undock · dock · dock_status (irobot_create_msgs)', color=BLUE, both=True, ex=1, ey=ry(466, 38, 485), nx=round((760 - 400) / 1240, 4), ny=0,
     points=((382, 485), (382, 773), (760, 773)), lx=0.35, loff=(0, 9), font=10)
edge(C3, LOGIC, '/robot_a/battery_state (sensor_msgs/BatteryState)', color=RED, ex=1, ey=ry(510, 32, 526), nx=round((640 - 400) / 1240, 4), ny=0,
     points=((370, 526), (370, 790), (640, 790)), lx=0.55, loff=(0, 9), font=10)

# SERVER <-> logic (group level, dashed)
sy = lambda y: round((y - 850) / 620, 4)
SMD = dict(dashed=True, font=10)
edge(SM, LOGIC, '/robot_a/mission_cmd<br>/robot_a/remission_list<br>/robot_a/recapture_request', color=RED, dashed=True, ex=1, ey=sy(880), nx=0, ny=round((880 - 800) / 1030, 4),
     lx=0, loff=(0, -30), font=10)
edge(LOGIC, SM, '/robot_a/detection_image<br>(352×352)<br>/robot_a/capture_info', color=BLUE, dashed=True, ex=0, ey=round((1010 - 800) / 1030, 4), nx=1, ny=sy(1010),
     lx=0, loff=(0, 30), font=10)

# Robot A topics → System Monitor (monitoring team subscribes directly)
PCB = [l for l in cells if 'PC  (원격 PC' in l][0].split('id="')[1].split('"')[0]
edge(PCB, MON, '토픽<br>발행', color=BLUE, ex=0, ey=round((700 - 80) / 1780, 4), nx=1, ny=round((700 - 572) / 150, 4), font=9.5, lx=0, loff=(0, 0))
edge(C3, MON, '', color=BLUE, ex=0.18, ey=1, nx=round((92 - 40) / 268, 4), ny=0, font=9.5, loff=(-2, 0))

# SM <-> Detect
edge(SM, DET, 'image', color=BLUE, ex=0.3, ey=1, nx=0.3, ny=0, loff=(-24, 0), **SMD)
edge(DET, SM, '탐지 결과 → DB', color=RED, ex=0.7, ey=0, nx=0.7, ny=1, loff=(46, 0), **SMD)

xml = ('<mxfile host="app.diagrams.net"><diagram id="robotA-arch" name="로봇 A 시스템 설계도">'
       '<mxGraphModel dx="1720" dy="1900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
       'fold="1" page="1" pageScale="1" pageWidth="1720" pageHeight="1900" math="0" shadow="0"><root>'
       '<mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1], 'w', encoding='utf-8').write(xml)
print('cells', len(cells))
