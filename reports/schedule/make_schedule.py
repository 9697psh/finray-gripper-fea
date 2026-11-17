"""Robot A schedule (detailed, based on the system architecture) — HTML sheet replica + CSV."""
import csv
days = ['11월 16일', '11월 17일', '11월 18일', '11월 19일']
slots = ['오전', '오후', '저녁']
ND = len(days)
def S(d, s): return d * 3 + s
YH, SH, BOTH = '용현', '수형', '용현, 수형'
# (단계, 항목, 구분, 세부항목, 비고, 담당자, 진행, {col: chip})
A = [
 ('기반', 'AMR', '설계', '섹터 목록과 좌표 정의 (4개 좌표)', '순찰 좌표 1,2,3,4', BOTH, '완료', {S(0,2): '완료'}),
 ('기반', 'AMR', '설계', '토픽·메시지 정의 → 서버와 주고받는 항목 확정', '작업 시작 · a_mission · a_remission · remission_list · B 작업 상태', BOTH, '진행', {S(0,2): '진행', S(1,2): '진행', S(2,0): '계획'}),
 ('기반', 'AMR', '구현', 'SLAM 매핑', 'farm_map.yaml', YH, '완료', {S(1,0): '완료'}),
 ('기반', 'AMR', '구현', 'Localization · Nav2 실행 절차 정리 (맵 → 2D Pose → Nav2 active → 노드 실행)', 'Nav2 활성화 대기 문제 해결 · namespace 확인', YH, '진행', {S(1,2): '진행', S(2,0): '계획'}),
 ('발표', 'AMR', '설계', '시스템 설계도 (A · B) 정리 · 발표 자료', '18일 14:00~16:00 발표', BOTH, '진행', {S(1,2): '진행', S(2,0): '계획', S(2,1): '발표'}),
 ('발표', 'AMR', '테스트', '코드 리뷰: a_mission 순찰부 (이동 · 재시도 · 로그)', '17·18일 코드 리뷰', BOTH, '예정', {S(2,0): '계획'}),
 ('순찰', 'AMR', '구현', '좌표 Nav2 자율주행: 좌표 i로 이동 · goal ↔ result로 도착 판단', 'a_mission', YH, '진행', {S(1,1): '진행', S(1,2): '진행', S(2,0): '계획'}),
 ('순찰', 'AMR', '구현', '이동 실패 처리: 3회 재시도 → 건너뛰고 서버에 기록 · costmap 초기화', '설계도: i 이동 완료?', YH, '예정', {S(2,0): '계획'}),
 ('순찰', 'AMR', '구현', '시작 처리: 작업 시작 수신(SERVER) → is docked?(dock_status) → 언도킹', '설계도: 작업 시작 · is docked?', YH, '예정', {S(2,1): '계획'}),
 ('순찰', 'AMR', '구현', '장애물 회피 (nav2.yaml 팽창 반경 · collision_monitor)', '', SH, '예정', {S(2,0): '계획'}),
 ('순찰', 'AMR', '테스트', '주행 테스트: 4개 좌표 도달 · 장애물 회피 (CSV: 시간 · 위치 오차 · 주행 거리)', 'logs/a_mission', BOTH, '예정', {S(2,0): '계획'}),
 ('순찰', 'AMR', '구현', '도착 후 TB4 정지 → OAK-D 캡처 (카메라 이미지 1장)', '설계도: oakd 캡처 실행', YH, '예정', {S(2,1): '계획'}),
 ('순찰', 'AMR', '구현', '서버 전송: a_mission (좌표 · image) publish', '', YH, '예정', {S(2,1): '계획', S(2,2): '계획'}),
 ('순찰', 'AMR', '테스트', '서버 연동 테스트: 이미지 · 좌표 전송, 서버 수신 확인', '서버 쪽 echo로 확인', YH, '예정', {S(2,2): '계획'}),
 ('재방문', 'AMR', '구현', 'visit subscriber: remission_list 구독 → 좌표 저장 (DB에서 받아오기)', '설계도: visit subscriber', SH, '예정', {S(2,1): '계획'}),
 ('재방문', 'AMR', '구현', '재방문 순찰: 남은 좌표로 이동 → 캡처 → a_remission 전송', '순찰 이동 · 캡처 코드 재사용', SH, '예정', {S(2,2): '계획'}),
 ('재방문', 'AMR', '구현', '방문한 좌표 remove + 서버 DB에 방문 완료 표시', '같은 좌표 반복 방지', SH, '예정', {S(2,2): '계획'}),
 ('재방문', 'AMR', '구현', '목록이 비면 B 작업 상태 확인 → 잠시 대기 후 다시 확인 / 끝났으면 종료', '설계도: B 작업 끝났나?', SH, '예정', {S(2,2): '계획'}),
 ('재방문', 'AMR', '테스트', '재방문 테스트: 더미 remission_list · B 작업 상태로 확인', '더미 퍼블리셔 사용', SH, '예정', {S(3,0): '계획'}),
 ('종료', 'AMR', '구현', '현 작업 종료 → 도킹 스테이션 이동 (Nav2) → 도킹 (/dock)', '설계도: 도킹 스테이션 이동', YH, '예정', {S(2,2): '계획'}),
 ('상시 감시', 'AMR', '구현', '상시 감시: 배터리 부족 → 도킹 복귀 · 비상정지 · 통신 3초 끊김 → 정지', 'battery_state 구독', SH, '예정', {S(3,0): '계획'}),
 ('상시 감시', 'AMR', '구현', '배터리 복귀 후 중단한 섹터부터 재개', '진행 섹터 번호 저장', SH, '예정', {S(3,0): '계획'}),
 ('상시 감시', 'AMR', '테스트', '상시 감시 · 배터리 복귀 재개 테스트', '배터리 기준값 낮춰서 시험', YH, '예정', {S(3,0): '계획', S(3,1): '계획'}),
 ('통합', 'AMR', '테스트', '*B와 연동 테스트 (재방문 목록 · B 작업 상태)', 'B팀 일정 맞추기', BOTH, '예정', {S(3,0): '계획', S(3,1): '계획'}),
 ('통합', 'AMR', '테스트', '*통합 테스트 (A + B + 서버 + 비전)', '20일 이후 통합 계속', BOTH, '예정', {S(3,1): '계획', S(3,2): '계획'}),
]
CHIP = {'계획': '#93c47d', '완료': '#6fa8dc', '진행': '#ffd966', '예비': '#f9cb9c', '발표': '#f6b26b'}
STATE = {'완료': '#93c47d', '진행': '#ffd966', '예정': '#d9d9d9'}
STAGE = {'기반': '#cfe2f3', '발표': '#fce5cd', '순찰': '#d9ead3', '재방문': '#ead1dc', '종료': '#d0e0e3', '상시 감시': '#fff2cc', '통합': '#d9d2e9'}
NS = ND * 3
def rows(group, data):
    out = []
    stages = [d[0] for d in data]
    for i, (stage, item, kind, task, note, who, state, chips) in enumerate(data):
        tr = '<tr class="%s">' % ('first' if i == 0 else ('sep' if stages[i - 1] != stage else ''))
        if i == 0:
            tr += '<td class="cat" rowspan="%d">%s</td>' % (len(data), group)
        if i == 0 or stages[i - 1] != stage:
            n = stages.count(stage)
            tr += '<td class="stage" rowspan="%d" style="background:%s">%s</td>' % (n, STAGE[stage], stage)
        tr += '<td class="c">%s</td><td class="c">%s</td><td class="task">%s</td><td class="note">%s</td><td class="c">%s</td>' % (item, kind, task, note, who)
        tr += '<td class="c st" style="background:%s">%s<span class="dd">▾</span></td>' % (STATE[state], state)
        for c in range(NS):
            cls = 'slot' + (' dayend' if c % 3 == 2 else '') + (' now' if c == S(1, 2) else '')
            if c in chips:
                k = chips[c]
                tr += '<td class="%s" style="background:%s"><span class="chip">%s</span><span class="dd">▾</span></td>' % (cls, CHIP[k], k)
            else:
                tr += '<td class="%s"><span class="dd">▾</span></td>' % cls
        out.append(tr + '</tr>')
    return '\n'.join(out)
