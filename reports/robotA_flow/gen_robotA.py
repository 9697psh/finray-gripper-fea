"""Generate the Robot A flowchart as a draw.io file, using the same visual language
(styles, panel layout, legend) as the team's Robot B draw.io file.
Usage: python3 gen_robotA.py OUT.drawio"""
import sys
from xml.sax.saxutils import escape

# ---------- styles copied from the Robot B file ----------
ST = {
    'panel': 'rounded=0;html=1;fillColor=#FFFFFF;strokeColor=#D0D0D0;',
    'head': 'rounded=0;html=1;fillColor=#F6F7F9;strokeColor=#D0D0D0;',
    'title': 'text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=20;',
    'subtitle': 'text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=12;fontColor=#555555;verticalAlign=top;',
    'rel': 'text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;align=right;fontSize=11;fontColor=#888888;',
    'term': 'rounded=1;arcSize=50;fontColor=#FFFFFF;whiteSpace=wrap;html=1;fillColor=#2B2B2B;strokeColor=#2B2B2B;strokeWidth=1.5;fontSize=13;',
    'proc': 'rounded=0;whiteSpace=wrap;html=1;fillColor=#EAF1FD;strokeColor=#3B6FD8;strokeWidth=1.5;fontSize=13;',
    'dec': 'rhombus;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#E08A1E;strokeWidth=1.5;fontSize=12;',
    'io': 'shape=parallelogram;perimeter=parallelogramPerimeter;fixedSize=1;size=16;whiteSpace=wrap;html=1;fillColor=#E6F6EC;strokeColor=#2F9E5B;strokeWidth=1.5;fontSize=13;',
    'sub': 'shape=process;backgroundOutline=1;size=12;fixedSize=1;whiteSpace=wrap;html=1;fillColor=#F1EAFD;strokeColor=#7C4DCC;strokeWidth=1.5;fontSize=13;',
    'db': 'shape=cylinder3;boundedLbl=1;backgroundOutline=1;size=8;whiteSpace=wrap;html=1;fillColor=#EFEFEF;strokeColor=#666666;strokeWidth=1.5;fontSize=13;',
    'off': 'shape=offPageConnector;size=14;fixedSize=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2B2B2B;strokeWidth=1.5;fontSize=13;verticalAlign=top;spacingTop=8;',
    'note': 'shape=partialRectangle;whiteSpace=wrap;html=1;top=0;bottom=0;right=0;fillColor=none;strokeColor=#888888;strokeWidth=1.5;align=left;spacingLeft=8;fontSize=12;fontColor=#555555;',
    'scope': 'rounded=0;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#D0D0D0;align=left;verticalAlign=top;spacingLeft=12;spacingTop=8;fontSize=12;fontColor=#333333;',
    'legtxt': 'text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=12;fontColor=#333333;',
    'leghead': 'text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=14;',
}
EDGE = ('edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#3A3A3A;strokeWidth=1.5;endArrow=block;'
        'endFill=1;endSize=6;exitX={ex};exitY={ey};exitDx=0;exitDy=0;entryX={nx};entryY={ny};entryDx=0;entryDy=0;'
        'fontSize=12;fontColor=#B5470F;fontStyle=1;labelBackgroundColor=#FFFFFF;')
DASH = 'endArrow=none;html=1;dashed=1;strokeColor=#888888;strokeWidth=1;'
SIDE = {'t': (0.5, 0), 'b': (0.5, 1), 'l': (0, 0.5), 'r': (1, 0.5)}
SIZE = {'term': (200, 46), 'proc': (260, 47), 'dec': (236, 92), 'io': (260, 47), 'sub': (260, 47),
        'db': (260, 60), 'off': (210, 56), 'note': (250, 52)}
SUBH = {'proc': 63, 'io': 63, 'db': 79, 'dec': 104}

cells = []
uid = [0]


def nid():
    uid[0] += 1
    return 'ra-%d' % uid[0]


def label(title, sub=None, bold=True):
    t = '<b>%s</b>' % title if bold else title
    if sub:
        t += '<br><span style="font-size:10px;color:#555555;">%s</span>' % sub
    return t


