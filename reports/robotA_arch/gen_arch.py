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
         lx=0, loff=(0, 0), both=False, width=2, font=10, end='block', spt=None, tpt=None):
    st = dict(edgeStyle='orthogonalEdgeStyle', rounded=0, html=1, endArrow=end, endFill=1, strokeColor=color,
              strokeWidth=width, fontSize=font, fontColor=color if color != GREY else '#666666',
              labelBackgroundColor='#FFFFFF', jumpStyle='arc', jumpSize=8)
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
lx0 = 1110
for i, (col, dsh, txt) in enumerate([(RED, False, '외부 → PC (입력)'), (BLUE, False, 'PC → 외부 (출력)'),
                                     (INK, False, 'PC 내부'), (GREY, True, '선택 · 미사용')]):
    x = lx0 + (i % 2) * 290
    y = 22 + (i // 2) * 24
    edge(None, None, color=col, dashed=dsh, spt=(x, y + 8), tpt=(x + 46, y + 8), width=2)
    box(x + 54, y, 220, 16, txt, TEXT.replace('fontSize=12', 'fontSize=11'))

# ---------- external (left) ----------
BOT = box(40, 160, 260, 300, t('Bot', 'TurtleBot4 (/robot&lt;n&gt;)', '', 'Create3 베이스', '/odom · /tf · 배터리',
                                '/dock · /undock (action)', '', 'RPLIDAR → /scan', '',
                                'OAK-D → /oakd/rgb/preview/image_raw', sub=11), EXT)
DET = box(40, 1060, 220, 100, t('Detect', '비전 인식 팀 (YOLO)', 'image 구독 → 익음·병충해 탐지', sub=11), EXT)
SM = box(40, 880, 220, 120, t('SM', 'Main PC 서버 · DB', '작업 지시 · 결과 저장', '재방문 목록(remission_list)', sub=11), EXT)

# ---------- PC ----------
box(360, 80, 1320, 1365, 'PC  (원격 PC · ROS 2 Jazzy)',
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

# Our logic — Robot A mission flow (user's flowchart), described in plain steps
LOGIC = box(400, 800, 1240, 625, '우리의 로직  <span style="font-weight:normal;font-size:12px">Robot A 미션 흐름 (2번 플로우차트)</span>',
            group(OUR_C, OUR_F))
def tag(txt, col):
    return f'<br><span style="font-size:10px;color:{col}">{txt}</span>'
def step(x, y, w, h, title, *tags, dashed=False):
    st = node('#E08A00' if dashed else OUR_C, '#FFF8EC' if dashed else '#FFFFFF', dashed=dashed, fs=12)
    return box(x, y, w, h, f'<b>{title}</b>' + ''.join(tag(tx, c) for tx, c in tags), st)
def dec(x, y, w, h, title):
    return box(x, y, w, h, f'<b>{title}</b>', 'rhombus;' + S(whiteSpace='wrap', html=1, fillColor='#FFFFFF', strokeColor=OUR_C,
                                                            strokeWidth=1.5, fontSize=11, fontColor='#1A1A1A'))
def lab(x, y, w, txt, col=OUR_C):
    box(x, y, w, 18, f'<b>{txt}</b>', TEXT.replace('fontSize=12', 'fontSize=12') + f'fontColor={col};')
def go(a, b, label='', **kw):
    kw.setdefault('width', 1.5)
    return edge(a, b, label=label, color=kw.pop('color', INK), **kw)

NAVT = ('→ Nav2: goal (NavigateToPose)', NAV_C)
# row 0: start
S0 = step(440, 850, 170, 56, '작업 시작 수신', ('← SM: 작업 시작', RED))
D0 = dec(650, 846, 120, 64, '도킹 중?')
U0 = step(810, 850, 190, 56, '언도킹', ('→ Bot: /undock', BLUE), ('흐름도에 추가 필요', '#B86E00'), dashed=True)
N0 = step(1060, 850, 200, 56, '도킹 (no일 때)', ('→ Bot: /dock', BLUE), ('의도 확인 필요', '#B86E00'), dashed=True)
go(S0, D0)
go(D0, U0, 'yes', lx=-0.4)
go(D0, N0, 'no', ex=0.5, ey=0, nx=0.5, ny=0, points=((710, 836), (1160, 836)), lx=-0.85)

# row 1: patrol sectors 1..4
lab(960, 937, 360, '탐색 단계 · 섹터 i = 1 → 4')
A1 = step(440, 985, 170, 60, '섹터 i 좌표로 이동', NAVT)
A2 = dec(645, 980, 115, 70, '이동 완료?')
A3 = step(795, 990, 95, 50, 'TB4 정지')
A4 = step(925, 985, 150, 60, 'OAK-D 촬영', ('← Bot: 카메라 이미지', RED))
A5 = step(1110, 980, 200, 70, '토마토 확인 후 서버 전송', ('→ SM: a_mission · 좌표 · image', BLUE))
A6 = dec(1345, 975, 120, 80, 'i = 마지막<br>섹터?')
B1 = step(1495, 980, 125, 70, '재방문 좌표 받기', ('← SM: remission_list', RED), ('(DB 좌표 저장)', '#666'))
go(U0, A1, ex=0.5, ey=1, nx=0.5, ny=0, points=((905, 930), (525, 930)))
go(A1, A2)
go(A2, A3, 'yes', lx=-0.3)
go(A2, A1, 'no (재시도)', ex=0.5, ey=1, nx=0.5, ny=1, points=((702, 1075), (525, 1075)))
go(A3, A4); go(A4, A5); go(A5, A6)
go(A6, A1, 'no · i = i + 1', ex=0.5, ey=0, nx=0.25, ny=0, points=((1405, 962), (482, 962)), lx=-0.2)
go(A6, B1, 'yes', lx=-0.2)

# row 2: revisit (right -> left)
lab(1300, 1100, 320, '재방문 단계 · remission_list 좌표')
B2 = step(1480, 1130, 140, 60, '받은 좌표로 이동', NAVT)
B3 = dec(1330, 1125, 115, 70, '이동 완료?')
B4 = step(1200, 1135, 95, 50, 'TB4 정지')
B5 = step(1040, 1130, 125, 60, 'OAK-D 촬영', ('← Bot: 카메라 이미지', RED))
B6 = step(830, 1125, 175, 70, '결과 서버 전송', ('→ SM: a_remission · 좌표 · image', BLUE))
B7 = dec(670, 1120, 125, 80, 'list에<br>남은 좌표?')
B8 = step(830, 1230, 175, 44, '방문한 좌표 remove')
E0 = step(430, 1130, 205, 60, '전 작업 완료 → 도킹 스테이션', ('→ Nav2 이동 · Bot /dock → 재대기', BLUE))
go(B1, B2)
go(B2, B3); go(B3, B4, 'yes', lx=-0.3); go(B4, B5); go(B5, B6); go(B6, B7)
go(B3, B2, 'no (재시도)', ex=0.5, ey=1, nx=0.25, ny=1, points=((1387, 1212), (1515, 1212)), lx=-0.1)
go(B7, B8, 'yes', ex=0.5, ey=1, nx=0, ny=0.5, points=((732, 1252),), lx=-0.5)
go(B8, B2, ex=1, ey=0.5, nx=0.75, ny=1, points=((1585, 1252),))
go(B7, E0, 'no', lx=-0.2)

# notes: what the flowchart still needs
box(430, 1300, 1190, 105,
    '<b>흐름도에 더하면 좋은 것</b><br>'
    '① 도킹 중이면 nav2 전에 <b>언도킹</b>이 있어야 합니다 (도킹 상태로는 주행 안 됨). "no → docking" 갈래는 의도를 정해 주세요.<br>'
    '② "이동 완료? no → 재시도"는 무한 반복될 수 있습니다. nav2 결과(성공·실패·취소)로 판단하고, 예: 3회 실패하면 그 섹터를 건너뛰고 서버에 기록.<br>'
    '③ 재방문 목록은 언제 오는지 정해야 합니다 (기다리는 시간 제한, 목록이 비어 있으면 바로 도킹 복귀). remove는 로봇·DB 중 누가 지우는지도 정하기.<br>'
    '④ 탐색 단계와 재방문 단계는 같은 동작(이동 → 정지 → 촬영 → 전송)이라 코드는 하나로 만들고 보내는 토픽(a_mission · a_remission)만 바꾸면 됩니다.<br>'
    '⑤ 전체 과정 동안 배터리 · 비상정지 · 통신 끊김(3초)을 따로 감시하기.',
    S(rounded=1, whiteSpace='wrap', html=1, fillColor='#FFFBEA', strokeColor='#E0B800', strokeWidth=1.2, fontSize=11,
      fontColor='#333333', align='left', verticalAlign='top', spacingLeft=12, spacingTop=6, arcSize=6))

# logic -> nav2 (goal)
edge(None, BT, label='이동 단계마다 goal (action client msg)<br>← feedback · result', color=INK, nx=0.5, ny=1,
     spt=(1350, 800), width=2.5, font=11)

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
edge(BOT, NAV, label='/scan · /odom · /tf', color=RED, ex=1, ey=round((400 - 160) / 300, 4), nx=0,
     ny=round((400 - 380) / 380, 4), loff=(0, -10))
edge(LOGIC, BOT, label='/undock · /dock', color=BLUE, ex=0, ey=round((830 - 800) / 625, 4), nx=1,
     ny=round((420 - 160) / 300, 4), points=((345, 830), (345, 420)), lx=0.02, loff=(-85, -40))
edge(BOT, LOGIC, label='카메라 이미지', color=RED, ex=1, ey=round((440 - 160) / 300, 4), nx=0, ny=round((850 - 800) / 625, 4),
     points=((325, 440), (325, 850)), lx=-0.1, loff=(-75, 40))

# SM / Detect
edge(SM, LOGIC, label='작업 시작<br>remission_list', color=RED, ex=1, ey=round((905 - 880) / 120, 4), nx=0,
     ny=round((905 - 800) / 625, 4), loff=(0, -17))
edge(LOGIC, SM, label='a_mission · a_remission<br>(좌표 · image)', color=BLUE, ex=0, ey=round((975 - 800) / 625, 4), nx=1,
     ny=round((975 - 880) / 120, 4), loff=(0, 17))
edge(LOGIC, DET, label='image topic', color=BLUE, ex=0, ey=round((1100 - 800) / 625, 4), nx=1,
     ny=round((1100 - 1060) / 100, 4), loff=(0, -10))
edge(DET, SM, label='탐지 결과 → DB', color=INK, ex=0.5, ey=0, nx=0.5, ny=1, width=1.5)

xml = ('<mxfile host="app.diagrams.net"><diagram id="robotA-arch" name="로봇 A 시스템 설계도">'
       '<mxGraphModel dx="1720" dy="1480" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
       'fold="1" page="1" pageScale="1" pageWidth="1720" pageHeight="1480" math="0" shadow="0"><root>'
       '<mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1], 'w', encoding='utf-8').write(xml)
print('cells', len(cells))
