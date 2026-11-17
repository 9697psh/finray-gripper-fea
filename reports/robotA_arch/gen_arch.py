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
DET = box(40, 930, 260, 110, t('Detect', '비전 인식 팀 (YOLO)', sub=11), EXT)
SM = box(40, 1060, 260, 110, t('SM', 'Main PC 서버 · DB', sub=11), EXT)

# ---------- PC ----------
box(360, 80, 1320, 1130, 'PC  (원격 PC · ROS 2 Jazzy)',
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

# Our logic
box(400, 800, 1240, 390, '우리의 로직  <span style="font-weight:normal;font-size:12px">(Robot A 패키지 · 노드 이름은 제안, 팀에서 확정)</span>',
    group(OUR_C, OUR_F))
OC = node(OUR_C)
DOCKC = box(425, 840, 190, 60, t('dock_client', 'Dock · Undock action client'), OC)
VIS = box(425, 920, 190, 100, t('vision_bridge', 'OAK-D 이미지 받아', '사진 토픽 발행', '탐지 결과 구독'), OC)
SRV = box(425, 1070, 190, 90, t('server_bridge', '작업 시작 · 재방문 좌표 수신', 'a_mission · a_remission 발행'), OC)
MIS = box(720, 840, 380, 330, t('robot_a_mission  (상태 머신)', '',
                                 '① 작업 시작 수신 → 도킹 중이면 언도킹',
                                 '② 섹터 i 좌표로 이동 (nav2, i = 1→4)',
                                 '③ 도착 → 정지 → OAK-D 촬영',
                                 '④ 사진 전송 → 탐지 결과 받기 → 서버 보고',
                                 '⑤ 마지막 섹터면 재방문 목록 받기',
                                 '⑥ 재방문 좌표 순회 (③~④ 반복)',
                                 '⑦ 끝나면 도킹 스테이션 복귀', sub=12),
          node(OUR_C, '#FFFFFF', align='left', fs=14))
NAVC = box(1250, 840, 200, 90, t('nav_goal_client', 'NavigateToPose', 'action client', 'goal = 섹터 좌표 i'), OC)

edge(MIS, NAVC, label='섹터 좌표 i', color=INK, ex=1, ey=round((885 - 840) / 330, 4), nx=0, ny=0.5, width=1.5)
edge(MIS, DOCKC, label='언도킹·도킹', color=INK, ex=0, ey=round((870 - 840) / 330, 4), nx=1, ny=0.5, width=1.5)
edge(MIS, VIS, label='촬영 요청<br>탐지 결과', color=INK, both=True, ex=0, ey=round((970 - 840) / 330, 4), nx=1, ny=0.5, width=1.5)
edge(SRV, MIS, label='시작·재방문<br>결과 보고', color=INK, both=True, ex=1, ey=0.5, nx=0, ny=round((1115 - 840) / 330, 4), width=1.5)

# logic -> nav2 (goal)
edge(NAVC, BT, label='goal (action client msg)<br>← feedback · result', color=INK, ex=0.5, ey=0, nx=0.5, ny=1, width=2.5,
     font=11)
edge(NAVC, WPF, label='또는 follow_waypoints<br>(섹터 1~4 한 번에)', color=GREY, dashed=True, ex=1, ey=0.5, nx=0.5, ny=1,
     points=((1550, 885),), width=1.5)
edge(DOCKC, DOCKS, label='Nav2 도킹을 쓸 경우', color=GREY, dashed=True, ex=0.5, ey=0, nx=0.5, ny=1, width=1.5, lx=0.6)

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
edge(DOCKC, BOT, label='/dock · /undock', color=BLUE, ex=0, ey=0.5, nx=1, ny=round((420 - 160) / 300, 4),
     points=((345, 870), (345, 420)), lx=-0.86, loff=(0, -10))
edge(BOT, VIS, label='OAK-D 이미지', color=RED, ex=1, ey=round((440 - 160) / 300, 4), nx=0, ny=0.15,
     points=((325, 440), (325, 935)), lx=0.84, loff=(0, -10))

# Detect / SM
edge(DET, VIS, label='탐지 결과', color=RED, ex=1, ey=round((975 - 930) / 110, 4), nx=0, ny=0.55, loff=(0, -10))
edge(VIS, DET, label='사진 토픽', color=BLUE, ex=0, ey=0.85, nx=1, ny=round((1005 - 930) / 110, 4), loff=(0, 10))
edge(SM, SRV, label='작업 시작<br>재방문 좌표', color=RED, ex=1, ey=round((1100 - 1060) / 110, 4), nx=0,
     ny=round((1100 - 1070) / 90, 4), loff=(0, -17))
edge(SRV, SM, label='a_mission<br>a_remission', color=BLUE, ex=0, ey=round((1130 - 1070) / 90, 4), nx=1,
     ny=round((1130 - 1060) / 110, 4), loff=(0, 17))

xml = ('<mxfile host="app.diagrams.net"><diagram id="robotA-arch" name="로봇 A 시스템 설계도">'
       '<mxGraphModel dx="1720" dy="1240" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
       'fold="1" page="1" pageScale="1" pageWidth="1720" pageHeight="1240" math="0" shadow="0"><root>'
       '<mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1], 'w', encoding='utf-8').write(xml)
print('cells', len(cells))