def vertex(style, value, x, y, w, h, cid=None):
    cid = cid or nid()
    cells.append('<mxCell id="%s" parent="1" style="%s" value="%s" vertex="1"><mxGeometry x="%.1f" y="%.1f" width="%.1f" height="%.1f" as="geometry" /></mxCell>'
                 % (cid, escape(style, {'"': '&quot;'}), escape(value, {'"': '&quot;'}), x, y, w, h))
    return cid


def edge(src, dst, text='', sub=None, ex='b', en='t', pts=None, lx=-0.75, style=None):
    cid = nid()
    v = text
    if sub:
        v += '<br><span style="font-weight:normal;color:#777777;font-size:11px;">%s</span>' % sub
    (a, b), (c, d) = SIDE[ex], SIDE[en]
    st = style or EDGE.format(ex=a, ey=b, nx=c, ny=d)
    geo = '<mxGeometry relative="1" x="%s" as="geometry">' % lx
    if pts:
        geo += '<Array as="points">' + ''.join('<mxPoint x="%.1f" y="%.1f" />' % p for p in pts) + '</Array>'
    geo += '</mxGeometry>'
    cells.append('<mxCell id="%s" parent="1" source="%s" target="%s" edge="1" style="%s" value="%s">%s</mxCell>'
                 % (cid, src, dst, escape(st, {'"': '&quot;'}), escape(v, {'"': '&quot;'}), geo))
    return cid


class Panel:
    """A white panel with a grey header; nodes are placed in a main column and a side column."""

    def __init__(self, x, y, w, title, subtitle, rel, main=300, side=630):
        self.x, self.y, self.w = x, y, w
        self.cx, self.sx = x + main, x + side
        self.title, self.subtitle, self.rel = title, subtitle, rel
        self.box = {}

    def node(self, key, kind, title, sub=None, col='main', y=None, cx=None, w=None, h=None, bold=True):
        W, H = SIZE[kind]
        if sub and kind in SUBH:
            H = SUBH[kind]
        W, H = w or W, h or H
        c = cx if cx is not None else (self.cx if col == 'main' else self.sx)
        style = ST[kind]
        txt = label(title, sub, bold) if kind not in ('note',) else title
        if kind == 'term':
            txt = '<b>%s</b>' % title
        cid = vertex(style, txt, c - W / 2, y, W, H)
        self.box[key] = (cid, c - W / 2, y, W, H)
        return y + H

    def id(self, k):
        return self.box[k][0]

    def mid_y(self, k):
        _, x, y, w, h = self.box[k]
        return y + h / 2

    def left(self, k):
        return self.box[k][1]

    def right(self, k):
        _, x, y, w, h = self.box[k]
        return x + w

    def top(self, k):
        return self.box[k][2]

    def bottom(self, k):
        _, x, y, w, h = self.box[k]
        return y + h

    def frame(self, height):
        # insert panel background before its contents so it sits underneath
        bg = ['<mxCell id="%s" parent="1" style="%s" value="" vertex="1"><mxGeometry x="%.1f" y="%.1f" width="%.1f" height="%.1f" as="geometry" /></mxCell>'
              % (nid(), ST['panel'], self.x, self.y, self.w, height),
              '<mxCell id="%s" parent="1" style="%s" value="" vertex="1"><mxGeometry x="%.1f" y="%.1f" width="%.1f" height="96" as="geometry" /></mxCell>'
              % (nid(), ST['head'], self.x, self.y, self.w)]
        return bg

    def header(self):
        vertex(ST['title'], '<b>%s</b>' % self.title, self.x + 20, self.y + 14, self.w - 240, 32)
        vertex(ST['subtitle'], self.subtitle, self.x + 20, self.y + 50, self.w - 40, 40)
        vertex(ST['rel'], self.rel, self.x + self.w - 220, self.y + 14, 200, 32)


def build_panel(fn, *args, **kw):
    start = len(cells)
    p = Panel(*args, **kw)
    p.header()
    h = fn(p)
    cells[start:start] = p.frame(h)
    p.h = h
    return p


GAP = 46
TOP = 136  # first node y offset inside a panel


