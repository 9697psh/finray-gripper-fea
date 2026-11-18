"""Robot A schedule reordered like Robot B's sheet: 설계 → 구현 (flow order) → 테스트 (order)."""
import csv
days = ['11월 16일', '11월 17일', '11월 18일', '11월 19일']
slots = ['오전', '오후', '저녁']
ND = len(days); NS = ND * 3
def S(d, s): return d * 3 + s
YH, SH, BOTH = '용현', '수형', '용현, 수형'
P = '계획'
# (구분, 세부항목, 비고, 담당자, 진행, {col: chip})  — contents and chips as in the team's sheet
A = [
 ('설계', '섹터 목록과 좌표 정의 (4개 좌표)', '', BOTH, '완료', {S(0,2): '완료'}),
 ('설계', '토픽·메시지 정의 → 서버와 주고받는 항목 확정', '', BOTH, '예정', {S(0,2): '진행'}),
 ('구현', 'SLAM 매핑', '', YH, '완료', {S(1,0): '완료'}),
 ('구현', '지정 좌표 Nav2 자율주행 기초 구현', '', YH, '예정', {S(1,1): P}),
 ('구현', '자율주행: 정확한 좌표 재지정, goal/result로 도착 판단', '', SH, '예정', {S(1,1): P}),
 ('구현', '이동 실패 처리: 3회 재시도/건너뛰고 서버에 기록/costmap 초기화', '구분 수정 (테스트 → 구현)', BOTH, '예정', {S(1,2): P}),
 ('구현', '시작 처리: 작업 시작 수신(SERVER)/is docked?(dock_status)/언도킹', '', YH, '예정', {S(1,0): P, S(1,1): P, S(1,2): P, S(2,0): P}),
 ('구현', '도착 후 TB4 정지/OAK-D 캡처', '', SH, '예정', {S(1,2): P}),
 ('구현', '서버 전송: (좌표/image) publish', '구분 수정 (테스트 → 구현)', SH, '예정', {S(2,1): P}),
 ('구현', '재순찰: remission_list 구독/좌표 저장 (DB에서 받아오기)', '', SH, '예정', {S(2,0): P}),
 ('구현', '재순찰: 남은 좌표로 이동/캡처/a_remission 전송', '', YH, '예정', {S(2,1): P}),
 ('구현', '방문한 좌표 remove/서버 DB에 방문 완료 표시', '구분 수정 (테스트 → 구현)', SH, '예정', {S(2,1): P, S(2,2): P, S(3,0): P}),
 ('구현', '목록이 비면 B 작업 상태 확인/잠시 대기 후 다시 확인/끝났으면 종료', '', YH, '예정', {S(2,0): P, S(2,1): P}),
 ('구현', '상시 감시: 배터리 부족/도킹 복귀/비상정지/통신 3초 끊김 이후 정지', '담당 · 일정 미정', '', '예정', {}),
 ('구현', '배터리 복귀 후 중단한 섹터부터 재개', '담당 · 일정 미정', '', '예정', {}),
 ('테스트', '주행 테스트: 시간/위치 오차/주행 거리 측정', '구분 수정 (구현 → 테스트)', YH, '예정', {S(1,1): P}),
 ('테스트', '서버 연동 테스트: 이미지/좌표 전송, 서버 수신 확인', '구분 수정 (구현 → 테스트)', SH, '예정', {S(2,0): P}),
 ('테스트', '재순찰 테스트: 더미 remission_list/B 작업 상태로 확인', '', BOTH, '예정', {S(2,1): P, S(2,2): P}),
 ('테스트', '상시 감시/배터리 복귀 재개 테스트', '담당 · 일정 미정', '', '예정', {}),
 ('테스트', '*B와 연동 테스트 (재방문 목록, B 작업 상태)', '담당 · 일정 미정', '', '예정', {}),
 ('테스트', '*통합 테스트 (A + B + 서버 + 비전)', '', BOTH, '예정', {S(2,2): P, S(3,0): P, S(3,1): P, S(3,2): P}),
]
CHIP = {'계획': '#93c47d', '완료': '#6fa8dc', '진행': '#ffd966'}
STATE = {'완료': '#93c47d', '진행 중': '#ffd966', '예정': '#d9d9d9'}
def rows(group, data):
    out = []
    for i, (kind, task, note, who, state, chips) in enumerate(data):
        first_test = kind == '테스트' and data[i - 1][0] != '테스트'
        tr = '<tr class="%s">' % ('first' if i == 0 else ('sep' if first_test else ''))
        if i == 0:
            tr += '<td class="cat" rowspan="%d">%s</td>' % (len(data), group)
        tr += '<td class="c">AMR</td><td class="c">%s</td><td class="task">%s</td><td class="note">%s</td><td class="c">%s</td>' % (kind, task, note, who)
        tr += '<td class="c st" style="background:%s">%s<span class="dd">▾</span></td>' % (STATE[state], state)
        for c in range(NS):
            cls = 'slot' + (' dayend' if c % 3 == 2 else '')
            if c in chips:
                tr += '<td class="%s" style="background:%s"><span class="chip">%s</span><span class="dd">▾</span></td>' % (cls, CHIP[chips[c]], chips[c])
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
td.cat { background: #a4c2f4; text-align: center; font-weight: 700; width: 80px; border-right: 2px solid #9a9a9a; }
td.c { text-align: center; } td.task { min-width: 420px; } td.note { min-width: 170px; color: #8a5a00; font-size: 11px; }
td.st { width: 80px; position: relative; }
td.slot { width: 52px; background: #fff; position: relative; border-right: 1px solid #e3e3e3; padding: 0 4px; }
td.dayend, th.dayend { border-right: 1px solid #8a8a8a; }
.dd { position: absolute; right: 4px; top: 8px; font-size: 9px; color: #666; }
.chip { font-size: 11px; }
tr.first td { border-top: 2px solid #8a8a8a; }
tr.sep td:not(.cat) { border-top: 2px solid #7a7a7a; }
.legend { font-size: 12px; margin: 10px 4px; color: #333; }
.legend span.k { display: inline-block; width: 34px; text-align: center; margin: 0 4px 0 12px; padding: 1px 0; }
</style></head><body><div id="wrap" style="display:inline-block;padding:8px">
<table>
<tr><th rowspan="2" class="top" style="width:80px">카테고리</th><th rowspan="2" style="width:70px">항목</th><th rowspan="2" style="width:56px">구분</th>
<th rowspan="2">세부항목</th><th rowspan="2">비고</th><th rowspan="2" style="width:84px">담당자</th><th rowspan="2">진행 상황</th>''' + head1 + '''</tr>
<tr>''' + head2 + '''</tr>
''' + rows('로봇A', A) + '''
</table>
<div class="legend"><b>정리 기준</b> &nbsp;설계 → 구현(시스템 설계도 흐름 순서) → 테스트(진행 순서) &nbsp;·&nbsp; 내용 · 담당 · 일정 칸은 원래 시트 그대로, 비고의 주황 글씨만 이번에 바뀐 점</div>
</div></body></html>'''
open('schedule3.html', 'w', encoding='utf-8').write(html)
hdr = ['카테고리', '항목', '구분', '세부항목', '비고', '담당자', '진행 상황'] + [f'{d} {s}' for d in days for s in slots]
with open('schedule3.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(hdr)
    for kind, task, note, who, state, chips in A:
        w.writerow(['로봇A', 'AMR', kind, task, note, who, state] + [chips.get(c, '') for c in range(NS)])
print(len(A), 'rows')
