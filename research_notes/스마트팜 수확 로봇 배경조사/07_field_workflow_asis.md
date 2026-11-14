# 상업 스마트팜(온실·수직농장) 현업 수확 작업 프로세스 AS-IS 조사 — Robot A(예찰·숙도·병해충·자율주행·정보공유) / Robot B(작업자 추종 카트·디스플레이·적재 확인·수확기록) 매핑용

> 조사 방법·한계 (보고서 작성자 필독)
> - 조사일: 2026-11-14. WebSearch(standard/extended) 약 30회로 조사함. 이 세션에서는 WebFetch가 대부분의 도메인(ridder.com, hortidaily.com, newsis.com, etnews.com, sival-innovation.com 등)에서 DNS 차단되어 **원문을 직접 열어보지 못함**. 아래 인용은 검색 엔진이 돌려준 원문 발췌(snippet) 기준이며, 수치는 가능한 한 원문 문장이 함께 제시된 것만 넣음.
> - 네덜란드 노동 표준 수치 상당수는 2000~2010년 전후 자료(WUR/IMAG 보고서)로 오래됨. 연도를 함께 표기함.
> - 한국 대형 토마토/파프리카 농장의 "작업자별 통로 배정·성과급·작업지시 방식"을 직접 다룬 2018년 이후 공개 르포는 찾지 못함 → Gaps에 명시.

---

## Q1. 일일/주간 작업 흐름: 예찰 → 수확 대상 판단 → 수확 → 상자 적재 → 대차/파이프레일 운반 → 집하장/선별장 → 선별·포장 → 저온저장 → 출하 → 기록 (단계별 담당·도구·소요시간)

### Takeaway
상업 온실의 수확 사이클은 "작업자가 파이프레일 수확대차(상자 4~8개 적재)를 밀며 통로(row)를 따라 수확 → 통로 끝/주통로에서 대차를 집하장으로 운반 → 선별기(또는 수작업) 선별·포장 → 예냉/저온저장 → 출하(농협 APC·도매시장·계열업체)" 구조이며, 토마토는 주 2~3회, 파프리카는 연 약 48회(≈주 1회), 오이는 주 3~4회~매일 수확한다. 시설 토마토 노동시간 중 수확이 약 1/3(한국 32.6%, 네덜란드 29%)을 차지하는 최대 단일 작업이다.