# ---------------- panel builders ----------------
def overall(p):
    y = p.y + TOP
    y = p.node('s', 'term', '시작', y=y) + GAP
    y = p.node('n1', 'proc', '전원 켜기 · 준비', 'ROS 2 · Nav2 · 카메라 · 통신 연결 확인', y=y) + GAP
    y = p.node('d1', 'dec', '준비 완료?', y=y)
    p.node('e1', 'io', '오류 화면 표시', '문제 해결 후 다시 시도', col='side', y=p.mid_y('d1') - 31.5)
    y += GAP
    y = p.node('n2', 'proc', '탐색 섹터 목록 준비', '4개 섹터 · 순서 · 좌표', y=y) + GAP
    y = p.node('sp1', 'sub', '① 섹터 이동', y=y) + GAP
    y = p.node('sp2', 'sub', '② 토마토 탐지 · 수량 정리', y=y) + GAP
    y = p.node('sp3', 'sub', '③ 로봇 B에 작업 정보 전송', y=y) + GAP
    y = p.node('d2', 'dec', '남은 섹터 있음?', 'i &lt; 전체 섹터 수', y=y) + GAP
    y = p.node('io1', 'io', '탐색 완료 보고 전송', '섹터별 탐지 · 전송 결과', y=y) + GAP
    y = p.node('sp4', 'sub', '④ 미수확 재확인', y=y) + GAP
    y = p.node('sp5', 'sub', '⑤ 작업 마무리', y=y) + GAP
    y = p.node('e', 'term', '끝', y=y) + 50
    # notes (partial rectangles) beside sub-processes, linked with dashed lines like Robot B
    nb = p.node('nt1', 'note', '배터리가 부족하면 충전 위치로<br>복귀 후 이어서 (①에서 확인)', col='side', y=p.mid_y('sp1') - 26)
    p.node('nt2', 'note', '전송 후 로봇 B가 작업하는 동안<br>A는 다음 섹터를 먼저 탐색 (선행 탐색)', col='side', y=p.mid_y('sp3') - 26)
    p.node('nt3', 'note', '⑥ 비상 상황 처리는<br>모든 단계에서 항상 감시', col='side', y=p.mid_y('n2') - 26)
    for a, b in (('sp1', 'nt1'), ('sp3', 'nt2'), ('n2', 'nt3')):
        edge(p.id(a), p.id(b), style=DASH + 'exitX=1;exitY=0.5;entryX=0;entryY=0.5;')
    # flow
    seq = ['s', 'n1', 'd1']
    for a, b in zip(seq, seq[1:]):
        edge(p.id(a), p.id(b))
    edge(p.id('d1'), p.id('e1'), '아니오', ex='r', en='l')
    edge(p.id('e1'), p.id('n1'), ex='t', en='r', pts=[(p.sx, p.mid_y('n1'))])
    edge(p.id('d1'), p.id('n2'), '예')
    for a, b in zip(['n2', 'sp1', 'sp2', 'sp3'], ['sp1', 'sp2', 'sp3', 'd2']):
        edge(p.id(a), p.id(b))
    lane = p.left('sp1') - 50
    edge(p.id('d2'), p.id('sp1'), '예', sub='다음 섹터 i + 1', ex='l', en='l',
         pts=[(lane, p.mid_y('d2')), (lane, p.mid_y('sp1'))], lx=-0.6)
    edge(p.id('d2'), p.id('io1'), '아니오')
    for a, b in zip(['io1', 'sp4', 'sp5'], ['sp4', 'sp5', 'e']):
        edge(p.id(a), p.id(b))
    # legend + scope box on the right
    lx, ly = p.x + 830, p.y + 130
    vertex(ST['leghead'], '<b>기호 설명</b>', lx, ly, 200, 24)
    items = [('term', '시작 / 끝'), ('proc', '처리 (로봇 동작)'), ('dec', '판단 (예 / 아니오)'),
             ('io', '입력 · 출력 (버튼, 화면, 통신)'), ('sub', '하위 기능 (별도 차트)'),
             ('db', '기록 저장'), ('off', '다른 차트로 연결')]
    small = {'term': 'rounded=1;arcSize=50;html=1;fillColor=#2B2B2B;strokeColor=#2B2B2B;',
             'proc': 'rounded=0;html=1;fillColor=#EAF1FD;strokeColor=#3B6FD8;',
             'dec': 'rhombus;html=1;fillColor=#FFF3E0;strokeColor=#E08A1E;',
             'io': 'shape=parallelogram;perimeter=parallelogramPerimeter;fixedSize=1;size=8;html=1;fillColor=#E6F6EC;strokeColor=#2F9E5B;',
             'sub': 'shape=process;backgroundOutline=1;size=6;fixedSize=1;html=1;fillColor=#F1EAFD;strokeColor=#7C4DCC;',
             'db': 'shape=cylinder3;boundedLbl=1;backgroundOutline=1;size=8;html=1;fillColor=#EFEFEF;strokeColor=#666666;',
             'off': 'shape=offPageConnector;size=6;fixedSize=1;html=1;fillColor=#FFFFFF;strokeColor=#2B2B2B;'}
    for i, (k, t) in enumerate(items):
        yy = ly + 34 + i * 36
        vertex(small[k], '', lx, yy, 48, 26)
        vertex(ST['legtxt'], t, lx + 58, yy, 220, 26)
    sy = ly + 34 + len(items) * 36 + 24
    vertex(ST['scope'], '<b>로봇 A 담당 범위</b><br>① Nav2로 섹터 순회 · 도착 확인<br>② YOLO로 토마토 탐지<br>'
           '③ 섹터별 목표 · 의심 수량 전송<br>④ B 작업 중 다음 섹터 선행 탐색<br>'
           '⑤ B가 끝낸 섹터 미수확 재확인<br><br><b>제외 (로봇 B):</b><br>투입구 계수 · 작업자 완료 버튼 · 집하장 이동',
           lx, sy, 270, 178)
    return y - p.y