head1 = ''.join('<th colspan="3" class="day dayend">%s</th>' % d for d in days)
head2 = ''.join('<th class="sl%s">%s</th>' % (' dayend' if i % 3 == 2 else '', s) for i, s in enumerate(slots * ND))
html = '''<!doctype html><html><head><meta charset="utf-8"><style>
* { font-family: "NanumGothic","Nanum Gothic",sans-serif; box-sizing: border-box; }
body { margin: 0; background: #fff; }
table { border-collapse: collapse; font-size: 12px; color: #222; }
th { background: #a4c2f4; font-weight: 700; height: 26px; border: 1px solid #8eaadb; }
th.top { height: 52px; }
td { background: #d9d9d9; height: 29px; border-bottom: 1px solid #e6e6e6; border-right: 1px solid #cfcfcf; padding: 0 6px; white-space: nowrap; }
td.cat { background: #a4c2f4; text-align: center; font-weight: 700; width: 70px; border-right: 2px solid #9a9a9a; }
td.stage { text-align: center; font-weight: 700; width: 64px; border-right: 1px solid #9a9a9a; border-bottom: 1px solid #9a9a9a; }
td.c { text-align: center; } td.task { min-width: 440px; } td.note { min-width: 220px; color: #555; font-size: 11px; }
td.st { width: 76px; position: relative; }
td.slot { width: 52px; background: #fff; position: relative; border-right: 1px solid #e3e3e3; padding: 0 4px; }
td.slot.now { box-shadow: inset 0 0 0 2px #e06666; }
td.dayend, th.dayend { border-right: 1px solid #8a8a8a; }
.dd { position: absolute; right: 4px; top: 8px; font-size: 9px; color: #666; }
.chip { font-size: 11px; }
tr.first td { border-top: 2px solid #8a8a8a; }
tr.sep td:not(.cat) { border-top: 1px solid #9a9a9a; }
.legend { font-size: 12px; margin: 10px 4px; color: #333; line-height: 1.9; }
.legend span.k { display: inline-block; width: 34px; text-align: center; margin: 0 4px 0 12px; padding: 1px 0; }
</style></head><body><div id="wrap" style="display:inline-block;padding:8px">
<table>
<tr><th rowspan="2" class="top" style="width:70px">카테고리</th><th rowspan="2" style="width:64px">단계</th><th rowspan="2" style="width:56px">항목</th><th rowspan="2" style="width:52px">구분</th>
<th rowspan="2">세부항목</th><th rowspan="2">비고</th><th rowspan="2" style="width:84px">담당자</th><th rowspan="2">진행 상황</th>''' + head1 + '''</tr>
<tr>''' + head2 + '''</tr>
''' + rows('로봇A', A) + '''
</table>
<div class="legend"><b>범례</b><span class="k" style="background:#93c47d">계획</span>예정 작업
<span class="k" style="background:#ffd966">진행</span>진행 중<span class="k" style="background:#6fa8dc">완료</span>완료
<span class="k" style="background:#f6b26b">발표</span>시스템 설계도 발표 (18일 14:00~16:00)
&nbsp;·&nbsp; <span style="box-shadow: inset 0 0 0 2px #e06666;padding:1px 6px">빨간 테두리</span> = 지금 (17일 저녁)<br>
단계는 시스템 설계도의 블록 순서: 기반(Localization · Nav2) → 순찰 → 재방문 → 종료(도킹) → 상시 감시 → 통합 &nbsp;·&nbsp; 18일 오후는 발표로 작업 시간이 짧음 &nbsp;·&nbsp; 시스템 통합은 19일부터 최소 2일
</div></div></body></html>'''
open('schedule2.html', 'w', encoding='utf-8').write(html)

hdr = ['카테고리', '단계', '항목', '구분', '세부항목', '비고', '담당자', '진행 상황'] + [f'{d} {s}' for d in days for s in slots]
with open('schedule2.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(hdr)
    for stage, item, kind, task, note, who, state, chips in A:
        w.writerow(['로봇A', stage, item, kind, task, note, who, state] + [chips.get(c, '') for c in range(NS)])
print(len(A), 'rows')