### Cited Findings
**작업 단계와 도구**
- 네덜란드 토마토 농가: 온실 내 수확은 파이프레일(buisrail) 위를 달리는 대차(kar)로 하며, 송이토마토(tros)는 수확대차 위 상자(doos)에 담는다 — [Bedrijfsprocesanalyse bij moderne trostomatenteeltbedrijven (WUR)](https://edepot.wur.nl/176100); [BSc thesis Agrotechnologie (WUR)](https://edepot.wur.nl/176513)
- 수확대차 사양 예: Taks 수확대차 — 소형 상자(30×40cm) 8개 또는 크레이트(60×40cm) 4개 적재, 롤러컨베이어 길이 2,400mm — [Machinio: Tomato harvesting trolleys (중고 장비 리스팅)](https://www.machinio.com/cat/tomato-harvesting-trolleys)
- 집하장(하역·계량) 설비 용량 예: Taks 송이토마토 하역·계량 시스템은 온실 약 5~10ha용, 최대 약 1,000상자/시간; Koat 처리·팔레타이징 시스템은 약 2,000상자/시간 (판매자 정격값, 실측 아님) — [Machinio](https://www.machinio.com/cat/tomato-harvesting-trolleys)
- 한국 대형 유통업체 직영 파프리카 온실(2026.3 기사): 작업자가 파프리카를 따 카트에 담으면 카트가 자동으로 선별장까지 이동, 온실 곳곳의 QR코드로 구역별 작물 상태 점검 — [‘꼭지만 따서 한입’… 딸기보다 더 달콤 (국민일보, 2026-03-19)](https://www.kmib.co.kr/article/20260319500018) (최첨단 시설 사례, 일반 농가와 차이 있음)
- 파프리카 계열업체 선별·출하 흐름: 농가 원물 수집 → 선별장 입고 → 농가별 식별번호 부여 → 선별기준표(무게·숙도·모양·색택·흠집·수축)에 따른 선별 → 상자 포장·바코드 부착 → 출하 상차 → 저온 수출 운송. 씨없는 소형 품종은 전용 선별기 부재로 수선별이 많음. 농가는 영농일지에 "주요 작업내역 및 소요인력" 기재 — [전북농업인교육원 파프리카 재배 과정 교재](https://agriacademy.jeonbuk.go.kr/data/file/ad_02_01/3556559627_mHvOsa0p_Fe_4.pdf)
- 파프리카 하절기: 선도 저하 방지를 위해 이른 아침 수확, 수확 직후 예냉 또는 저온저장고 입고 — [파프리카전문 농산 유통 안내](http://paprika.kr/story/circulation.php)
- 농협 스마트 APC(강원 영월, 토마토): 선별·포장·출하를 APC가 맡아, 과거 농가가 4~5시간 들이던 선별·포장 작업을 농가가 더 이상 하지 않음. APC 입고 시 중량·농가 정보 자동 인식(675kg 입고 사례) — [675㎏ 토마토 들어오자 선별·포장 '척척'…농협 스마트 APC 가보니 (서플)](https://supple.kr/news/cmts9xgg2003zx2d8iwnmdn77)
- 봉화군 임대형 스마트팜(2026.4): B동에서 3개 팀 9명이 토마토 재배, 선별기 시간당 2만 개 처리, 도매시장·로컬푸드·택배로 출하 — [봉화군 스마트팜, 토마토 선별기 도입 (메트로서울, 2026-04-02)](https://www.metroseoul.co.kr/article/20260402500277); [대한경제 2026-04-13](https://www.dnews.co.kr/uhtml/view.jsp?idxno=202604130837594150914)
- 딸기 고설 수경(밀양 농가 사례): 새벽 4~8시 수확, 오전 8시~오후 2시 포장, 별도 인력 없이 가족 2명이 수확·포장 전담 — [딸기 고설 수경 재배 (농업인신문)](https://www.nongupin.co.kr/news/articleView.html?idxno=202757)
- 딸기 수출용 선별기(농진청): 카메라로 착색도·모양 판정, 시간당 10,800개, 정확도 90% 이상, 노동력 부담 50% 이상 경감 — [딸기 수출농가에 도움되는 패키지 기술 개발 (영농자재신문)](https://www.newsfm.kr/news/article_print.html?no=3375)

**수확 주기**
- 토마토: 주 2~3회 수확 권장 — [Greenhouse Tomato guide (Univ. of Kentucky)](https://publications.ca.uky.edu/sites/publications.ca.uky.edu/files/ghtomatoes.pdf); 3~4일 간격(주 2~3회), 소량 자주 수확이 식물 부담이 적음 — [CEAC Univ. of Arizona Ch.8](https://ceac.arizona.edu/sites/default/files/Ch8.pdf); "대부분의 농장은 주 3회 수확" — [Labor Management Tips For Greenhouse Vegetables (Greenhouse Grower)](https://www.greenhousegrower.com/management/labor-management/)
- 오이: 영양생장/생식생장 균형과 품질 유지를 위해 주 3~4회 수확 필요 — [Cucumbers 101 (Produce Grower)](https://producegrower.com/article/cucumbers-101-a-production-guide); 주 3회, 일부 농가는 매일 — [Pinova](https://pinova.hr/en/?p=10069)
- 파프리카(네덜란드): 연간 수확 횟수 48회 — [Bedrijfsprocesanalyse (WUR)](https://edepot.wur.nl/176100) 계열 데이터(검색 요약 기준)

**노동시간 중 수확 비중**
- 한국 시설토마토: 농가당 연간 노동 3,314.4시간 중 수확 1,080시간(32.6%), 재배관리 1,140시간(34.4%). 노지토마토는 1,297.6시간 중 수확 343시간(26.4%) — 농식품부 품목별 경영통계 인용 기사(검색 요약). 원문 기사 URL 직접 확인 못함 → 원자료 재확인 필요 (검색 결과 리스트상 [에너지에프엔 토마토 수확 로봇 기사](http://www.energyfn.co.kr/news/articleView.html?idxno=21154) 또는 [농민신문 2022-12-07](https://www.nongmin.com/article/20221207368061) 중 하나로 추정)
- 네덜란드 송이토마토: 조사된 6개 작업 중 수확이 연간 노동의 29%로 최대, 적엽 26%, 곁순제거·유인 21% — [Bedrijfsprocesanalyse (WUR)](https://edepot.wur.nl/176100) / [BSc thesis (WUR)](https://edepot.wur.nl/176513)
- 송이토마토는 파프리카보다 노동집약적 — [Bedrijfsprocesanalyse (WUR)](https://edepot.wur.nl/176100)

**농업 노동 일반 통계(한국)**
- 시설원예 노동투하시간: 1990년 870.3시간/10a → 2015년 412.5시간/10a — [시설원예산업의 현황과 선진화 정책방향 (농식품부 원예경영과)](https://www.horticulture.or.kr/!/download/?path=/media/14/mig/notice/2010003078_VwHpDbq5_EC8B9CEC84A4EC9B90EC9888EC8BACED8FAC3-EBB095ED989CEBAFBC.pdf&filename=%EC%8B%9C%EC%84%A4%EC%9B%90%EC%98%88%EC%8B%AC%ED%8F%AC3-%EB%B0%95%ED%98%9C%EB%AF%BC.pdf&ct=76&oi=429)
- 2024년산 10a당 소득: 토마토(수경) 1,764만원, 가지 1,509만원, 딸기(수경) 1,500만원, 오이 1,288만원 — [농촌진흥청 2024년도 농산물소득조사 결과](https://www.rda.go.kr/board/board.do?mode=view&prgId=day_farmprmninfoEntry&dataNo=100000805467)

### Inferences
- "수확 → 대차 적재 → 통로 끝 운반 → 집하장 하역"은 주 2~3회(토마토) × 전 통로 반복되는 고빈도 루틴이므로, Robot B(추종 카트)의 가동률 근거가 충분하다. 반면 선별·포장은 APC·선별기로 이미 자동화/외부화되는 추세(영월 APC, 봉화 선별기)라, Robot B의 가치 지점은 "온실 내부 수확~집하장 입고" 구간과 그 구간에서 발생하는 데이터(누가·어느 통로·몇 상자·몇 kg) 생성에 있다.
- APC 입고 시점에 비로소 중량·농가 정보가 자동 인식되는 구조 → 온실 내부(통로·작업자 단위) 데이터는 공백. Robot B의 "수확 적재 확인 + 기록"이 이 공백을 메운다.

### Gaps
- 한국 대형 토마토·파프리카 온실(예: 1ha 이상)의 수확 1회당 소요시간, 통로당 수확시간, 대차 1회 운반 거리·시간 실측치는 공개 자료에서 찾지 못함.
- 한국 시설토마토 32.6% 수치는 검색 요약에서만 확인 — 원문(농식품부 품목별 경영통계/농진청 소득자료집) 재확인 필요.
- 저온저장(예냉) 체류시간, 출하 빈도(일 1회 등)에 대한 상업 농가 실측 자료 미확보.

---

## Q2. 작업 조직 방식: 작업자별 통로(row) 할당, 수확 주기, 성과급, 작업지시 전달 방식

### Takeaway
선진(네덜란드·멕시코·일본 대형) 온실은 "작업자-통로-작업" 단위로 단말/앱에 등록하고, 이를 근거로 작업 표준 대비 성과를 관리하며 일부는 성과와 임금을 연동한다. 한국은 외국인 근로자 비중이 높고(시설원예 외국인력 64%), 작업지시는 구두·언어장벽 문제가 크며, 정부가 다국어 소통가이드를 만드는 단계다. 한국 농가의 성과급·통로배정 실무는 공개 자료가 거의 없다.

### Cited Findings
- Ridder Productive(멕시코 재배사, 작업자 약 500명): 작업자가 통로(row)나 작업을 바꿀 때 고정 단말기에서 로그인·등록 → 스케줄링, 작업별 표준 미달자 파악. 관리자 앱 제공, 딸기용 크레이트 단위 등록 기능 추가 — ["Ridder Productive motivates staff and ensures fair pay" (Ridder)](https://ridder.com/insights/projects/detail/ridder-productive-motivates-staff-and-ensures-fair-pay) (검색 요약 기준; 원문 접근 차단)
- Priva: 작업·수확 등록과 경영 리포트를 결합, 작물·부서·위치별 실적을 실시간 비교, 생산 예측 기반 인력 계획 지원 — [Priva Horticulture](https://www.priva.com/horticulture)
- 네덜란드 시공사 Stolze도 노동등록·경영정보 솔루션을 별도 제품으로 공급 — [Labor registration and management information (Stolze)](https://www.stolze.nl/en/solutions/automation/labour-registration-and-management-information/)
- 일본 대형 미니토마토 시설(3.2ha, 작업자 100명 이상): 출퇴근은 시판 앱 사용, 계획·진척관리 앱은 미도입 상태였음 → 생산관리지원시스템과 출퇴근 시스템 연계로 시프트 작성 시간 절감·작업속도 분석 기반 교육 추진 — [トマト大規模施設における生産管理支援システムの活用による労働生産性向上のための手引き (農研機構 NARO)](https://www.naro.go.jp/smart-nogyo/katsuyo-sanchi-shien/files/E08.pdf)
- 일본 JGHA 보고서(2026년 4월 게재, 令和7年度): 작업자 평가와 시급·상여 연동 사례 소개(一苺一笑), デ・リーフデ北上 등 적정 인원배치 작업관리 사례 — [JGHA スマートグリーンハウス展開推進 事業報告書 別冊2](https://jgha.com/wp-content/uploads/2026/04/TM06-07-bessatsu2.pdf)
- 일본 수확량 75톤/10a 농업법인이 노무관리 시스템을 공동개발(2021) — [反収75トンの衝撃 (マイナビ農業, 2021-08-22)](https://agri.mynavi.jp/2021_08_22_167162/)
- 한국 외국인 고용 배정 기준(농식품부): 시설원예 고용허가는 2,000~4,000㎡ 8명 이하 ~ 21,500㎡ 이상 40명 이하, 계절근로는 2,600㎡ 미만 5명 이하 ~ 6,500㎡ 이상 9명 이하. 시설원예 인력 중 외국인력 64%, 국내인력 36% — [농식품부 국민제안 답변 자료](https://www.mafra.go.kr/bbs/home/791/588435/download.do)
- 파프리카 외국인 총 고용허용인원: 고용24는 50명까지 인정 — [외국인고용관리시스템 (고용24)](https://www.eps.go.kr/eo/EmployPerSystem.eo?tabGb=05); 반면 이투데이·농식품부 자료는 25명 상한으로 기재 — [이투데이](https://www.etoday.co.kr/news/view/2092411) (시점 차이로 추정, 상충)
- 언어장벽: 작업지시·안전수칙·숙소·임금·병원 등 거의 모든 과정에서 소통 필요, 농장주-근로자 언어장벽이 여전히 큼 → 정부 8개 국어 농장 소통가이드 마련(2026.5 보도) — [농업 핵심 인력 된 외국인 노동자…‘8개 국어 소통가이드’ (다음뉴스, 2026-05-03)](https://v.daum.net/v/20260503103017506)
- 다국어 농작업 일정 안내서 제작(외국인 계절근로자용) — [농어업경제귀농신문](http://www.knongnews.com/news/articleView.html?idxno=22440)
- 충남도농업기술원: 외국인 근로자 언어별 안전정보 제공 + 전자서명으로 교육이력 관리하는 AI 서비스 실증(3개 시군 15농가) — [내외일보](https://www.naewoeilbo.com/news/articleView.html?idxno=2416639)
- 인력 이탈 사례: 충남 논산 방울토마토 농가, 외국인 3명 이탈 후 비닐하우스 40동 중 8동 로터리, 11동 방치; 외국인 일당 7~8만원 → 12~13만원 — [외국인 노동자들, 돈 더 주는 곳으로 훌쩍 (농민신문)](https://www.nongmin.com/339767); 파종·수확철 일당 15만원, 웃돈 거래 — [[탐사기획] 일당 15만원으로 껑충 (농민신문, 2021-11-05)](https://www.nongmin.com/article/20211105346768)
- 네덜란드: 원예 고용노동의 80% 이상이 인력파견업체 소속 — [The power of Dutch greenhouse vegetable horticulture (WUR)](https://edepot.wur.nl/27928) (발간연도 2000년대 후반으로 추정, 오래된 자료)

### Inferences
- 선진 온실의 "통로 단위 등록" 관행은 Robot B가 작업자 추종 중 자동으로 "작업자 ID + 통로 ID + 시각"을 기록하는 기능과 1:1 대응한다(고정 단말까지 걸어가 로그인하는 행위 제거).
- 한국은 외국인 64% + 언어장벽 → Robot B 디스플레이는 텍스트보다 아이콘·색상·다국어(베트남어·캄보디아어·네팔어 등) 작업지시 표시가 필수 요구사항.
- 성과급/성과평가 연동(일본·멕시코)은 공정한 개인별 실적 데이터가 전제 → 자동 기록의 신뢰성(오적재·중복 카운트 방지)이 Robot B 요구사항.

### Gaps
- 한국 상업 온실의 통로 배정 방식, 성과급(상자당 단가) 운용 여부, 카카오톡/화이트보드 사용 실태를 다룬 공개 조사·르포를 찾지 못함 (검색 결과 없음). 현장 인터뷰로 보완 필요.
- 네덜란드 수확 성과급(piece-rate) 관행과 CAO(단체협약) 규정 미확인.

---

## Q3. 예찰(scouting) 실무: 누가, 얼마나 자주, 어떤 양식으로, 발견 후 방제 의사결정 흐름, IPM

### Takeaway
표준 관행은 "주 1회(또는 주 2회) 고정 위치 끈끈이트랩 교체·계수 + 식물체 육안 조사 → 온실 지도/구역별 기록 → 주간 요약 → 관리자가 천적 방사 또는 약제 결정"이다. 기록 없이 진단하는 관리자는 불리하다는 것이 공통 권고이며, 한국은 "끈끈이트랩 예찰 → 초기 천적/약제" 흐름은 지침으로 있으나 농가 실무 양식·담당자 실태 자료는 부족하다.

### Cited Findings
- 끈끈이트랩: 온실 전역 배치, 최소 주 1회(밀도에 따라 더 자주) 교체·계수 기록. 주 1~2회 예찰 권장 — [IPM in the Greenhouse Series (Oklahoma State Extension)](https://extension.okstate.edu/fact-sheets/ipm-in-the-greenhouse-series-integrated-pest-management-in-commercial-greenhouses-an-overview-of-principles-and-practices)
- 기록 항목: 끈끈이트랩 계수, 주간 모니터링, 처리 내역, 처리 효과 — [UConn Greenhouse IPM factsheet (2023)](https://ipm.cahnr.uconn.edu/wp-content/uploads/sites/3216/2023/10/2023GreenhouseIPMfactsheetfinal.pdf); 입고 식물 검사·처리 기록 포함, "기록 없이 문제를 진단하는 관리자는 불리" — [Oklahoma State](https://extension.okstate.edu/fact-sheets/ipm-in-the-greenhouse-series-integrated-pest-management-in-commercial-greenhouses-an-overview-of-principles-and-practices)
- 트랩은 캐노피 위 2인치 이내, 매주 같은 위치에 새 트랩 → 추세 파악; 온실·해충·계수·특이사항별 주간 요약 작성 — [Scouting For Pathogens And Pests (Greenhouse Grower)](https://www.greenhousegrower.com/production/plant-culture/special-series/scouting-for-pathogens-and-pests-the-basics-of-monitoring/)
- 토마토: 3×5인치 황색트랩 100주당 1개(약 25개/acre), 해충·천적 주간 추적용 온실 지도 권장 — [Biological Pest Control Success in Greenhouse Tomatoes (UConn)](https://ipm.cahnr.uconn.edu/?p=1972); 가루이는 토마토 생장점을 가볍게 흔들어 확인 — [Greenhouse Canada](https://www.greenhousecanada.com/how-to-monitor-for-pests/)
- 예찰 기록은 작물별 반복 핫스팟·주요 해충 계절성 파악에 쓰임 — [Greenhouse Canada](https://www.greenhousecanada.com/how-to-monitor-for-pests/)
- 한국(경기도농업기술원 2026년 제1회 예보): 시설채소 주요 해충 총채벌레류·가루이류·진딧물류·응애류·작은뿌리파리·토마토뿔나방, 황색 끈끈이트랩 지상부 50cm 이하 설치 — [2026년 제1회 농작물 병해충 발생정보예보](https://nongup.gg.go.kr/wp-content/uploads/sites/2/2026/01/2026년-제1회-농작물-병해충-발생정보예보.pdf)
- 농진청 해충 가이드: 초기 방제가 효과적이므로 끈끈이트랩을 매달아 예찰하고, 발견 초기 천적 생물적 방제 또는 적용약제 방제 — [농사로 시설채소 해충 자료](https://www.nongsaro.go.kr/cms_contents/136/88822_MF_ATTACH_01.pdf)
- 농진청: 온실 해충 밀도·종류를 영상으로 진단하고 방제 시기·방법 제시 시스템 개발 보도. 담배나방·굴파리 등은 시설재배에서 연중 발생, 예찰이 어렵고 잦은 약제로 저항성 문제 — [데일리안 보도](https://m.dailian.co.kr/news/view/994236) (발표일 미확인)
- 네덜란드: 행정 도구로 노동등록과 함께 병해충 등록(registration of diseases and pests)이 활용됨 — [The power of Dutch greenhouse vegetable horticulture (WUR)](https://edepot.wur.nl/27928)
- 스마트 온실 방제 로봇 현장실증(농진청): 바닥 바코드를 읽고 스스로 레일에 진입해 방제, 방제 노동시간 절반 이상 절감 농가 증언 — [스마트팜에서 농작업 전 자동화를 꿈꾸다 (농진청 웹진 2022-12)](https://rda.go.kr/webzine/2022/12/sub1-5.html)

### Inferences
- 예찰은 "주 1회 × 고정 지점 × 사람 육안"이라 공간 해상도(통로·포기 단위)와 시간 해상도(주 1회)가 낮다. Robot A가 수확 주기(주 2~3회)에 맞춰 순회하면 예찰 빈도를 2~3배로 올리고 위치 태그(통로·포스트 번호)를 자동 부여할 수 있다.
- 방제 의사결정은 관리자 1인이 주간 요약을 보고 결정 → Robot A의 "핫스팟 지도 + 추세 그래프" 공유가 의사결정 직전 단계에 해당.
- 방제 로봇이 이미 "바닥 바코드 + 레일 진입" 방식으로 실증됨 → Robot A의 측위·레일 진입 방식에 참고 가능.

### Gaps
- 한국 상업 온실에서 예찰을 누가(농장주/관리자/천적업체 컨설턴트) 하는지, 기록 양식(종이/엑셀/앱) 실태 자료 미확보.
- Koppert·Biobest 등 천적 업체의 상업 농가 예찰 서비스 운영 방식(방문 주기 등)은 이번 조사에서 확인 못함.

---

## Q4. 수확량·작업 기록 실무: 수기 장부, 상자 카운트, 작업자별 실적(Priva/Ridder 단말, 바코드), 출하량, GAP/이력

### Takeaway
선진 온실은 (1) 통로·작업 전환 시 고정 단말 로그인 → (2) 수확대차/크레이트 단위 등록 → (3) 집하장 계량으로 작업자별·통로별 kg을 산출하고, 최신으로는 실내측위(Ridder CoRanger, ~10cm)로 수동 입력 없이 대차·작업자를 추적한다. 일본은 앱에 하우스·작업명·시작시각·컨테이너 수/kg를 입력한다. 한국 일반 농가는 영농일지(수기/GAP 앱)와 APC 입고 계량에 의존하며, 온실 내부의 작업자·통로 단위 기록은 연구 실증 수준이다.

### Cited Findings
- Ridder CoRanger: 비콘+태그 기반 특허 실내측위, 작업자·수확대차·물체 위치를 약 10cm 정밀도로 파악, 네덜란드 토마토 재배사 Duijvestijn에서 자동 수확·노동 등록 시험, Ridder Productive와 통합해 수동 입력 없이 수확·노동 데이터 수집 — [Ridder introduces innovative indoor positioning system CoRanger](https://ridder.com/insights/news/ridder-introduceert-innovatief-positiebepalingssysteem-coranger); [Hortidaily](https://www.hortidaily.com/article/9353949/indoor-positioning-system-pinpoints-positions-of-plants-people-and-objects-in-the-greenhouse/); [CoRanger Productive Brochure (2021)](https://www.sival-innovation.com/wp-content/uploads/2021/10/20210460-Ridder-CoRanger-Productive-Brochure-EN-DEF-LR.pdf) (발표 2021년경; 현재 보급 상태 불명)
- Ridder Productive: 고정 단말 로그인(통로·작업 변경 시), 표준 미달자 식별, 딸기용 크레이트별 등록 — [Ridder 사례](https://ridder.com/insights/projects/detail/ridder-productive-motivates-staff-and-ensures-fair-pay); 업데이트로 적용범위 확대 — [MMJdaily](https://www.mmjdaily.com/article/9811091/labor-management-system-even-more-widely-applicable-after-update/)
- Priva FS Performance: 수확·노동 등록 + 경영 리포트, 작물·부서·위치별 실시간 비교 — [Priva](https://www.priva.com/horticulture)
- 일본 ASHIGARUWARE(JGHA 보고서): 하우스명·작업명·시작시각·작업량 입력, 중단/완료 버튼. 수확은 컨테이너 수 또는 kg, 순지르기·유인 등은 작업 거리(m) 또는 레인 수로 입력 → 개인별 작업량·진척 관리 — [JGHA 令和5年度 報告書 別冊2](https://jgha.com/wp-content/uploads/2024/04/TM06-05-bessatsu2.pdf)
- 일본 NARO: 휴대 단말로 작업자명·시간·작업내용·작업구획 기록하는 작업관리 시스템, 수확작업시간 예측·계획 — [作業管理システム及び生育予測を核とした大規模施設園芸発展スキーム (NARO, 2019)](https://www.naro.go.jp/laboratory/brain/h27kakushin/keiei/research/files/keiei_subject3_04_2019.pdf); 수량·작업시간 모니터링 자동화, 온도와 수확작업시간 대조로 적절한 노무관리 시 수확작업 피크 2~5할 저감 — [施設園芸で収量・作業時間のモニタリングを自動化するシステム (NARO 2016)](https://www.naro.go.jp/project/results/4th_laboratory/nivfs/2016/16_035.html)
- HBM: 앱 기반 토마토 수확 등록 + 계량 모듈 사례 — [アプリでトマトを収穫 (HBM)](https://www.hbm.com/jp/6986/meercamp-registration-system-and-weighing-modules-provide/)
- 한국 KISTI 보고서 "토마토 온실의 스마트 생산이력관리 기술개발 및 현장실증"(2020~2021년경): 파종부터 1작기 투입 인력 조사, 농작업별 작업자 투입률·효율 분석, 농작업별 인력배분 기준·작업 매뉴얼 작성, 누적 데이터로 농작업별 적정 인원 산출 공식 도출, 노동력 향상 및 개인별 포인트 변화 확인 — [KISTI ScienceON TRKO202100010100](https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202100010100)
- 한국 GAP 기록: 'GAP 영농일지' 앱 — 작목·재배활동·농약·비료 사용 내역 날짜별 기록·검색, 인증 심사용 증빙 공유, 인증 갱신 알림 — [GAP 영농일지 (Google Play, 풀무원)](https://play.google.com/store/apps/details?id=com.pulmuone.farmdiary&hl=en_US)
- 파프리카 영농일지: 주요 작업내역·소요인력 기재, 선별장에서 농가별 식별번호·바코드 부착 — [전북농업인교육원 교재](https://agriacademy.jeonbuk.go.kr/data/file/ad_02_01/3556559627_mHvOsa0p_Fe_4.pdf)
- 농협 스마트 APC: 입고 시 중량·농가정보 자동 인식 — [서플](https://supple.kr/news/cmts9xgg2003zx2d8iwnmdn77)
- 한국 스마트온실 토마토 93개 농가(2016~2022) 데이터 표준화·상위 20%/하위 80% 분류 생산성 모델 연구 — [The Society of Convergence Knowledge Transactions Vol.12 No.3 (2024)](https://cdn.apub.kr/journalsite/sites/scvk/2024-012-03/N0890120302/N0890120302.pdf)

### Inferences
- 기록 계층: [작업자·통로·대차 단위(온실 내부)] → [집하장 계량] → [APC/선별장 농가 단위] → [출하·GAP]. 한국 일반 농가는 첫 계층이 비어 있음. Robot B의 적재 확인(상자 카운트·중량)+작업자/통로 태깅이 정확히 이 계층을 자동 생성하며, Ridder CoRanger가 해외에서 같은 가치를 "인프라(비콘)" 방식으로 제공하는 반면 Robot B는 "이동체" 방식으로 제공 → 차별점.
- 일본 앱 사례처럼 작업량 단위가 수확=컨테이너/kg, 관리작업=m/레인 수 → Robot B 기록 스키마에 그대로 차용 가능.

### Gaps
- Priva/Ridder 단말의 구체적 조작 절차(바코드 카드 스캔, 대차 라벨 등)는 원문 접근 차단으로 상세 확인 못함.
- 한국 상업 온실의 작업자별 실적 기록 보급률(수기 vs 디지털) 통계 없음.
- 농산물이력추적(이력관리) 의무 대상·기록 항목은 이번 조사 범위에서 확인 못함.

---

## Q5. 수직농장 실무 (팜에이트, 엔씽, Plenty, Bowery 등): 재배 베드 이송, 수확 스테이션, 포장 라인, 인력 구성

### Takeaway
수직농장 작업은 파종·이식·수확·선별·포장·세척이 실내 한 작업장에서 팀(대개 2인 1조) 단위로 이루어지며, 수확 노동생산성은 1.5~6.0 kg/인·시 수준으로 보고된다. 미국 대형 업체(Bowery 2024 폐업, Plenty 2025.3 파산보호)는 로봇화를 추진했으나 경제성 문제로 붕괴했고, 국내 팜에이트는 하루 약 30톤 샐러드를 출하하지만 평택 자체 스마트팜 생산은 1~1.5톤/일이다.

### Cited Findings
- 한국 경기도 수직농장 직무분석(2023, 장애인 케어팜 목적): 계층적 작업분석으로 6개 직무·28개 과업 도출, 거의 모든 작업이 한 작업장 내에서 이루어지고 대부분 2인 1조 — [Analysis of Farm Work in a Vertical Farm (J. People Plants Environ. 26(5), 2023)](https://jppe.ppe.or.kr/journal/view.php?doi=10.11628%2Fksppe.2023.26.5.495)
- 수직농장 5개 작업의 상지 근활성: 전삼각근이 가장 활성, 노지 작업보다 신체 부담 낮을 것 — [Muscle Activation Patterns ... Vertical Farming (HortTechnology 35(5))](https://journals.ashs.org/view/journals/horttech/35/5/article-p748.xml)
- iFarm 분석: 대부분 수작업인 1,000㎡ 시설 ≈ 월 1,220 인·시, 파종·이식·수확·포장 담당, 1인 다기능. 일상 운영은 소수 정규직, 주 2회 파종·수확 사이클에는 파트타임 추가 — [How many working hours does it take to run a vertical farm (iFarm)](https://ifarm.fi/blog/how-many-working-hours-does-it-take-to-run-a-vertical-farm)
- 단일 시설 6개월 수확 노동생산성 1.5~6.0 kg/인·시(타 시설 일반화 주의) — [iFarm](https://ifarm.fi/blog/how-many-working-hours-does-it-take-to-run-a-vertical-farm)
- Vertical Farm 2.0 설계 추정: 수확 하루 약 5시간, 작업자 1인 하루 약 49상자 (설계 추정치) — [Vertical Farm 2.0 (ResearchGate)](https://www.researchgate.net/publication/321427717_Vertical_Farm_20_Designing_an_Economically_Feasible_Vertical_Farm_-_A_combined_European_Endeavor_for_Sustainable_Urban_Agriculture)
- 컨테이너형(Freight Farms Greenery) 수확·포장 주 6~8시간 — [Freight Farms](https://www.freightfarms.com/blog/labor-requirements-for-the-greenery)
- 팜에이트: 하루 샐러드 출하 약 30톤, 평택 본사 스마트팜 생산은 하루 1~1.5톤 — [하루 30톤의 샐러드를 만드는 ... 팜에이트 (에스콰이어 코리아)](https://www.esquirekorea.co.kr/article/54168); 하루 6만5천 팩·30톤(2021) — [에포크타임스 2021-01](https://www.epochtimes.kr/2021/01/562389.html)
- Plenty Richmond(버지니아) 딸기 수직농장: 2024.9 개장, 40,000 sq ft 미만에서 연 400만 파운드 이상, 30ft 타워, Driscoll's 전용, 초기 약 60명 고용 → 최종 300명 이상 계획 — [Axios Richmond 2024-10-02](https://www.axios.com/local/richmond/2024/10/02/richmond-vertical-berry-farm-plenty); [Fresh Fruit Portal 2024-09-25](https://www.freshfruitportal.com/news/2024/09/25/plenty-unlimited-inc-opens-first-farm-to-grow-indoor-vertically-farmed-berries/). Compton 상추 농장은 바닥 청소·식물 검사 인력 몇 명 외 로봇 운영 — [CyberGuy/Fox News](https://cyberguy.com/ai/ai-being-used-to-run-worlds-first-indoor-vertical-berry-farm/)
- Plenty 2025년 3월 파산(챕터 11), 버지니아 딸기농장·와이오밍 R&D는 유지 계획 — [Fertilizer Daily 2025-03-26](https://www.fertilizerdaily.com/20250326-vertical-farming-startup-plenty-filed-for-bankruptcy-despite-raising-1-billion-from-softbank-walmart-and-jeff-bezos/)
- Bowery Farming 2024년 폐업, 187명 해고 — [Agriculture Dive](https://www.agriculturedive.com/news/celebrity-backed-indoor-farming-company-bowery-closes-lays-off-187-workers/732282). 기타 Fifth Season(2022), InFarm·Kalera(2023) 파산, 원인은 에너지비·설비투자·낮은 상추 가격 등 경제성 — [Agritecture](https://www.agritecture.com/blog/odyssey-teachings-about-vertical-farming)

### Inferences
- 수직농장은 동선이 짧고 작업장 집중형이라 "작업자 추종 카트"의 효용이 온실보다 낮고, 대신 베드 이송 자동화(컨베이어/AGV)·수확 스테이션 방식이 주류. Robot B의 수직농장 적용은 "다단 베드 사이 이동형 수확 보조 + 기록"으로 한정적일 가능성.
- Robot A의 수직농장 적용은 다단 선반 상부 예찰(사람 시야 밖)·딸기 숙도 판정에서 가치가 있으나, 대형 업체 붕괴 사례로 보아 투자 대비 회수 근거가 핵심.

### Gaps
- 팜에이트·엔씽 등 국내 업체의 수확·포장 공정별 인원·자동화 수준 공개 자료 없음.
- Plenty Richmond의 2025년 이후 실제 수확 인력/로봇 분담 자료 없음.
- 수직농장 직무분석 논문의 6개 직무 세부 명칭(수확·선별·포장 포함 여부)은 원문 미확인.

---

## Q6. 네덜란드 등 선진 온실의 작업 표준(kg/hr, 1인당 관리면적, 대차 운용) 및 한국과의 차이

### Takeaway
네덜란드 토마토는 노동생산성 45~71 kg/인·시(전 작업 기준), 약 3.8 연간노동단위/ha(1단위=2,000시간 이상)로 보고되며(2000년대 자료), 수확은 파이프레일 대차 기반 표준시간표(taaktijden: 100kg당 분 단위)로 관리된다. 사람 맨손 수확 실측은 22~30 kg/hr(대학 온실 시험)이고, 로봇은 12~110 kg/hr(벤더 주장 포함)로 편차가 크다. 한국은 소규모·외국인 의존·수기 기록 중심이라 표준시간 기반 관리가 거의 없다.

### Cited Findings
- 네덜란드 토마토: 노동생산성 45~71 kg/인·시, 노동비가 생산비의 37%. 노동 투입 약 1.09 h/㎡(한 유형), 0.77 h/㎡(다른 유형) — [Greenhouse Tomato Production (Peet & Welles)](https://www.researchgate.net/profile/Arvind-Singh-21/post/How_much_maximum_yield_kg_m2_can_a_farmer_get_from_the_Tomato_crop_with_all_maximum_high_end_technology/attachment/59d6377e79197b8077994d54/AS:393263811973134@1470772807893/download/1.pdf) (발간연도 미표기, 2005년경 추정)
- 토마토 약 3.8 연간노동단위(AWU)/ha (1 AWU=2,000시간 이상), 임금비의 25%가 고용노동, 고용노동의 80% 이상이 파견업체 — [The power of Dutch greenhouse vegetable horticulture (WUR)](https://edepot.wur.nl/27928)
- KWIN 2005/2006 노동항목 1,246시간(단위 불명확), Hendrix(2000)와 KWIN(2005) 차이 매우 작음 → 5년간 ha당 노동 소요가 크게 줄지 않음 — WUR 보고서(검색 요약)
- 수확 노동 규범: 수확 1,840~2,325 시간/ha (작물 불명확) — [Arbeidsnormen afgeleid uit arbeidsregistraties (IMAG-DLO, Hendrix 2000)](https://www.ergolabresearch.eu/pdf/Rapport2000Arbeidsnormen.pdf). 이 보고서 자체가 "노동등록 데이터에서 노동규범을 도출"한 것으로, 네덜란드에서 작업자 등록 데이터가 표준시간 설정에 쓰여 왔음을 보여줌
- 표준작업시간표(Taaktijden voor de groenteteelt onder glas II): 수확방법별(파이프레일 대차 좌식/보행식, 수확차) × kg/㎡ × 개/kg에 따른 규범. 예: 100kg당 50분 × 10,000kg = 83시간 — [Taaktijden (core.ac.uk)](https://core.ac.uk/download/pdf/29380325.pdf)
- 딸기 파이프레일 시스템에 의한 노동절감 프로젝트 보고서(WUR) — [Arbeidsbesparing door buisrailsysteem in Aardbei](https://edepot.wur.nl/291492); 상자 디스태커가 채소 재배자의 중노동 경감 — [Ontstapelaars nemen groentetelers vooral zwaar werk (WUR)](https://edepot.wur.nl/74854)
- 사람 수확 속도: 대학 온실 맨손 수확 약 22~30 kg/hr(3품종), 수확 보조 도구 사용 시 54~59 kg/hr 보고 — [Manually operated tomato harvesting tool for greenhouse (ISHS Acta Hort. 710)](https://ishs.org/ishs-article/710_61/)
- 로봇 수확 속도(참고): Four Growers GR-100 43 kg/hr(피크 약 63 kg/hr, 방울/그레이프) — [Four Growers (yespress)](https://yespress.io/four-growers-inc); Inaho 스낵토마토 12 kg/hr 이상 — [Future Farming](https://www.futurefarming.com/smart-farming/tomato-harvesting-robot-after-upgrade-eight-times-faster/); Qogori 110 kg/hr(벤더 주장, 미검증) — [Qogori](https://qogori.com/greenhouse-tomato-harvesting-robot-europe/); TTA-ISO 450송이/hr(2025 제품 발표) — [Nieuwe Oogst 2025-02-08](https://www.nieuweoogst.nl/nieuws/2025/02/08/450-trossen-tomaten-per-uur-oogsten-zonder-mensenhand); 네덜란드 온실 로봇 20 kg/hr 보도 — [Tridge](https://insights.tridge.com/speaker-product-news-reports/KJLyFXpzJzgKuB1Gqsm5QUKHGgR43AVdqLMyxPzHhiLkLuJMUJq9fb7Y)
- 한국: 파프리카 수출조직 계획에서 농가 호당 재배규모 0.5ha 가정(2008) — [KREI C2008-19-3](https://krei.re.kr/attach/pdf/605ba745-9baa-2a94-e054-b09928988b3c.pdf); 파프리카 재배면적 연평균 약 750ha — [KATI 파프리카](https://www.kati.net/product/basisInfo.do?lcdCode=MD147)
- 한국 시설원예 외국인력 64% / 국내 36% — [농식품부 자료](https://www.mafra.go.kr/bbs/home/791/588435/download.do)

### Inferences
- 네덜란드 3.8 AWU/ha ≈ 1ha당 상시 약 4명(연 7,600시간 이상)으로 환산 가능(추정). 한국 고용허가 기준(21,500㎡ 이상 40명 이하 ≈ 2.15ha에 최대 40명)은 상한일 뿐 실제 투입이 아님 — 직접 비교 불가.
- 사람 맨손 22~30 kg/hr vs 전 작업 45~71 kg/인·시 수치는 정의(수확만 vs 전체 노동, 실험 vs 상업)가 달라 비교 주의.
- 핵심 차이: 네덜란드는 (a) 노동등록 데이터 → (b) 표준시간 → (c) 성과관리/인력계획의 폐루프가 있음. 한국은 (a)가 없음 → Robot B의 기록 기능은 한국형 (a)를 만드는 출발점.

### Gaps
- 최신(2018~2026) KWIN 노동시간·kg/hr 공식 수치 미확보(원문 차단).
- 상업 농가 실측 1인당 관리면적(ha/인) 네덜란드·한국 모두 최신 수치 없음.
- 한국 수확대차(파이프레일 대차) 보급률·적재량 표준 자료 없음.

---

## Q7. 각 단계의 현장 Pain Point (일손 부족, 숙련도 편차, 운반 부담, 기록 누락, 정보 전달 지연)

### Takeaway
가장 근거가 강한 Pain Point는 (1) 외국인 의존 인력의 이탈·임금 급등·쿼터 부족, (2) 수확물 운반의 중량 부담(수동 운반 80kg 초과 시 사고 위험, 상자 20kg 안팎), (3) 언어장벽에 따른 작업지시 전달 문제, (4) 온실 내부 작업 데이터 부재(대규모 시설도 계획·진척관리 앱 미도입), (5) 예찰 난이도와 약제 저항성이다.

### Cited Findings
**일손 부족·이탈**
- 평택 수확철 외국인 집단 이탈로 토마토 수확 차질; 농업 외국인 쿼터 6,600명 vs 업계 요구 12,000명 — ["농촌 외국인근로자 쿼터 확대를" (한국농어민신문)](http://www.agrinet.co.kr/news/articleView.html?idxno=147172)
- 논산 방울토마토: 외국인 3명 이탈 → 40동 중 8동 로터리·11동 방치, 영농조합 120농가 중 약 10곳 유사 피해, 일당 7~8만원 → 12~13만원 — [농민신문](https://www.nongmin.com/339767)
- 수확철 일당 15만원·웃돈 거래 — [농민신문 2021-11-05](https://www.nongmin.com/article/20211105346768)
- 농업 고용인력 지원 기본계획(2026~2030) 수립 — [제1차 농업고용인력 지원 기본계획 (농식품부, 2026.1)](https://www.mafra.go.kr/bbs/home/792/593792/download.do)

**운반·근골격 부담**
- 농진청: 운반은 단순 반복 작업, 사람이 직접 80kg 이상 나르면 안전사고 위험 증가 — [노지 작업자를 따라다니는 운반 로봇 (농사로 영상)](https://www.nongsaro.go.kr/portal/ps/psb/psby/vodPlay.ps?mvpNo=3265) (노지용 로봇 영상, 해당 로봇 적재 150kg)
- 농작업 중량물 작업은 대부분 수확 관련, 요추 부담; 참외·사과 수확 상자 20kg 안팎으로 권고 기준 초과; 수확 바구니·가방은 어깨·팔·허리 부담 — [농업인안전365 (농진청)](https://farmer.rda.go.kr/portal/menu3/PostureExercise.do?menuId=PS03466&m_id=9000_9051_51&mainCateNo=501011); [농축산기계신문](http://m.alnews.co.kr/news/articleView.html?idxno=5404); 허리 통증이 근골격계 질환 1위 — [농민신문 2025-07-23](https://www.nongmin.com/article/20250723500669)
- 농진청 온실용 작업자 추종 운반 로봇(2023.11): 3D 카메라+AI로 작업자와 0.1~1m 간격 유지, 집하장 하역 후 복귀, 최대 300kg·10시간 이상, 2023년 익산 토마토 농장 실증, 대당 약 2,500만원·약 2년 손익분기, 하루 작업량 200kg → 500kg·인력 절반 전망(개발자) — [중도일보 2023-11-29](https://m.joongdo.co.kr/view.php?key=20231129010009570); [머니투데이 2023-11-29](https://www.mt.co.kr/future/2023/11/29/2023112910124825042); [농민신문 2024-03-22](https://www.nongmin.com/article/20240322500556)
- 같은 로봇 현장 의견: 안전상 속도가 느림, 자율주행 유도선이 스티커라 쉽게 벗겨짐 — [농민신문 2024-03-22](https://www.nongmin.com/article/20240322500556)

**정보 전달·기록**
- 언어장벽이 작업지시·안전·임금 등 전 과정에 존재 — [다음뉴스 2026-05-03](https://v.daum.net/v/20260503103017506)
- 일본 3.2ha·100명+ 시설도 계획·진척관리 앱 미도입, 시프트 관리가 번잡 — [NARO E08](https://www.naro.go.jp/smart-nogyo/katsuyo-sanchi-shien/files/E08.pdf)
- 기온 상승 시 수확작업시간 증가 → 데이터 없으면 피크 대응 불가, 데이터 기반 노무관리로 피크 2~5할 저감 — [NARO 2016](https://www.naro.go.jp/project/results/4th_laboratory/nivfs/2016/16_035.html)
- 기록 없는 관리자의 진단 불리 — [Oklahoma State](https://extension.okstate.edu/fact-sheets/ipm-in-the-greenhouse-series-integrated-pest-management-in-commercial-greenhouses-an-overview-of-principles-and-practices)

**숙련도 편차**
- 한국 토마토 생산이력관리 실증: 작업자 개인별 포인트에서 확실한 변화, 여성 작업자 성취도가 매우 높음 → 개인 간 편차 존재 — [KISTI 보고서](https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202100010100)
- 일본: 작업속도 분석으로 연수·트레이닝 추진 — [NARO E08](https://www.naro.go.jp/smart-nogyo/katsuyo-sanchi-shien/files/E08.pdf)

**예찰·방제**
- 담배나방·굴파리 연중 발생, 예찰 어렵고 잦은 약제로 저항성 — [데일리안](https://m.dailian.co.kr/news/view/994236)

**수직농장**
- Bowery·Plenty 등 붕괴 원인은 에너지비·설비투자·저가 등 경제성 — [Agritecture](https://www.agritecture.com/blog/odyssey-teachings-about-vertical-farming)

### Inferences
- 농진청 추종 운반 로봇의 현장 피드백(느린 속도, 유도선 스티커 탈락)은 Robot B 설계 시 직접 반영할 요구사항: 유도선 비의존 측위(파이프레일·LiDAR·UWB), 작업자 보행속도 추종, 집하장 왕복 자율주행.
- "숙련도 편차"를 객관화하려면 개인별 kg/hr 데이터가 필요 → Robot B 기록 + Robot A의 숙도 지도(놓친 숙과 비율) 조합으로 "수확 품질(누락률)"까지 측정 가능.

### Gaps
- 한국 상업 온실 수확 작업의 기록 누락률·오기록 실태 정량 자료 없음.
- 시설 토마토·파프리카 수확·운반 특화 인간공학 연구(작업자세·운반거리)는 찾지 못함(일반 농작업 자료만).

---

## Q8. AS-IS 프로세스 단계표와 Robot A/B 기능 매핑 제안

### Takeaway
아래 표는 위 Q1~Q7의 인용 근거를 단계별로 재구성한 것이다. Robot A는 "예찰·수확 대상 판단·정보공유(①②⑩)", Robot B는 "수확 중 동행·적재 확인·운반·기록(③④⑤⑩)"에 대응하며, 선별·포장·저장·출하(⑥~⑨)는 APC/선별기로 이미 자동화가 진행 중이라 로봇의 직접 대상이라기보다 데이터 연계 대상이다.

### Cited Findings
(표 내 근거는 Q1~Q7의 인용 출처를 참조. 담당자·시간 칸의 "미확인"은 공개 근거 없음을 뜻함)

| # | 단계 | 담당(AS-IS) | 도구(AS-IS) | 빈도/시간(근거) | 정보 흐름(AS-IS) | 문제점(근거) |
|---|---|---|---|---|---|---|
| ① | 예찰(병해충) | 관리자/농장주(해외: 전담 scout) — 한국 실태 미확인 | 황색 끈끈이트랩(100주당 1개, 지상 50cm 이하/캐노피 위 2인치), 육안·흔들기 | 주 1~2회, 트랩 주 1회 교체·계수 (Oklahoma State, UConn) | 종이/엑셀 → 주간 요약 → 관리자 (Greenhouse Grower) | 연중 발생·예찰 어려움·약제 저항성(데일리안); 공간 해상도 낮음 |
| ② | 수확 대상 판단(숙도) | 수확 작업자 개인 판단 | 육안(색택; 파프리카 착색, 토마토 출하 85~90% 착색 등) | 수확 시 실시간 | 기록 없음 | 숙련도 편차(KISTI), 놓친 숙과 기록 없음 |
| ③ | 수확 | 외국인 근로자 중심(시설원예 외국인력 64%), 소농은 가족 | 가위/손, 파이프레일 수확대차 | 토마토 주 2~3회, 오이 주 3~4회~매일, 파프리카 연 48회; 토마토 노동의 29~32.6%; 맨손 22~30 kg/hr(시험) | 해외: 통로 변경 시 단말 로그인(Ridder); 한국: 구두 지시 | 일손 부족·이탈·일당 12~15만원(농민신문), 언어장벽 |
| ④ | 상자 적재 | 수확 작업자 | 대차 위 상자 8개(30×40) 또는 크레이트 4개(60×40) | 수확과 동시 | 해외: 크레이트 단위 등록(Ridder 딸기); 한국: 없음 | 상자 20kg 안팎 중량물·허리 부담(농업인안전365) |
| ⑤ | 대차 운반(통로→집하장) | 수확 작업자 | 수동 파이프레일 대차/손수레 | 왕복 반복(시간 미확인) | 없음 | 80kg 초과 수동 운반 시 사고 위험(농진청); 비생산 보행 시간 |
| ⑥ | 집하장 하역·계량 | 집하 담당/관리자 | 하역·계량 라인(대형: ~1,000상자/hr), 소농: 저울 | 미확인 | 계량값 수기/시스템; 해외는 작업자 등록과 결합 | 작업자·통로별 kg 연결 끊김 |
| ⑦ | 선별·포장 | 선별장 인력 or 농협 APC | 선별기(토마토 2만 개/hr, 딸기 10,800개/hr), 수선별 | 소농 포장 4~6시간/일(딸기 8시~14시, 토마토 4~5시간) | 농가별 식별번호·바코드(계열업체/APC) | 소형 품종 수선별 부담 |
| ⑧ | 예냉·저온저장 | 농장/APC | 저온저장고 | 수확 직후(파프리카 하절기) | 미확인 | 미확인 |
| ⑨ | 출하 | 농장주/APC/계열업체 | 상차, 저온 운송 | 미확인 | 출하량 기록(APC 자동 인식) | — |
| ⑩ | 기록(작업·수확·GAP) | 농장주 | 영농일지(수기/GAP 앱), 해외: Priva/Ridder, 일본: 작업관리 앱 | 일 단위 | 사후 기록 | 대규모 시설도 진척관리 앱 미도입(NARO), 언어장벽 |

### Inferences
**Robot A/B 매핑 제안 (TO-BE)**

| AS-IS 단계 | Robot A (예찰·숙도·병해충·자율주행·정보공유) | Robot B (추종 카트·디스플레이·적재 확인·기록) | 기대 개선(근거 기반 추론) |
|---|---|---|---|
| ① 예찰 | 수확 주기(주 2~3회)에 맞춰 통로 자율 순회, 병해충 영상 탐지, 트랩 판독, 통로/포스트 위치 태깅, 핫스팟 지도 | — | 예찰 빈도 주 1회 → 주 2~3회, 위치 해상도 온실/구역 → 통로·포기 |
| ② 수확 대상 판단 | 숙도 분류(착색 단계)·통로별 수확 예정량 추정 → "오늘 수확할 통로/예상 상자 수" 생성 | 디스플레이에 Robot A가 생성한 통로별 수확 대상·예상량 표시(다국어 아이콘) | 개인 판단 편차 축소, 인력 배치 사전 계획(일본 NARO 수확시간 예측과 동일 개념) |
| ③ 수확 | (수확 후) 재순회로 놓친 숙과 탐지 → 품질 피드백 | 작업자 추종(0.1~1m 간격 선례: 농진청), 작업자 ID 인식, 통로 진입/이탈 자동 기록(Ridder 단말 로그인 대체) | 단말 이동·로그인 제거, 개인별 kg/hr 자동 산출 |
| ④ 상자 적재 | — | 적재 확인(상자 카운트·중량 센서·비전), 오적재/과적 경고, 디스플레이 실시간 표시 | 크레이트 단위 등록 자동화(Ridder 딸기 기능의 이동체 버전) |
| ⑤ 대차 운반 | 공용 지도·경로 정보 공유 | 만재 시 집하장 자율 왕복(농진청 로봇 선례: 300kg, 10시간), 유도선 스티커 비의존 측위 | 작업자 보행·중량물 운반 제거, 하루 처리량 증대(농진청 개발자 전망 200→500kg) |
| ⑥ 집하장 계량 | — | 하역 시 작업자·통로·상자 수 데이터를 계량값과 매칭 | 작업자·통로별 kg 연결 복원 |
| ⑦~⑨ 선별~출하 | (선택) 통로별 수확 예측을 APC/선별장 작업계획에 공유 | 수확 로트 ID 생성 → APC 농가 식별번호·바코드와 연계 | 이력추적 해상도 향상(농가 단위 → 통로·일자 단위) |
| ⑩ 기록 | 예찰 기록·방제 이력 자동 축적(GAP 증빙) | 작업·수확 기록 자동 생성, 영농일지/GAP 앱 내보내기 | 기록 누락 제거, 표준시간·성과관리 데이터 확보(네덜란드식 폐루프) |

- 설계 요구사항 시사점(추론): (a) Robot B 디스플레이 = 다국어·아이콘 중심(외국인 64%, 언어장벽), (b) 측위 = 파이프레일/LiDAR 기반, 스티커 유도선 회피(농진청 현장 피드백), (c) 데이터 스키마 = {작업자, 통로, 시작·종료시각, 상자 수, kg, 숙도분포, 병해충 이벤트} — 일본 ASHIGARUWARE·Ridder Productive 항목과 호환, (d) 공정성: 개인 실적이 임금·평가에 연동될 수 있으므로(일본 사례) 카운트 정확도·이의제기 기능 필요.

### Gaps
- 표의 ⑤⑥⑧⑨ 단계 소요시간, ① 담당자(한국), ③ 통로 배정·성과급 실태는 공개 근거 없음 → 현장 인터뷰(대형 토마토·파프리카 농장 2~3곳, 농협 APC 1곳) 및 시간동작 측정(stopwatch study)으로 보완 필요.
- 수직농장의 단계표는 별도 작성이 필요하나(파종·이식·베드 이송·수확 스테이션·포장 라인), 국내 업체 공정 공개 자료가 없어 이번 조사에서 단계별 수치 미확보.