def sector_move(p):
    y = p.y + TOP
    y = p.node('s', 'term', '시작', y=y) + GAP + 20
    y = p.node('db1', 'dec', '배터리 충분?', y=y)
    p.node('ch', 'proc', '충전 위치로 복귀 · 대기', '배터리 부족 알림 · 충전 후 다시 확인', col='side', y=p.mid_y('db1') - 31.5)
    y += GAP
    y = p.node('ni', 'proc', '섹터 i 설정', '처음 i = 1, 이후 i + 1', y=y) + GAP
    y = p.node('np', 'proc', '이동 경로 정하기', '현재 위치 → 섹터 i 최단 경로', y=y) + GAP
    y = p.node('nm', 'proc', '섹터 i로 자율주행', 'Nav2 · 장애물 피하기', y=y) + GAP
    y = p.node('da', 'dec', '목적지 도착?', '현재 위치 확인', y=y)
    p.node('dr', 'dec', '재시도 3회 넘음?', col='side', y=p.mid_y('da') - 46)
    p.node('xf', 'io', '이동 실패 알림', '섹터 건너뜀 표시 · 관리자 확인', col='side', y=p.bottom('dr') + GAP)
    p.node('of2', 'off', '③ 전송으로 (실패 상태)', col='side', y=p.bottom('xf') + GAP)
    y += GAP
    y = p.node('ns', 'proc', '정지 · 촬영 위치 확보', '카메라 영상 준비', y=y) + GAP
    y = p.node('of1', 'off', '② 토마토 탐지로', y=y) + 50
    edge(p.id('s'), p.id('db1'))
    edge(p.id('db1'), p.id('ch'), '아니오', ex='r', en='l')
    ymid = (p.bottom('s') + p.top('db1')) / 2
    edge(p.id('ch'), p.id('db1'), ex='t', en='t', pts=[(p.sx, ymid), (p.cx, ymid)])
    edge(p.id('db1'), p.id('ni'), '예')
    for a, b in (('ni', 'np'), ('np', 'nm'), ('nm', 'da')):
        edge(p.id(a), p.id(b))
    edge(p.id('da'), p.id('dr'), '아니오', ex='r', en='l')
    edge(p.id('dr'), p.id('nm'), '아니오', sub='위치 다시 맞추기', ex='t', en='r', pts=[(p.sx, p.mid_y('nm'))], lx=-0.5)
    edge(p.id('dr'), p.id('xf'), '예')
    edge(p.id('xf'), p.id('of2'))
    edge(p.id('da'), p.id('ns'), '예')
    edge(p.id('ns'), p.id('of1'))
    return y - p.y


