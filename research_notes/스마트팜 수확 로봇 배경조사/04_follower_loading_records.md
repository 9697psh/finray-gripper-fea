# Robot B: 작업자 추종·정보 표시 및 수확물 적재 확인·이력 기록의 필요성

> 범위: 온실/수직농장 및 과채류 수확. 2018–2026 자료 우선. 출처 제목은 영어 원문 유지.
> 주의: 상당수 수치는 업체 자료(Burro, Ridder, Hectre, Croptracker 등)이며 독립 검증되지 않음. 각 항목에 표시함.

---

## Q1. 수확물 운반에 드는 시간·노동력과 작업자 신체 부담

### Takeaway
수확 중 운반·보행은 생산적이지 않은 시간의 큰 부분을 차지한다. 딸기에서는 보행 시간이 수확 시간의 최대 22%로 측정됐다. 국내 농업인 업무상 질병의 약 85%(2020)에서 90% 이상(2026 언급)이 근골격계 질환이며, 그 원인에 중량물 취급과 반복 동작이 포함된다. 운반 자동화가 필요하다는 정량 근거는 충분하다. 다만 국내 시설과채에서 운반 비중과 상자 무게를 직접 잰 자료는 찾지 못했다.

### Cited Findings
- 딸기 수확에서 보행(운반 포함) 시간은 전체 수확 시간의 최대 22%로 측정됨(Peng et al.이 선행연구를 인용). — [A strawberry harvest-aiding system with crop-transport co-robots: Design, development, and field evaluation (arXiv 2107.13063, J. Field Robotics 2022)](https://arxiv.org/pdf/2107.13063.pdf)
- 2020년 농업인 업무상 질병 조사(농진청, 표본 10,020가구 면접, 격년 국가승인통계): 휴업 1일 이상 업무상 질병 유병률 5.0%. 이 중 근골격계 질환 유병률이 4.4%로 가장 높고 업무상 질병의 84.6%를 차지함. — [농촌진흥청, 2020년 농업인 업무상 질병 조사 결과 발표 (위키트리 보도)](https://www.wikitree.co.kr/articles/658268)
- 같은 조사에서 근골격계 질환 부위는 허리 47.3%, 무릎 27.3%, 어깨 6.9% 순. 원인은 장시간 근무 27.6%, 반복 동작 22.8%, 불편한 자세 16.8%, 과도한 힘 또는 중량물 취급 13.0%. 여성 유병률 5.8%로 남성 4.3%보다 높음(근골격계는 여 5.2%, 남 3.7%). — [위키트리 보도](https://www.wikitree.co.kr/articles/658268)
- 농진청 웹진(2026년 3월호)은 "농업인 업무상 질병 가운데 근골격계 질환은 90% 이상을 차지한다"고 서술함. 근거 조사 연도는 명시되지 않음. — [RDA 웹진 March 2026 Vol.247](https://rda.go.kr/webzine/2026/03/1_2.html)
- 파프리카 대규모 온실 실증: 순치기·수확·유인이 전체 작업시간의 91% 이상을 차지하고, 유인·순치기 시간이 수확의 약 2배. 운반 시간은 따로 나누지 않음. — [KAIS 2023 추계 포스터 (2023_autumn_136)](https://www.kais99.org/jkais/springNfall/autumn2023/poster/2023_autumn_136.pdf)
- 농진청 온실 운반로봇 소개에서 농가는 "온실 작업 중 가장 노동력이 많이 드는 수확, 운반 작업"을 로봇과 함께 할 수 있다는 기대를 밝힘(정성적 근거). — [머니투데이방송 2023.11.29](https://news.mtn.co.kr/news-detail/2023112910034398548/share-modal)
- 온실 실측 생산량은 파프리카 약 4.1–4.3 kg/주, 토마토 약 16.2 kg/주(운반 물량 추정용 참고치). — [koreascience JAKO201333959964342](https://koreascience.kr/article/JAKO201333959964342.pdf)

### Inferences
- 토마토는 주당 약 16 kg을 생산한다. 그러면 1,000주 규모의 온실에서도 작기 동안 십여 톤 단위의 수확물을 사람이 상자에 담아 끌거나 들어서 옮겨야 한다. 허리·무릎에 집중된 근골격계 부담을 줄이는 데 운반 대행이 직접 기여할 수 있다.
- 딸기 노지 데이터(보행 최대 22%)를 온실 고설·과채 재배에 그대로 적용하기는 어렵다. 그래도 "수확 시간의 1/5 안팎이 비생산 보행"이라는 규모감은 요구사항의 근거로 쓸 수 있다.

### Gaps
- 국내 토마토·파프리카 온실에서 수확 작업 중 운반이 차지하는 시간 비율을 측정한 자료는 찾지 못함. 농진청 표준 작업시간 자료나 KREI 농산물 생산비 조사의 원문 확인이 필요함.
- 수확상자 표준 무게(예: 토마토 10 kg 상자, 수확 컨테이너 만재 시 15–20 kg)를 1차 출처로 확인하지 못함. 브리프에 적힌 "10–20 kg"은 미검증 값임.
- 근로복지공단 산재 통계(농업 분야 업무상 질병 건수)는 조사하지 못함.

---

## Q2. 작업자 추종 운반로봇 사례와 생산성 효과

### Takeaway
협동 운반로봇이 작업자 생산성을 약 10%(독립 논문)에서 20–48%(업체 주장) 높인다는 보고가 있다. UC Davis 현장시험에서는 비생산 시간이 60% 줄었다. 국내에서는 농진청이 온실용 작업자 추종 운반로봇(300 kg 적재, 추종거리 0.1–1 m, 인식 정확도 97.6%)을 개발해 실증하고 기술이전까지 마쳤다. 다만 노동시간 절감률은 공개하지 않았다.

### Cited Findings
- **UC Davis (Peng, Vougioukas 등, J. Field Robotics 2022)**: 상업 딸기농장 현장평가. 빈 트레이와 만재 트레이를 나르는 co-robot을 로봇 1대당 작업자 3명(1:3) 비율로 운용한 결과, 평균 수확 효율 약 10% 향상, 평균 비생산 시간 60% 감소. 예측형 확률적 스케줄링으로 기대 비수확 시간을 최소화함. — [arXiv 2107.13063](https://arxiv.org/pdf/2107.13063.pdf); [CDC stacks 사본](https://stacks.cdc.gov/view/cdc/230128)
- **시뮬레이션(Seyyedhasani, Peng, Jang, Vougioukas 2020)**: 작업자 25명 기준으로 효율이 약 82%/78%(오전/오후)에서 로봇 5대 투입 시 92%/86.5%로 상승. 로봇이 5대를 넘으면 작업자에게 이동하는 시간 때문에 효율 향상이 멈춤. 트레이가 찼는데 로봇이 아직 오지 않으면 대기 지연이 생긴다는 한계도 지적함. — [arXiv 2107.13063 (관련연구 인용)](https://arxiv.org/pdf/2107.13063.pdf)
- **Burro (Augean Robotics), 업체 주장**: 2019년 California Table Grape Commission과 시험했을 때 단일 행에서 수확량 +25%, 여러 행을 더 많은 인원으로 수확할 때 +42%. — [Burro Generation 6 Order Form](https://forms.gle/XYMt9y3MeMgtQced8)
- Burro 2021 Series A($10.9M) 보도: Burro 1대가 6명 이상과 함께 일하며 하루 최대 48% 더 수확한다는 주장. — [Robotics 24/7: Burro Raises $10.9M Series A](https://www.robotics247.com/article/burro_raises_10_9m_series_a_commercialize_collaborative_agricultural_robot)
- Burro 감귤 수확: 1대당 작업자 4–6명 조합으로 생산성 30% 향상(업체 블로그). — [Harvesting with Ease: The Burro Solution for Citrus Farms](https://medium.com/goodburro/harvesting-with-ease-the-burro-solution-for-citrus-farms-5809feb0745f)
- Burro Gen 8.2에 대해 작업자 생산성 20–30% 향상이라는 2차 요약(제3자 제품 소개, 신뢰도 낮음). — [AgTecher: Burro Generation 8.2](https://agtecher.com/robotics/burro-generation-8-2-cutting-edge-collaborative-robo)
- **농촌진흥청 온실용 작업자 추종 운반로봇(2022 개발, 2023 실증)**: 작업자를 따라가며 수확물을 집하장까지 옮기고 하역장에서 자동으로 내림. 전방 3D 카메라와 AI 제어기로 작업자와의 거리를 0.1–1 m 사이에서 조절함. 1회 최대 300 kg 적재, 10시간 이상 연속 작동. 전북 익산 토마토 농장에서 실증했으며 영상 인식 정확도 97.6%, 특허 등록 및 산업체 기술이전 완료. — [머니투데이방송 2023.11.29](https://news.mtn.co.kr/news-detail/2023112910034398548/share-modal)
- 농진청 온실 로봇 통합관리 프로그램(2025.4): 방제·운반·모니터링 로봇 3종을 PC나 휴대전화로 연계해 관리하고 작업 정보를 디지털화함. 기사 제목의 "방제 시간 40%, 인건비 1,200만 원 감소"는 방제로봇 수치이며 운반로봇 수치가 아님. — [다음/데일리안 2025.04.23](https://v.daum.net/v/20250423140015179); [데일리안](https://www.dailian.co.kr/news/view/1489173)
- 농진청 과수원용 운반로봇(2024): 작업자를 따라 수확물과 농기구를 옮긴 뒤 집하장 등 지정 위치로 스스로 이동하는 셔틀 기능을 탑재함. — [뉴스토마토: 초고령화 농촌…농작업 로봇 시대 연다](https://newstomato.com/ReadNews.aspx?no=1235506)

### Inferences
- 독립 논문 수치(+10% 효율, 비생산 시간 −60%)는 보수적인 근거로, 업체 수치(+20–48%)는 상한 시나리오로 쓰는 것이 적절하다.
- 로봇 대수를 늘려도 효율 향상이 멈춘다는 시뮬레이션 결과로 보아, Robot B 기획에서는 "1대당 작업자 수"와 "만재 시 하역장 왕복 중 공백"을 줄이는 운용 설계(셔틀 복귀, 대기 최소화)가 핵심 요구사항이 된다.
- 농진청 로봇의 추종거리 0.1–1 m와 자동 하역 기능은 국내 온실 환경에서 이미 검증된 기준선이다. Robot B는 여기에 정보 표시와 적재 기록을 더하는 차별화가 필요하다.

### Gaps
- 농진청 운반로봇의 노동시간·인건비 절감률은 공개 자료에서 찾지 못함.
- 대동, LG 등 국내 기업의 추종형 운반로봇, Thorvald(Saga Robotics), Naio, Kubota의 운반 성능 수치는 이번 조사에서 확인하지 못함.
- 온실(고설·레일 파이프 환경)에서 측정한 Burro류 효과는 없음. 위 수치는 대부분 노지 포도·딸기·감귤 기준임.

---

## Q3. 작업자-로봇 안전거리와 안전 규격

### Takeaway
작업자 곁에서 움직이는 운반로봇은 ISO 3691-4:2023(무인 산업용 트럭/AMR)의 적용 대상이다. 이 규격은 인원 감지, 속도 연동 보호필드, 감지 비활성 구간 저속 같은 요구사항을 정한다. 다만 정확한 수치는 규격 원문으로 확인해야 한다. 온실 추종로봇의 실용 추종거리 기준으로는 농진청 로봇의 0.1–1 m가 유일한 국내 사례로 확인됐다.

### Cited Findings
- ISO 3691-4:2023(제2판, 2023년 6월 발행, 2020년판 대체)은 항법 방식과 관계없이 무인 산업용 트럭(AGV, AMR 포함)에 적용됨. — [Fabrico: ISO 3691-4 Driverless Industrial Trucks](https://www.fabrico.io/blog/iso-3691-4-driverless-industrial-trucks/)
- 인원이 있는 운행구역에서는 인원 감지가 필요하고, 경로상의 사람과 접촉하기 전에 정지해야 함. 감지 시험체는 수직 원통(직경 200 mm, 높이 600 mm)과 바닥에 놓인 수평 원통(직경 70 mm, 길이 400 mm). — [Fabrico (2차 자료)](https://www.fabrico.io/blog/iso-3691-4-driverless-industrial-trucks/); [TÜV Rheinland AGV whitepaper 2021](https://tuv.com/content-media-files/master-content/services/industrial-services/pdf/tuv-rheinland-automated-guided-vehicle-whitepaper-2021.pdf)
- 보호필드 길이는 감지부터 정지까지 이동하는 거리 이상이어야 하며 속도에 따라 필드 세트를 전환함. 1.5 m/s AMR이면 약 1.3 m라는 업체 계산 예시가 있음(규격 공식이 아닌 예시). 감지를 비활성화하는 도킹 등의 상황에서는 0.3 m/s로 제한한다는 서술이 있음(단일 블로그 출처, 원문 확인 필요). 안전 제어 신뢰성은 ISO 13849-1, 안전 레이저스캐너는 IEC 61496을 참조함. — [Fabrico](https://www.fabrico.io/blog/iso-3691-4-driverless-industrial-trucks/); [ISO 3691-4 Deep Dive (개인 기술 노트, 신뢰도 낮음)](https://kvynlim.github.io/industry-research/60-safety-validation/standards-certification/iso-3691-4-deep-dive)
- EU에서는 기계규정 (EU) 2023/1230이 2027년 1월부터 기계지침을 대체함. — [Fabrico](https://www.fabrico.io/blog/iso-3691-4-driverless-industrial-trucks/)
- 농진청 온실 추종로봇의 작업자-로봇 거리 0.1–1 m(3D 카메라와 AI 제어). — [머니투데이방송 2023.11.29](https://news.mtn.co.kr/news-detail/2023112910034398548/share-modal)

### Inferences
- 추종거리 0.1–1 m는 ISO 3691-4의 속도 연동 보호필드 개념에 비춰 보면 매우 저속에서만 성립한다. Robot B 요구사항에는 "추종 모드 최대속도 제한 + 보호필드/경고필드 이중화 + 작업자 정지 시 즉시 정지"를 명시하는 것이 타당하다.
- 브리프에 있는 ISO 13482(개인 돌봄 로봇)와 ISO/TS 15066(협동 매니퓰레이터)는 운반 플랫폼의 주 규격이 아니다. 운반 본체는 ISO 3691-4가, 농업 자율기계 측면은 ISO 18497이 더 직접 관련된다. ISO 18497은 이번 조사에서 미확인이다.

### Gaps
- ISO 3691-4 원문의 보호필드 산정식, 속도 한계, 감지 성능 등급(PL) 요구치를 1차 출처로 확인하지 못함(유료 규격).
- 농업용 추종/운반 로봇과 작업자의 충돌 사고 사례 통계는 찾지 못함.
- ISO 18497(농업기계 자율운전 안전) 및 국내 농업용 로봇 안전 인증 기준은 미조사.

---

## Q4. 다수 작업자 환경의 추종 대상 식별(re-ID) 문제

### Takeaway
여러 작업자가 같은 작업복을 입고 작물에 가려지는 환경에서는 비전 기반 추종이 가림(occlusion)과 유사 외형 방해자 때문에 대상을 잃는 것이 가장 큰 실패 요인이다. UWB는 거리 측정에는 유용하지만 각도 오차가 커서 단독으로 쓰기 어렵다. 그래서 비전+UWB 융합과 온라인 재식별이 주요 해법으로 연구되고 있다.

### Cited Findings
- UWB 송수신기로 사람을 추적할 수는 있으나 각도 오차가 큼. 비전과 UWB를 융합해 단일 센서의 약점을 보완하는 접근. — [Springer J. Intell. Robot. Syst. (s10846-023-02037-4)](https://link.springer.com/content/pdf/10.1007/s10846-023-02037-4.pdf)
- 단안 카메라는 시야가 제한되어 대상이 부분적으로 가려지는 문제가 생김. 검출, 추적, 식별(외형 모델 기반 re-ID), 제어를 분리한 파이프라인을 제안함. — [Robot Person Following Under Partial Occlusion (arXiv 2302.02121)](https://arxiv.org/pdf/2302.02121)
- 기존 재식별은 오프라인으로 학습한 특징과 단기 경험에 의존해, 가림 이후 외형이 비슷한 방해자를 구별하는 데 취약함. 온라인 지속학습으로 이를 보완함. — [Person Re-Identification for Robot Person Following (arXiv 2309.11727)](https://ar5iv.labs.arxiv.org/html/2309.11727)
- 기존 방법은 부분 또는 완전 가림 뒤 재식별의 강건성이 부족함. — [CARPE-ID (arXiv 2310.19413)](https://arxiv.org/pdf/2310.19413v1)
- 과수원 환경에는 심한 잎 가림, 배경 유사성, 급격한 조도 변화가 흔함. DIMP 추적기와 EfficientNet 기반 re-ID를 결합한 DeepDIMP-ReID는 재식별 상황에서 대상 판별 성공률 93.3%를 기록함. — [MDPI Mach. Learn. Knowl. Extr. 8(2):39](https://www.mdpi.com/2504-4990/8/2/39)
- 농업용 추종로봇에서 KCF 추적기는 장애물 가림에 대한 강건성이 낮음. — [MDPI Horticulturae 10(4):348](https://mdpi.com/2311-7524/10/4/348/xml)
- 농진청 온실 추종로봇의 영상 인식 정확도는 97.6%(실증 단계). — [머니투데이방송](https://news.mtn.co.kr/news-detail/2023112910034398548/share-modal)

### Inferences
- 성공률 93.3–97.6%를 뒤집어 보면, 작업 중 수십 번의 가림 상황에서 몇 차례 대상을 잃거나 잘못 바꿀 수 있다. 다수 작업자 온실에서는 "추종 대상 등록(페어링) + 대상 상실 시 정지·재확인"이 필수 요구사항이다.
- 온실 통로는 폭이 좁아(두 행 사이) 작업자 간 교차가 잦다. 그래서 UWB 태그로 ID를 확정하고 비전으로 방향과 거리를 정밀하게 잡는 융합 구조가 합리적이다(추론).

### Gaps
- 온실 금속 구조물(레일 파이프, 철골) 환경에서 UWB 다중경로 오차를 측정한 자료는 찾지 못함.
- 같은 작업복을 입은 다수 작업자 조건에서 추종 대상 오전환율을 측정한 농업 현장 데이터는 없음.

---

## Q5. 디스플레이를 통한 수확 대상·병해충 정보 제공의 이점

### Takeaway
물류 피킹 연구에서는 작업자 옆에 시각 정보를 보여주는 방식(카트 장착 디스플레이, HUD)이 종이 목록이나 pick-by-light보다 속도, 정확도, 작업부하 모든 지표에서 우수하다는 근거가 있다. 국내 농업은 외국인 노동자가 2020년 약 2만 명에서 2025년 약 13만 명으로 늘면서 작업 지시 전달 문제가 공식 정책 과제가 되었다. 로봇에 단 디스플레이로 작업 지시를 시각화하는 방안의 근거로 쓸 수 있다.

### Cited Findings
- Guo et al.(ISWC 2014)은 HUD, 카트 장착 디스플레이(CMD), pick-by-light, 종이 목록을 비교함. HUD와 CMD가 정확도, 작업시간, 주관적 작업부하 모든 지표에서 종이와 pick-by-light보다 우수했음. — [A comparison of order picking assisted by head-up display (HUD), cart-mounted display (CMD), light, and paper pick list (dblp)](https://dblp.org/rec/conf/iswc/GuoRXILSGBSS14.html); [Unpaywall DOI 10.1145/2634317.2634321](https://unpaywall.org/10.1145%2F2634317.2634321)
- 후속 RF-pick(2018): HUD에 웨어러블 RFID 검증을 더한 방식이 피킹 속도가 유의하게 빠르고 오류율과 작업부하가 가장 낮았음. — [RF-pick: comparing order picking using a HUD with wearable RFID verification to traditional pick methods](https://athena.westpoint.edu/items/1bae5be4-8097-4ee4-846d-eb0f729f6d75)
- OrderPickAR(LMU, 프로젝터 장착 카트): 종이, 음성, pick-by-vision보다 약 2배 빠르고 오류율을 최대 9배 낮춤. — [Funk et al., Pick from here! (LMU)](https://www.medien.ifi.lmu.de/pubdb/publications/pub/funk2015pickfrom/funk2015pickfrom.pdf)
- 반대 근거: 31명 소규모 실험에서는 pick-to-light와 종이 사이에 오류의 유의차가 없었음. — [Logistics & Sustainable Transport (Feb 2020), DOAJ](https://doaj.org/article/5c9cd7c3513f4298a268690bfc50b28f)
- 국내 농업 외국인 노동자는 2020년 20,738명, 2024년 85,292명, 2025년 130,259명으로 늘었으며 증가는 계절근로자가 주도함. — [헤럴드K 2026.04.29](https://www.heraldk.com/article/2026042913312256366)
- 농식품부(2026.4)는 언어·문화 차이로 의사소통, 작업 지시, 안전수칙 안내가 어렵고 이것이 작업 효율 저하와 안전사고 위험으로 이어진다고 보고, 8개 언어 농작업 용어 포켓북(QR 음성 지원)을 배포함. — [헤럴드K 2026.04.29](https://www.heraldk.com/article/2026042913312256366)
- 경기도 계절근로자 인권 실태조사(2025.12): 계절근로자는 한국어 시험 절차가 없음. 근로계약서 내용을 '아주 잘 안다'는 응답은 54.4%(162명)에 그침. — [뉴시스 2025.12.11](https://www.newsis.com/view/NISX20251211_0003436935)

### Inferences
- 근로계약서조차 절반가량만 충분히 이해한다는 조사 결과로 보아, 숙도 판정이나 병해충 증상 식별 같은 현장 판단을 말로 전달하는 방식은 한계가 크다. 로봇 디스플레이로 "이 행에서 수확할 대상(예: 착색 단계 사진) / 발견된 병해충 위치와 사진"을 다국어·아이콘으로 보여주면 교육 부담을 줄일 수 있다.
- 카트 장착 디스플레이(CMD)가 우수하다는 Guo et al.의 결과는 작업자를 따라오는 로봇의 디스플레이와 구조적으로 같다. 그래서 물류 연구를 유추 근거로 쓸 수 있다. 다만 농업 현장에서 효과를 직접 측정한 연구는 없다.

### Gaps
- Guo et al. 2014의 정확한 오류율과 시간 수치는 원문을 확인하지 못함.
- 농업 수확 작업에서 시각적 작업 지시(디스플레이, AR)가 수확 정확도(미숙과·과숙과 오수확률)에 미치는 효과를 측정한 연구는 찾지 못함.
- 병해충 정보를 작업자에게 실시간으로 제공했을 때 조기 방제 효과를 정량화한 자료는 없음.

---

## Q6. 기존 수확물 적재·수확량 관리 방식과 문제점(누락·중복·오류)

### Takeaway
과수·딸기 등에서는 아직 손으로 쓴 빈 태그, 공책 집계, 따로 관리하는 장부가 흔하다. 이 때문에 작업자 이름이 잘못 기재돼 성과급이 엉뚱한 사람에게 지급되거나, 기록끼리 맞지 않고, 급여일에 분쟁이 생기는 문제가 보고된다. 다만 오류율을 정량적으로 측정한 독립 연구는 찾지 못했다.

### Cited Findings
- Kono Horticulture(NZ 과일 수출업체): Hectre 도입 전에는 모든 빈 태그를 손으로 쓰고 태그 꼬리표를 보관해 빈 수를 셌음. 태그에 다른 이름이 적혀 엉뚱한 작업자에게 임금이 지급된 사례가 있었음. 도입 후 성과급 보고서를 몇 초 만에 만들고, 급여 업무를 주당 최소 1시간 절감함(업체 사례). — [Hectre Case Study: Kono Horticulture](https://hectre.com/case-studies/kono-horticulture/)
- 다른 Hectre 고객 후기: 빈 티켓 세기, 재입력, 오류 정정을 없애 주당 약 4–6시간 절감(업체 후기). — [Hectre: Efficiency and traceability – the advancements in bin tagging technology](https://hectre.com/blog/efficiency-and-traceability-the-advancements-in-bin-tagging-technology/)
- Croptracker는 전형적인 종이 체계를 수확량 집계, 성과급 급여, 빈 티켓, 품질검사 시트가 서로 다른 곳에 있고 대조되지 않는 상태로 묘사함. 작업자별 공책 집계는 급여일 분쟁으로 이어진다고 함(업체 자료). — [Croptracker: Piece rate tracking for harvest](https://croptracker.com/blog/piece-rate-tracking-for-harvest.html); [Croptracker use case: bucket and bin productivity and inventory tracking](https://www.croptracker.com/blog/croptracker-use-case-bucket-and-bin-productivity-and-inventory-tracking.html)
- Ridder: 행, 수확 트롤리, 펀넷이나 상자에 붙은 NFC 태그를 스캔하면 실수 위험이 크게 줄어든다고 함. 처음에는 행 단위였다가 딸기 농가를 위해 상자 단위 등록을 추가함(업체 자료). — [hortidaily: Labor management system even more widely applicable after update](https://www.hortidaily.com/article/9811091/labor-management-system-even-more-widely-applicable-after-update)
- Greenhouse Grower: 대부분의 시설은 아직 완전한 수확 데이터를 수집하지 못하고 있음. — [The Evolution of Smart Sales Forecasting for Greenhouse Operations](https://greenhousegrower.com/management/the-evolution-of-smart-sales-forecasting-for-greenhouse-operations/)

### Inferences
- 수기 기록의 핵심 문제는 세 가지다. ① 누가(작업자 귀속 오류), ② 얼마나(상자 수 누락·중복), ③ 어디서(행·구역 정보 부재). Robot B가 적재 순간 무게, 작업자 ID, 위치를 함께 자동으로 기록하면 세 가지를 동시에 해결할 수 있다.
- 국내 시설과채 농가도 외국인 근로자 비중이 커지면서 작업자별 실적 집계와 성과 관리 수요가 커질 것으로 보인다(추론, 국내 성과급 제도 실태는 미확인).

### Gaps
- 수기 수확 기록의 오류율(누락·중복 %)을 측정한 독립 연구는 찾지 못함. 모두 업체 사례의 일화적 서술임.
- 국내 온실 농가의 수확량 기록 방식(수기, 엑셀, 스마트팜 앱) 실태조사 자료는 찾지 못함.
- 국내 시설원예에서 성과급(piece-rate) 적용 실태 자료는 없음.

---

## Q7. 적재 확인과 지정 적재 위치(품종·등급·구역) 구분의 필요성

### Takeaway
선진 온실 노무 시스템은 트롤리, 행, 상자 단위로 수확물을 위치(10 cm 정밀도)와 작업자에 연결해 등록한다. 이력추적제도도 생산 단계부터 단계별 정보 기록을 요구한다. 따라서 "어느 구역/품종/등급 수확물이 어느 적재 위치에 실렸는가"를 확인하는 기능은 추적성과 품질 관리의 기본 요건이다.

### Cited Findings
- Ridder CoRanger Productive: 작업자와 트롤리에 실내 측위 태그를 달아 스캔 없이 위치를 등록함. 작업자, 수확 카트 등의 위치를 10 cm 정확도로 기록함. 2021년 초 네덜란드 토마토 농가 Duijvestijn의 신축 10 ha 온실 전체에 도입됨. 업체는 수확·노무 등록의 품질과 신뢰성 향상, 비용과 시간 절감을 주장함. — [Ridder CoRanger Productive Brochure EN](https://ridder.com/wp-content/uploads/2021/11/Ridder-CoRanger-Productive-Brochure-EN.pdf); [CoRanger Productive: Seamless Works](https://ridder.com/ridder-coranger-seamless-works/)
- 법령상 이력추적관리는 "농산물을 생산단계부터 판매단계까지 각 단계별로 정보를 기록·관리하여" 안전성 문제가 생기면 추적해 원인을 밝히고 조치할 수 있도록 하는 제도로 정의됨(구 농산물품질관리법 기준). — [대한민국 농산물품질관리법 (위키문헌)](https://ko.wikisource.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD_%EB%86%8D%EC%82%B0%EB%AC%BC%ED%92%88%EC%A7%88%EA%B4%80%EB%A6%AC%EB%B2%95)
- 현행 「농산물이력추적관리제도 세부실시요령」(국립농산물품질관리원 고시) 개정안은 2026년 7월 6일 시행. 근거는 「농수산물 품질관리법」 제24–27조와 시행규칙 제46–54조이며 과태료 규정을 포함함. — [law.go.kr 고시 첨부](https://www.law.go.kr/LSW/flDownload.do?flSeq=166795611)
- 일본 NARO 연구: 바코드와 카트 장착 장치로 생식용 온실 토마토의 수확량과 수확 시간을 기록하는 시스템을 개발함. 가공용 토마토 수확기의 수량 모니터는 손 수확 생식용에 쓸 수 없다고 지적함. — [NARO postprint SC10201902190024](https://repository.naro.go.jp/record/3369/files/NARO_SC10201902190024_postprint-a.pdf)

### Inferences
- 온실 한 동 안에서도 품종, 구역(블록), 등급(정품·비품)이 섞여 수확된다. 적재 위치를 구분하지 않으면 출하 단계에서 다시 선별해야 하고 이력추적 단위가 흐려진다. Robot B 적재함을 구획하고 각 구획의 적재 여부를 감지하는 것은 이 문제를 직접 해결한다(추론).

### Gaps
- 이력추적 등록 농가가 수확 단계에서 기록해야 하는 구체 항목(수확일, 필지, 수량)과 GAP 기록 요건의 원문은 확인하지 못함.
- 국내 스마트 APC의 입고 단계 이력 연계 사례와 수치는 이번 조사에서 확인하지 못함.

---

## Q8. 자동 기록(무게센서·RFID/NFC·비전) 기반 수확 이력과 데이터 활용

### Takeaway
네덜란드 온실은 NFC 스캔과 로드셀 카트 계량으로 작업자별 수확량을 자동 집계해 임금 산정에 쓰고 있다. 수확 무게 데이터는 AI 수확량 예측의 입력으로도 활용된다(업체 주장 정확도 85–90%, 최대 8주 앞). 다만 자동 기록 도입 전후 효율을 독립적으로 검증한 연구는 없다.

### Cited Findings
- Meer Camp(네덜란드 토마토): 휴대폰 NFC 스캔으로 작업 활동을 기록하고 로드셀로 수확 카트를 계량해 작업자별 수확량을 정확히 집계함. 이를 임금과 연동함. — [HBK case study: Meer Camp registration system and weighing modules](https://www.hbkworld.com/en/knowledge/resource-center/case-studies/meercamp-registration-system-and-weighing-modules-provide)
- Priva 노무 시스템: 온실용 모바일 단말과 고정 스테이션으로 운용. 한 농가는 10년간 사용하며 투입 시간과 노무 예산 대비 진척을 관리한다고 밝힘. 노지 딸기용 클라우드 제품은 작업자별 작업시간, 생산량, 성과를 제공함. — [hortidaily: Overview increasingly important in large company](https://www.hortidaily.com/article/6003298/overview-increasingly-important-in-large-company); [hortidaily: High labour costs growing concern for soft fruit growers](https://www.hortidaily.com/article/6031974/high-labour-costs-growing-concern-for-soft-fruit-growers)
- Croptracker: 버킷이나 빈 단위 작업자 산출을 급여와 연결하고 최저임금 보전 계산을 자동화함(업체 자료). — [Croptracker: Piece rate tracking for harvest](https://croptracker.com/blog/piece-rate-tracking-for-harvest.html)
- 토마토 수확은 여전히 수작업 중심임. 무게 자동 측정과 작업시간 기록 시스템이 제안되어 왔지만, 대부분의 머신러닝 수확량 예측은 수확량과 작업시간의 관계를 반영하지 않음. — [ProQuest 3149494652 (학술 논문)](https://www.proquest.com/docview/3149494652)
- Greenhouse Grower: 무게 데이터, 작물 등록, 기후 데이터를 결합하면 예측이 좋아지고, AI가 등록 작업을 자동화하면 숙련 인력의 부담을 덜 수 있다고 봄. — [Greenhouse Grower](https://greenhousegrower.com/management/the-evolution-of-smart-sales-forecasting-for-greenhouse-operations/)
- Source.ag(Source Cultivate)는 최대 8주 앞까지 예측 정확도 85–90%를 주장함(업체 주장). 같은 기사는 현재 데이터로 4–8주 앞을 정확히 예측하기 어렵다고도 언급함. — [Greenhouse Management: Leveraging AI to unlock the potential of yield forecasting for tomatoes](https://www.greenhousemag.com/news/leveraging-ai-forecasting-tomato-yield-source-ag)
- Source Scan App(2026년 3월): 휴대폰으로 상자 무게와 과실 수를 입력해, 추정 대신 실측 과중을 예측에 반영함. — [Source.ag: Introducing Scan App](https://www.source.ag/product-updates/introducing-scan-app-a-new-way-to-capture-your-harvest-data)
- 농진청 통합관리 프로그램은 운반로봇을 포함한 로봇의 작업 정보를 디지털화해 관리함. — [데일리안 2025.04](https://www.dailian.co.kr/news/view/1489173)

### Inferences
- 업계는 수동 스캔(NFC/QR)에서 무스캔 측위(CoRanger)와 계량 카트(Meer Camp)로 옮겨가고 있다. Robot B는 운반 플랫폼 자체에 로드셀, 작업자 ID, 위치를 통합해 별도 스캔 장비나 계량 스테이션 없이 같은 데이터를 만들 수 있다. 이 점이 차별화 포인트다(추론).
- 행·구역별 수확 무게 시계열은 수확량 예측 모델의 실측 입력이 된다. 업계는 이 데이터가 없는 것을 예측 정확도의 병목으로 지목하고 있다.

### Gaps
- 자동 기록 도입 전후 노무 관리 시간과 오류율 변화를 측정한 독립 연구는 찾지 못함. Ridder, Priva, Hectre, Croptracker 수치는 모두 업체 주장이거나 일화임.
- FarmERP, 국내 스마트 APC, 국내 스마트팜 플랫폼의 수확 이력 기능과 효과 수치는 미조사.
- 비전 기반 적재 확인(상자 인식, 과실 계수) 정확도에 관한 농업 현장 데이터는 이번 조사에서 확인하지 못함.