def detect(p):
    y = p.y + TOP
    y = p.node('s', 'term', '시작', y=y) + GAP
    y = p.node('c1', 'proc', '층별 촬영', '1층 … N층 · 각도별 영상', y=y) + GAP
    y = p.node('c2', 'proc', 'YOLO로 토마토 탐지', '익음 · 미숙 · 병충해 의심', y=y) + GAP
    y = p.node('dc', 'dec', '신뢰도 ≥ 기준?', y=y)
    p.node('c3', 'proc', "'의심'으로 분류", '사람 확인 필요 표시', col='side', y=p.mid_y('dc') - 31.5)
    y += GAP
    y = p.node('c4', 'proc', '섹터별 수량 정리', '익음 = 수확 목표 · 미숙 · 의심', y=y) + GAP
    y = p.node('dr', 'dec', '익은 토마토<br>있음?', y=y)
    p.node('c6', 'db', '수확 대상에서 제외', '목표 0 · 미숙 · 의심만 기록', col='side', y=p.mid_y('dr') - 39.5)
    y += GAP
    y = p.node('c5', 'db', '수확 목표 n개 저장', '섹터 ID · 익음 n · 미숙 · 의심', y=y) + GAP
    y = p.node('of', 'off', '③ 작업 정보 전송으로', y=y) + 50
    for a, b in (('s', 'c1'), ('c1', 'c2'), ('c2', 'dc')):
        edge(p.id(a), p.id(b))
    edge(p.id('dc'), p.id('c3'), '아니오', ex='r', en='l')
    edge(p.id('c3'), p.id('c4'), ex='b', en='r', pts=[(p.sx, p.mid_y('c4'))])
    edge(p.id('dc'), p.id('c4'), '예')
    edge(p.id('c4'), p.id('dr'))
    edge(p.id('dr'), p.id('c6'), '아니오', ex='r', en='l')
    edge(p.id('dr'), p.id('c5'), '예')
    edge(p.id('c5'), p.id('of'))
    edge(p.id('c6'), p.id('of'), ex='b', en='r', pts=[(p.sx, p.mid_y('of') - 6)])
    return y - p.y


def send(p):
    y = p.y + TOP
    y = p.node('s', 'term', '시작', y=y) + GAP
    y = p.node('t1', 'proc', '작업 정보 만들기', '섹터 ID · 목표 개수 · 의심 개수 · 좌표', y=y) + GAP
    y = p.node('t2', 'io', '로봇 B에 전송', 'ROS 2 토픽', y=y) + GAP
    y = p.node('d1', 'dec', 'B 수신 확인<br>받음?', y=y)
    p.node('d2', 'dec', '재전송 3회 넘음?', col='side', y=p.mid_y('d1') - 46)
    p.node('t3', 'io', '통신 경고 표시', '결과 보관 · 다시 연결되면 전송', col='side', y=p.bottom('d2') + GAP)
    y += GAP + 40
    y = p.node('t4', 'db', '섹터 탐색 결과 기록', '섹터 ID · 목표 · 의심 · 전송 시각', y=y) + GAP
    y = p.node('e', 'term', '끝 (전체 흐름으로)', y=y) + 50
    for a, b in (('s', 't1'), ('t1', 't2'), ('t2', 'd1')):
        edge(p.id(a), p.id(b))
    edge(p.id('d1'), p.id('d2'), '아니오', ex='r', en='l')
    edge(p.id('d2'), p.id('t2'), '아니오', sub='1초 뒤 다시 전송', ex='t', en='r', pts=[(p.sx, p.mid_y('t2'))], lx=-0.5)
    edge(p.id('d2'), p.id('t3'), '예')
    edge(p.id('t3'), p.id('t4'), ex='b', en='r', pts=[(p.sx, p.mid_y('t4'))])
    edge(p.id('d1'), p.id('t4'), '예')
    edge(p.id('t4'), p.id('e'))
    return y - p.y


def recheck(p):
    y = p.y + TOP
    y = p.node('s', 'term', '시작', y=y) + GAP
    y = p.node('w', 'proc', '로봇 B 완료 알림 기다리기', '배터리 부족 시 충전 후 복귀', y=y) + GAP
    y = p.node('d1', 'dec', '섹터 완료 알림<br>받음?', y=y) + GAP
    y = p.node('r1', 'proc', '완료된 섹터로 이동', 'Nav2', y=y) + GAP
    y = p.node('r2', 'proc', '대상 재확인', 'YOLO로 남은 익은 토마토 확인', y=y) + GAP
    y = p.node('d2', 'dec', '미수확 토마토<br>있음?', y=y)
    p.node('r3', 'db', '미수확 구역 정보 갱신', '섹터 ID · 남은 개수 · 좌표', col='side', y=p.mid_y('d2') - 39.5)
    p.node('r4', 'io', '로봇 B에 미수확 구역 전송', '다시 수확 요청', col='side', y=p.bottom('r3') + GAP)
    y += GAP
    y = p.node('r5', 'db', '섹터 완료 확정 기록', y=y) + GAP
    y = p.node('d3', 'dec', '모든 섹터<br>확인 끝?', y=y) + GAP
    y = p.node('of', 'off', '⑤ 작업 마무리로', y=y) + 50
    edge(p.id('s'), p.id('w'))
    edge(p.id('w'), p.id('d1'))
    lane1 = p.left('w') - 40
    lane2 = p.left('w') - 70
    edge(p.id('d1'), p.id('w'), '아니오', sub='기다림', ex='l', en='l', pts=[(lane1, p.mid_y('d1')), (lane1, p.mid_y('w') - 8)], lx=-0.4)
    edge(p.id('d1'), p.id('r1'), '예')
    edge(p.id('r1'), p.id('r2'))
    edge(p.id('r2'), p.id('d2'))
    edge(p.id('d2'), p.id('r3'), '예', ex='r', en='l')
    edge(p.id('r3'), p.id('r4'))
    far = p.right('r4') + 40
    edge(p.id('r4'), p.id('w'), ex='r', en='r', pts=[(far, p.mid_y('r4')), (far, p.mid_y('w'))])
    edge(p.id('d2'), p.id('r5'), '아니오')
    edge(p.id('r5'), p.id('d3'))
    edge(p.id('d3'), p.id('w'), '아니오', ex='l', en='l', pts=[(lane2, p.mid_y('d3')), (lane2, p.mid_y('w') + 8)], lx=-0.6)
    edge(p.id('d3'), p.id('of'), '예')
    return y - p.y


def finish(p):
    y = p.y + TOP
    y = p.node('s', 'term', '시작', y=y) + GAP
    y = p.node('f1', 'proc', '전체 결과 정리', '섹터별 목표 · 탐지 · 미수확 개수', y=y) + GAP
    y = p.node('f2', 'db', '최종 결과 저장', y=y) + GAP
    y = p.node('f3', 'io', '결과 화면 표시 · 관리자 보고', y=y) + GAP
    y = p.node('f4', 'proc', '충전 위치로 이동', 'Nav2', y=y) + GAP
    y = p.node('f5', 'proc', '대기 상태로 전환', '다음 작업 명령 기다림', y=y) + GAP
    y = p.node('e', 'term', '끝', y=y) + 50
    seq = ['s', 'f1', 'f2', 'f3', 'f4', 'f5', 'e']
    for a, b in zip(seq, seq[1:]):
        edge(p.id(a), p.id(b))
    return y - p.y


def emergency(p):
    y = p.y + TOP
    y = p.node('s', 'term', '시작', y=y) + GAP
    y = p.node('g1', 'proc', '로봇 상태 확인', '비상 버튼 · 통신 · 카메라 · 배터리', y=y) + GAP
    rows = [('d1', '비상정지<br>버튼 눌림?', 'h1', '즉시 정지', '작업 상태 저장'),
            ('d2', '통신이 3초 이상<br>끊김?', 'h2', '정지 · 경고 표시', '다시 연결 시도 · 결과 보관'),
            ('d3', '카메라 인식<br>이상?', 'h3', '탐지 일시 중지 · 경고', '해당 섹터 재탐색 예약'),
            ('d4', '배터리 부족?', 'h4', '현재 섹터 저장', '충전 위치로 복귀')]
    for d, dt, h, ht, hs in rows:
        y = p.node(d, 'dec', dt, y=y)
        p.node(h, 'proc', ht, hs, col='side', y=p.mid_y(d) - 31.5)
        y += GAP - 10
    p.node('k1', 'io', '관리자 확인 · 재시작 입력', col='side', y=p.bottom('h4') + GAP + 10)
    p.node('of', 'off', '멈췄던 단계로 복귀', col='side', y=p.bottom('k1') + GAP)
    y = max(y, p.bottom('of')) + 50
    edge(p.id('s'), p.id('g1'))
    edge(p.id('g1'), p.id('d1'))
    for (d, _, h, _, _), nxt in zip(rows, ['d2', 'd3', 'd4', None]):
        edge(p.id(d), p.id(h), '예', ex='r', en='l')
        if nxt:
            edge(p.id(d), p.id(nxt), '아니오')
    lane = p.left('g1') - 50
    edge(p.id('d4'), p.id('g1'), '아니오', sub='정상 · 계속 감시', ex='l', en='l',
         pts=[(lane, p.mid_y('d4')), (lane, p.mid_y('g1'))], lx=-0.75)
    rl = p.right('h1') + 30
    for h in ('h1', 'h2', 'h3'):
        edge(p.id(h), p.id('k1'), ex='r', en='r', pts=[(rl, p.mid_y(h)), (rl, p.mid_y('k1'))])
    edge(p.id('h4'), p.id('k1'))
    edge(p.id('k1'), p.id('of'))
    return y - p.y


def main(out):
    X0, Y0, GX, GY = 40, 40, 60, 60
    W_OV, W = 1130, 820
    p0 = build_panel(overall, X0, Y0, W_OV, '로봇 A 전체 흐름',
                     '섹터 이동 → 토마토 탐지 · 수량 정리 → 로봇 B에 작업 정보 전송을 섹터마다 반복하고, B가 끝낸 섹터는 다시 확인',
                     '로봇 A 담당: BR-__ (번호 입력)')
    x1 = X0 + W_OV + GX
    a1 = build_panel(sector_move, x1, Y0, W, '① 섹터 이동',
                '배터리를 확인하고 섹터 i까지 경로를 정해 Nav2로 이동한 뒤 촬영 위치에 정지', '관련: BR-__')
    a2 = build_panel(detect, x1 + W + GX, Y0, W, '② 토마토 탐지 · 수량 정리',
                '층별로 찍은 영상을 YOLO로 분석해 익음 · 미숙 · 의심 개수를 섹터별로 정리', '관련: BR-__')
    a3 = build_panel(send, x1 + 2 * (W + GX), Y0, W, '③ 로봇 B에 작업 정보 전송',
                '로봇 B가 받는 형식(섹터 번호 · 목표 개수 · 병충해 의심 개수)으로 보내고, 수신 확인 후 기록', '관련: BR-__')
    y2 = Y0 + max(a1.h, a2.h, a3.h) + GY
    build_panel(recheck, x1, y2, W, '④ 미수확 재확인',
                '로봇 B가 끝낸 섹터로 가서 남은 익은 토마토가 있는지 확인하고, 있으면 B에 다시 알림', '관련: BR-__')
    build_panel(finish, x1 + W + GX, y2, W, '⑤ 작업 마무리',
                '모든 섹터 확인이 끝나면 결과를 정리해 저장하고 충전 위치로 복귀', '관련: BR-__')
    build_panel(emergency, x1 + 2 * (W + GX), y2, W, '⑥ 비상 상황 처리',
                '작업 중 모든 단계에서 항상 실행 — 멈추고 알린 뒤, 해결되면 멈췄던 단계로 복귀 (로봇 B와 같은 규칙)', '관련: 안전 요구사항')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<mxfile host="app.diagrams.net">\n'
           '  <diagram name="로봇 A 탐색 흐름도" id="robotA-flow">\n'
           '    <mxGraphModel dx="4000" dy="2600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">\n'
           '      <root>\n        <mxCell id="0" />\n        <mxCell id="1" parent="0" />\n        '
           + '\n        '.join(cells) + '\n      </root>\n    </mxGraphModel>\n  </diagram>\n</mxfile>\n')
    open(out, 'w', encoding='utf-8').write(xml)
    print('cells', len(cells))


if __name__ == '__main__':
    main(sys.argv[1])
