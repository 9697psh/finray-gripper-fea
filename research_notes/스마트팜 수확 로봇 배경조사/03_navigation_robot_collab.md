# 온실·수직농장 내 자율주행 및 로봇 간(예찰 로봇 A ↔ 작업자 추종 운반 로봇 B) 실시간 정보 공유의 필요성과 기대효과

> 조사 방법 메모: 이번 세션에서는 WebFetch가 네트워크 정책으로 막혀(doi.org, v.daum.net 접근 불가) 원문 전체를 읽지 못했다. 아래 수치는 **WebSearch 결과에 나온 원문 발췌/요약**을 근거로 했다. 보고서에 인용하기 전에 핵심 수치(특히 ★ 표시)는 원문 확인을 권장한다.

---

## 1. 농장(온실·수직농장) 내부 이동·작업 동선의 비효율: 이동·운반 시간 비율, 통로 길이·규모

### Takeaway
과채류 온실에서는 수확·유인·정지 같은 "통로를 따라 이동하며 하는 작업"이 전체 노동시간의 약 2/3~70%를 차지하고, 수확(24%)과 출하 준비(23%)도 큰 비중을 차지한다. 그러나 **이동·운반 시간만 따로 떼어 본 온실 대상 시간동작 분석 수치는 공개 자료에서 찾지 못했다.** 대신 노지 수확 연구에서 "운반·보행 같은 비생산 시간"을 줄이면 수확 효율이 오른다는 근거가 있고, 1ha 온실의 통로 총길이는 수 km 규모다.

### Cited Findings
- 시설 가지과 채소에서 유인·정지·수확 작업이 전체 노동시간에서 차지하는 비율: **파프리카 70.3%, 방울토마토 67.4%, 가지 48.3%**. 정식부터 작기 종료까지 1,000㎡당 소요 노동시간은 조사 농가별 **497시간, 604.9시간, 514시간**이었다. — [Analysis of the Relationship between Sweet Pepper Stem Growth and Labor Load (Horticultural Science and Technology)](https://www.hst-j.org/articles/xml/YwYo/)
- 일본 토마토 시설에서 **수확이 전체 작업시간의 24%, 출하 준비가 23%** 를 차지했다(스마트 기기로 작업 정보를 측정한 연구, Sensors 2018). — [Yield Visualization Based on Farm Work Information Measured by Smart Devices (PMC6263386)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6263386/)
- 노지 토마토 수확 시간 분석(UF/IFAS FE1026)은 수확 사이클을 "용기 채우는 시간"과 "**비채움 시간(트럭까지 걸어가 비우고 돌아오는 시간)**"으로 나눴다. 트럭에 가까운 작업자일수록 걷는 시간이 짧았다. — [FE1026 Labor Requirements and Costs for Harvesting Tomatoes (UF/IFAS)](https://ask.ifas.ufl.edu/publication/FE1026/pdf)
- 온실 토마토 작업방법을 시뮬레이션한 연구는 작업자 보행 속도 등을 모델링해 **비생산 시간(non-productive time)** 을 예측했다(작업 방법 개선 대상으로 이동을 명시). — [Improvement of Work Methods in Tomato Greenhouses Using Simulation](https://www.researchgate.net/publication/270579348_Improvement_of_Work_Methods_in_Tomato_Greenhouses_Using_Simulation)
- 온실 토마토 노무관리에 시간연구와 기정시간법(MOST 등)을 적용한 연구가 있다. 기정시간과 실측 시간의 차이는 정지 작업에서 약 6~23% 이상, 수확에서 약 3~7%였다. — [Time study techniques applied to labor management in greenhouse tomato cultivation (Agrociencia)](https://www.researchgate.net/publication/285731886_Time_study_techniques_applied_to_labor_management_in_greenhouse_tomato_Solanum_lycopersicum_L_cultivation); [Agrociencia PDF](https://www.redalyc.org/pdf/302/30211225006.pdf)
- 상업 온실의 재배 열 길이는 온실 크기에 따라 약 **120~300 ft(약 37~91 m)** 이다. — [Alberta: Tomato plant propagation in commercial greenhouse tomato production](https://www.alberta.ca/tomato-plant-propagation-in-commercial-greenhouse-tomato-production)
- 대형 온실 통로 폭: **보조 통로 0.60~0.90 m, 주 통로 1.2~1.8 m**. 벤로형은 3.2 m 스팬당 4열 재배와 2개 통로로 구성하고, 토마토는 약 0.5 m 간격의 2열 재배 사이에 **약 1.1 m 작업 통로**를 둔다. 바닥 온수 난방관은 장비용 레일(파이프레일)로 겸용한다. — [Greenhouse tomato production 관련 자료 (검색 요약: Peet & Welles; ResearchGate Venlo 그림)](https://www.researchgate.net/figure/Example-of-a-Venlo-greenhouse-Modern-Venlo-greenhouse-in-background-left-an-older-one_fig2_239847413)
- 국내 사례: 아이오크롭스는 2021년 3,000평으로 시작해 **2만1,000평(약 6.9 ha)** 규모의 파프리카·토마토 온실을 직접 운영한다. 뉴로메카와 함께 만든 로봇은 **3,000평이 넘는 온실 내부를 자율주행**하며 생육 데이터를 수집한다. — [이투데이 탐방기 (2024~2025)](https://www.etoday.co.kr/news/view/2370164); [ITWorld: 뉴로메카-아이오크롭스 로봇 플랫폼 (2023)](https://www.itworld.co.kr/news/280309)

### Inferences
- 통로 간격 1.6 m로 가정하면 1 ha에는 약 6,250 m의 통로가 있다(100 m 열 기준 약 62개 통로). 수확자는 통로 양쪽을 작업하고 수거 지점까지 오가므로, **1 ha를 한 바퀴 도는 데만 6 km 이상**을 걷는다는 추정이 가능하다(필자 계산이며 출처 수치가 아님).
- 수확·유인·정지가 노동의 약 70%를 차지하고 이 작업들은 모두 통로를 따라 걸으며 수확물·자재를 끌고 다니는 구조다. 따라서 "보행+운반" 부담을 로봇에 넘기는 것이 노동 절감 효과가 가장 큰 지점이라고 볼 수 있다.

### Gaps
- 온실(또는 수직농장)에서 **이동·운반 시간이 총 작업시간의 몇 %인지** 직접 측정한 시간동작 분석 수치는 찾지 못했다. 농촌진흥청 작업분석 보고서나 한국농업기계학회지·생물환경조절학회지의 "운반 노동시간" 연구를 원문으로 확인할 필요가 있다.
- 수직농장의 통로·이동 동선 관련 정량 자료는 찾지 못했다.

---

## 2. 자율주행 도입을 통한 이동 시간·노동 절감 가능성 (파이프레일 로봇, 자율 운반차)

### Takeaway
작업자 추종(follow-me) 운반 로봇과 AGV 수확대차는 "수확물을 들고 걸어가 비우고 돌아오는" 비생산 시간을 없애는 방식으로 효과를 낸다. 동료 심사를 거친 시뮬레이션 연구는 **수확 효율 약 10% 향상**을 보고했고, 업체 자체 주장은 **15~48%**, 국내 농진청 실증은 **1회 300 kg 운반, 방제 작업시간 50% 단축**이다.

### Cited Findings
- **Seyyedhasani et al. (2020, Computers and Electronics in Agriculture, Part I/II)**: 수동 수확과 로봇 보조 수확을 하이브리드 오토마타로 모델링하고 확률 시뮬레이터를 만들었다. 수동 수확의 비생산 시간 예측 오차는 오전 6.4%, 오후 3%, 하루 전체 1.2%였다. **운반 로봇 5대가 수확자 25명을 반응형으로 지원하면 수확 효율이 최대 10.2% 향상**됐다. 로봇은 공유 자원이라 대기 시간이 생기므로 **스케줄링이 효과를 좌우**한다. — [Part I (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S016816991932486X); [Part II (ADS)](https://ui.adsabs.harvard.edu/abs/2020CEAgr.17205323S/abstract); [eScholarship](https://escholarship.org/uc/item/0j36x3fk)
- 같은 그룹의 후속 연구(딸기 수확 보조 co-robot 실증, 2021~2023)도 **수확 효율 약 10% 향상과 평균 비생산 시간 감소**를 보고했다. — [A strawberry harvest-aiding system with crop-transport co-robots (arXiv 2107.13063)](https://arxiv.org/pdf/2107.13063); [UC Davis PDF](https://s.gifford.ucdavis.edu/uploads/pub/2023/03/10/vougioukasrobots.pdf)
- **농촌진흥청 작업자 추종 운반 로봇 (2023.11 발표)**: 작업자를 따라다니며 수확물을 운반하고 자동 하역한다. **1회 최대 300 kg, 10시간 이상 연속 작동**하며, 전북 익산 토마토 농장에서 실증했다. — [뉴시스 2023-11-29](https://www.newsis.com/view/NISX20231129_0002539343); [머니투데이 2023-11-29](https://www.mt.co.kr/future/2023/11/29/2023112910124825042); [중도일보](https://m.joongdo.co.kr/view.php?key=20231129010009570); [농민신문 2024-03-22](https://www.nongmin.com/article/20240322500556)
- **농진청 방제 로봇**: 300 L 약제를 싣고 8시간 이상 자율 운전하며 **0.33 ha를 1.5시간에 무인 방제**한다. 익산 농가 현장에서는 1,000평 기준 **3시간 → 1.5시간**으로 줄었다. 운반은 "수동 80 kg → 자동 300 kg"으로 바뀌었다. 2025년 보급 계획은 운반 13대, 방제 10대(총 23대)였고, 운반 로봇 1대 도입비는 약 2,500만 원으로 보도됐다. — [전자신문 르포 2025-10-09](https://www.etnews.com/20251009000070); [아주경제 르포 2025-09-28 ("방제로봇으로 연간 1200만원 절감")](https://www.ajunews.com/view/20250928143618678)
- **Burro (미국, 작업자 추종 협동로봇)**: 회사 측은 6명 이상의 팀에 1대를 붙이면 하루 수확량이 **최대 48% 증가**하고 2개월 이내에 투자를 회수한다고 주장했다(2021 시리즈 A). 다른 보도는 8인 팀 기준 **15~30% 증가**로 소개했고, 2018년 CEO는 "왕복 보행이 사라져 **20~30% 더 수확**"한다고 말했다. **모두 업체 자체 수치이며 독립 검증은 없다.** — [The Robot Report (2021)](https://www.therobotreport.com/burro-raises-10-9m-series-a-to-accelerate-agriculture-robotics/); [Farmtario](https://farmtario.com/machinery/diminutive-burro-packs-a-big-ai-robotic-punch/); [Future Farming](https://www.futurefarming.com/tech-in-focus/field-robots/burro-raises-%E2%80%8910-9-million-to-commercialise-field-robots/)
- **네덜란드 온실 AGV 수확대차**: Berg Hortimotive의 AGV Tomato는 수확자를 따라가며 보행·수확 센서로 속도를 계속 맞춘다. 대차가 차면 유도선(induction) 경로로 선별장까지 스스로 가고, 빈 상자를 싣고 돌아온다. — [Berg Hortimotive Tomato AGV](https://berghortimotive.com/en/harvest-a-transport/loose-and-vine-tomatoes)
- 네덜란드 토마토 농가가 내부 운반 시스템 2종을 큰 개조 없이 연결한 사례: AGV 대차 길이 **2.4 m, 적재 약 350 kg, 배터리 2일 지속**. 노동 절감 효과는 정성적으로만 서술됐다. — [HortiDaily: Two internal transport systems linked for tomato grower](https://www.hortidaily.com/article/9568533/two-internal-transport-systems-linked-for-tomato-grower/)
- AGV 수확대차를 쓰면 온실과 작업장 사이에 별도 내부 운반 시스템이 필요 없다는 업체 설명. — [Steenks Service: AGV harvesting trolley](https://www.steenks-service.com/pipe-rail-trolleys/agv-harvesting-trolley/); [Royal Brinkman BeMotion AGV Tomato](https://royalbrinkman.com/mechanical-equipment/internal-transport/harvest-trolleys/bemotion-agv-tomato-999701228)

### Inferences
- 효과의 핵심은 "로봇이 따라와 주는 것" 자체보다 **로봇이 제때 제자리에 와 있는 것**이다. Seyyedhasani 연구에서 대기 시간이 이득을 상쇄한 점을 보면, Robot B(추종 운반)가 Robot A(예찰)가 만든 작물·수확 대상 위치 정보를 미리 받아 **배차·경로를 선제적으로 계획**할 때 효율 개선 폭이 커질 수 있다.
- 업체 주장(15~48%)과 학술 결과(약 10%)의 차이가 크다. 제안서에서는 보수적 근거(10%, 농진청 50% 시간 단축)와 상한 시나리오(업체 수치)를 구분해서 쓰는 것이 바람직하다.

### Gaps
- 온실 파이프레일 자율 로봇의 **이동 시간 절감률(%)** 을 실측한 동료 심사 논문은 찾지 못했다.
- 2026년 *Agriculture* 리뷰 "Transport Robots in Protected Horticulture"(아래 3장)에 정량 사례가 있을 가능성이 높지만 원문 접근이 막혀 확인하지 못했다.

---

## 3. 농장 환경의 주행 장애 요소와 해결 기술

### Takeaway
온실은 GNSS를 쓸 수 없고, 길고 좁으며 **반복적인 통로 구조** 때문에 SLAM이 혼동(perceptual aliasing)하기 쉽다. 여기에 유리벽 반사, 작물 가림, 조명 변화, 젖은 바닥에서의 휠 슬립, 고온·고습이 겹친다. 이를 풀기 위한 기술로 **LiDAR SLAM과 레일 주행의 하이브리드, UWB·초음파 태그, 시각-IMU-휠 오도메트리 융합** 등이 연구되고 있다.

### Cited Findings
- **GNSS 불가**: 실내 온실은 신호 가림 때문에 GNSS로 정확한 위치를 얻을 수 없다. LiDAR로 작물 열 2D 지도를 만들고 AMCL로 전역 위치를 추정한 뒤 UWB, IMU, 오도메트리와 융합한다. — [Integrated Indoor Positioning System of Greenhouse Robot Based on UWB/IMU/ODOM/LIDAR (Sensors 2022, PMC9269595)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9269595/)
- **반복 구조와 좁은 통로**: "길고 좁으며 매우 반복적인 온실 골조 구조"가 위치 추정의 큰 장애다. 이를 시각-IMU-휠 오도메트리 융합으로 해결하려는 연구. — [Real-Time Localization and Mapping Utilizing Multi-Sensor Fusion and Visual–IMU–Wheel Odometry ... GPS-Denied Greenhouse Environments (Agronomy 2022)](https://www.mdpi.com/2073-4395/12/8/1740)
- 온실 장면은 고유한 시각 특징이 부족해 위치 추정이 어렵다(GREENBOT 데이터셋, 2024). — [The GREENBOT dataset (arXiv 2402.00438)](https://arxiv.org/pdf/2402.00438)
- 반복 환경에서는 LiDAR와 카메라 모두 perceptual aliasing이 생기고 **조명 변화에 민감**하다(포도원 연구, 유사 구조). — [Semantic Landmark Particle Filter for Robot Localisation in Vineyards (arXiv 2603.10847)](https://arxiv.org/pdf/2603.10847)
- **유리벽 반사·특징 희소**: 다연동 온실에서 유리벽이 LiDAR 반사를 일으키고 특징이 희소해 SLAM 성능이 떨어진다. 해결책은 운송 구역에서는 개선한 LIO-SAM(반사 필터링, 루프 클로저 개선)과 A*/DWA를 쓰고, 재배 구역에서는 **레일 전환을 시각 서보잉으로 처리하는 하이브리드**다. 0.2 m/s에서 평균 횡방향 편차는 **4.12 cm**였다. — [A LiDAR SLAM and Visual-Servoing Fusion Approach to Inter-Zone Localization and Navigation in Multi-Span Greenhouses (Agronomy 2025)](https://doi.org/10.3390/agronomy15102380)
- **작물 가림과 SLAM 왜곡**: 딸기 온실 방제 로봇 연구에서 일반 LiDAR SLAM은 비슷한 작물 특징에 따른 지도 왜곡, 누적 오차, 위치 점프 문제가 있었다. **초음파 태그를 융합하자 최대 횡오차가 0.045 m**로 유지됐다(2025). — [A novel fusion positioning navigation system for greenhouse strawberry spraying robot using LiDAR and ultrasonic tags (ScienceDirect 2025)](https://www.sciencedirect.com/science/article/pii/S2949798125000171)
- 초음파 비콘 방식에서도 열 사이에서는 **캐노피 가림 때문에 위치 정확도가 떨어졌다**(Frontiers in Plant Science 2024). — [Frontiers in Plant Science 2024 (fpls.2024.1276799)](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1276799/xml)
- **조명·지면**: 2D LiDAR 온실 위치 추정 연구에서 울퉁불퉁한 지면과 불확실한 조명 때문에 실험실 복도보다 정확도가 낮았다. — [Autonomous Localization and Navigation for Agricultural Robots in Greenhouse (ResearchGate)](https://www.researchgate.net/publication/371310254_Autonomous_Localization_and_Navigation_for_Agricultural_Robots_in_Greenhouse)
- **고온·고습, 젖은 바닥 슬립**: 온실 로봇은 고온·고습 환경에서 작동해야 하고, 젖은 지면에서는 휠 슬립으로 오도메트리 오차가 누적된다. — [Navigation and Sensor Fusion for Autonomous Field Robots in Precision Agriculture: Narrative Review (Sensors, MDPI)](https://www.mdpi.com/1424-8220/26/16/5169)
- **레일 vs 자유 주행**: 고정 레일은 로봇의 경로와 작업 범위를 크게 제한한다. 3D LiDAR를 2D로 변환해 Cartographer로 SLAM을 하면 레일, 자기 테이프, 컬러 밴드 같은 추가 설치가 필요 없지만, 3D LiDAR는 계산 부하가 크다. — [Autonomous Navigation System of Greenhouse Mobile Robot Based on 3D Lidar and 2D Lidar SLAM (Frontiers in Plant Science 2022, PMC8960995)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8960995/)
- 온실 로봇 리뷰(2022): Thorvald II는 사전 기록한 웨이포인트로 주행하고, 엔코더 오도메트리와 2D LiDAR로 GMapping을 쓰는 사례도 있다. **레일 방식은 온실 구조 변경이 필요해 비용이 늘어난다.** — [Greenhouse Robots: Ultimate Solutions to Improve Automation in Protected Cropping Systems—A Review (Sustainability 2022)](https://doi.org/10.3390/su14116436)
- 시설원예 운반 로봇 리뷰(2026)는 운반 로봇을 "기계·전자 시스템이자 물류 시스템"으로 보고, 2D/3D LiDAR, SLAM, UWB, IMU를 주요 센서로 정리했다. **GNSS 불가 환경의 위치 추정을 핵심 과제**로 꼽았다. — [Transport Robots in Protected Horticulture: A Review of Key Technologies, Representative Systems, and Future Directions (Agriculture 2026)](https://doi.org/10.3390/agriculture16111145)
- **파이프레일+콘크리트 혼합 바닥**: 상용 수확대차는 파이프레일 위를 달리다가 콘크리트 통로로도 이동한다. 네덜란드 AGV는 콘크리트 주 통로에서 **유도선(induction) 경로**를 쓴다. — [Royal Brinkman Harvest Trolleys](https://royalbrinkman.com/mechanical-equipment/internal-transport/harvest-trolleys/); [Berg Hortimotive](https://berghortimotive.com/en/harvest-a-transport/loose-and-vine-tomatoes)
- **조명(UV-C 사례)**: Saga Robotics는 햇빛, 특히 청색광이 곰팡이의 UV-C 손상 회복을 유도하므로 UV-C 처리를 **야간에** 한다. 농장 로봇이 주간·야간과 다양한 조명 조건에서 모두 주행해야 한다는 점을 보여준다. — [AgFunderNews: Saga Robotics raises $11.2m](https://agfundernews.com/saga-robotics-raises-11-2m-to-expand-fleet-of-bots-blasting-powdery-mildew-with-uv-c-light)

### Inferences
- 파이프레일 구간(재배 통로)은 레일 기하 구조를 구속 조건으로 쓰면 위치 추정이 쉽다. 콘크리트 주 통로와 작업장 구간은 LiDAR SLAM이나 마커가 필요하다. 그래서 **"레일 + SLAM + 마커/태그" 하이브리드**가 현실적인 설계라는 데 문헌이 수렴한다.
- 반복 구조 때문에 SLAM만으로는 "몇 번째 통로, 몇 번째 포기"를 혼동할 수 있다. Robot A가 공유하는 해충·작물 위치는 SLAM 좌표만이 아니라 **통로 ID와 레일 상 거리(또는 QR·UWB 앵커) 같은 위상(topological) 좌표**로 함께 표현해야 Robot B가 정확히 찾아갈 수 있다.
- 사람·대차가 같이 다니는 공간이므로 Robot B의 추종 주행에는 사람 인식과 감속·정지 기능(4장의 ISO 3691-4 개념)이 필요하다. 사람을 인식하는 주행 모듈 연구로는 Guevara et al.(J. Field Robotics 2024) "Implementation of a human-aware robot navigation module for cooperative soft-fruit harvesting operations"가 있다. — [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22227)

### Gaps
- 결로·고습이 LiDAR나 카메라 성능에 주는 영향을 **정량화한 온실 연구는 찾지 못했다**.
- LED 보광(적·청색 광)이 비전 기반 위치 추정·인식에 주는 영향을 정량화한 자료는 확인하지 못했다.
- 수직농장 전용 주행(다층 랙, 리프트 연계) 문헌은 이번 범위에서 찾지 못했다.

---

## 4. 기존 수작업 정보 전달(예찰 결과 → 작업자/다른 작업)의 문제

### Takeaway
종이 예찰 기록은 보통 "동/구역" 단위로만 남아 **정확한 위치를 잃고**, 관리자에게 전달될 때쯤에는 **이미 오래된 정보**가 되며, 나중에 다시 옮겨 적어야 한다. 디지털 예찰 앱은 QR·위치를 태그하고 클라우드로 동기화해 이 문제를 줄인다. 다만 **지연·누락을 정량화한 연구는 찾지 못했고**, 근거는 대부분 업체·지도기관 자료다.

### Cited Findings
- 종이 예찰 결과는 정확한 지점이 아니라 동이나 블록 단위로만 연결되는 경우가 많다. 관리자에게 전달될 때쯤이면 이미 오래된 정보가 돼, 국소 처리 대신 전면 살포로 이어진다(화훼 농장 정밀 국소 방제 사례). — [FloralDaily: targeted spot spraying](https://www.floraldaily.com/article/9890668/helping-flower-farms-cut-chemical-use-by-replacing-blanket-spraying-with-targeted-spot-spraying/)
- 종이 기록은 나중에 전산으로 옮겨 적어야 한다. Biobest Crop-Scanner는 관찰 결과를 클라우드에 바로 올리고, "디지털 예찰이 수년 내 과채류 생산의 표준이 될 것"이라고 전망했다(업체 견해). — [Biobest: Digital scouting in greenhouse vegetables](https://www.biobest.com/news/digital-scouting-will-become-the-standard-in-vegetable-production-within-a-few-years)
- Cornell Pocket IPM Greenhouse Scout는 **위치마다 QR 코드**를 붙여 위치·날짜별로 예찰 데이터를 기록하고, 오프라인에서 저장했다가 연결되면 동기화한다. — [Greenhouse Canada: Scouting? There's an app for that](https://www.greenhousecanada.com/scouting-theres-an-app-for-that/); [Hort Americas](https://hortamericas.com/blog/news/looking-for-a-better-easier-way-to-do-greenhouse-ipm/); [Pocket IPM help](https://greenhouse-scout.pocketipm.com/help)
- Ecoation OKO 시스템은 하루 작업이 끝날 때 Wi-Fi와 전원에 연결해야 데이터가 올라간다. 즉 **실시간이 아닌 일 단위 배치 전송**이다. — [Ecoation](https://www.ecoation.com/)
- MSU 지도 자료는 온실 IPM에서 온실 지도를 포함한 예찰 기록 유지를 권고한다. — [MSU Extension: Pest scouting in greenhouses (PDF)](https://www.canr.msu.edu/uploads/resources/pdfs/pest_scouting_in_greenhouses.pdf)
- 국내: 농진청 모니터링 로봇은 병충해 발생 위치를 **오차 5 cm 이내**로 파악하고, 그 정보를 클라우드나 로컬 서버로 보내 농업인이 위치별로 확인할 수 있게 한다(사람이 찾아서 기록·전달하던 방식을 대체). — [농촌진흥청 보도자료: 온실 내 병충해 발생 상황, 로봇이 알려준다](https://www.rda.go.kr/board/board.do?mode=view&prgId=day_farmprmninfoEntry&dataNo=100000792060)

### Inferences
- 종이·구두·메신저 전달은 ① 위치 해상도가 낮고(동·구역 단위), ② 전달이 늦고(하루 단위 이상), ③ 옮겨 적는 과정에서 누락·오기가 생기는 3중 손실 구조다. Robot A → Robot B로 좌표를 기계 간에 바로 넘기면 세 가지를 동시에 줄일 수 있다는 논리가 성립한다.
- 메신저(카카오톡 등) 기반 전달 관행에 대한 국내 조사·통계는 찾지 못했다. 제안서에는 "현장 관행"으로 정성적으로만 서술하는 것이 안전하다.

### Gaps
- 수작업 예찰 정보 전달의 **지연 시간·누락률을 측정한 정량 연구**는 찾지 못했다.
- 국내 농가의 예찰 기록 방식(종이·메신저) 실태조사 자료는 찾지 못했다.

---

## 5. 로봇 간 실시간 정보 공유(멀티로봇 협업, ROS 2, fleet management, 디지털 트윈/FMS)의 필요성과 기대효과

### Takeaway
"예찰 로봇이 위치를 찾아 → 작업 로봇이 그 위치로 가서 일한다"는 구조는 이미 **농진청이 예찰-방제 로봇 연계(위치 오차 5 cm 이내)와 다기종 로봇 통합관리 프로그램(2025 시범 보급)** 으로 실증하고 있다. 해외에서도 Ridder·Priva 같은 온실 통합 플랫폼이 로봇 데이터를 연동하는 방향으로 가고 있다. 학술 리뷰는 멀티로봇 시스템의 성패가 **인지 공유, 상태 동기화, 온라인 작업 스케줄링**에 달려 있다고 정리한다.

### Cited Findings
**국내**
- **농진청 예찰 ↔ 방제 로봇 연계**: 병해 모니터링 로봇이 **병해 발생 구역의 위치 정보와 방제 정보를 방제 로봇에 전달**하면, 방제 로봇은 그 위치로 가서 구역 전체를 방제하거나 해당 잎만 국소 방제한다. 위치 오차는 5 cm 이내다. — [농촌진흥청 보도자료](https://www.rda.go.kr/board/board.do?mode=view&prgId=day_farmprmninfoEntry&dataNo=100000792060)
- **농진청 농업로봇 통합관리 기술 (2025.04 공개)**: 온실 안 로봇들의 실시간 위치를 추적하고, **경로 간섭 없이 다기종 로봇(방제·운반·모니터링)이 협업**하도록 설계한 통합관리 프로그램이다. 방제 로봇의 약제가 떨어지면 운반 로봇이 약액을 보충하는 로봇 간 협업도 개발 중이며, 2025년 강원·충청 지역에 시범 보급됐다. — [정책브리핑 korea.kr: "이젠 로봇도 체계적으로" 통합 관리 기술](https://www.korea.kr/news/policyNewsView.do?newsId=156685775); [전자신문 2025-04-23: 농업로봇 통합관리 기술 첫 공개](https://www.etnews.com/20250423000182)
- ★ 도입 조건으로 **온실 내 레일 설치가 필수이고 도입 가능 면적은 0.5 ha 이상**이라는 보도가 있다(검색 요약 기준이며, 어느 기사인지 원문 확인 필요; 후보는 위 두 기사와 [한국농기계신문](https://www.kamnews.co.kr/news/articleView.html?idxno=7631)). 모니터링-방제 연계 자동화는 대형 온실에 적합하고, 소규모 농가용으로는 CCTV와 소형 컴퓨터 분석이 연구되고 있다.
- 아산시는 스마트팜에 병해충 감지 로봇을 투입했다. — [대전MBC](https://tjmbc.co.kr/NewsArticle/836766)
- **아이오크롭스 HERMAI**: 예찰·운반·방제·수확을 수행하는 AI 자율주행 온실 로봇. 국책 과제로 수확 로봇을 실증 중이며 **2027년 상용화**를 계획하고 있다. 2025년에는 수확 로봇, 그리퍼, 자율주행 관련 국가 R&D를 수행했다. — [이투데이](https://www.etoday.co.kr/news/view/2370164); [ITWorld 2023](https://www.itworld.co.kr/news/280309); [파이낸셜뉴스 2023-03-03](https://www.fnnews.com/news/202303031048333770)

**해외 상용/플랫폼**
- **Ridder**: MetoMotion과 제휴해 로봇 플랫폼을 글로벌 유통하고, 토마토 수확 로봇 GRoW(양팔, 3D AI 비전)를 보유한다. Ridder는 로봇이 만든 데이터를 온실 내 다른 Ridder 시스템과 통합하겠다고 밝혔다. 개방형 클라우드·API 플랫폼으로 외부 파트너(Aranet, Quantified 등)와 연동한다. — [Ridder adds robotics to its portfolio](https://ridder.com/insights/news/ridder-adds-robotics-to-its-portfolio); [Netrom: Ridder open platform](https://www.netromsoftware.com/client-cases/ridder/)
- **Priva**: Priva Gateway와 Priva API Services로 환경제어기 데이터를 외부 서비스와 안전하게 공유하고, "로보틱스·제어기술·온라인 앱을 연결"하는 개방형 통합 플랫폼을 내세운다. — [Priva: Integrate greenhouse data](https://www.priva.com/horticulture/solutions/digital-services/integrate-greenhouse-data); [Priva: Get connected](https://www.priva.com/horticulture/get-connected)
- **Saga Robotics (Thorvald)**: 2021년 영국 딸기 시즌을 **8대**로 시작해, 2025년 시즌에는 캘리포니아 포도원 **약 1,300 에이커**와 영국 테이블탑 딸기 시장의 **약 20%** 를 처리했다(회사 발표). 제3자 프로필은 보유 대수를 150대 이상으로 추정한다(공식 수치 아님). 로봇은 카메라 2대로 열마다 꽃·과실 수와 숙도 데이터를 수집해 IPM 서비스와 연계한다. — [Saga: 2021 light treatment season](https://www.sagarobotics.com/post/the-2021-light-treatment-season-has-started); [FreshPlaza: autonomous robots expand in US and UK](https://www.freshplaza.com/europe/article/9779878/autonomous-robots-expand-crop-operations-in-us-and-uk/); [HortiDaily: UV-C robot expanded to count flowers and strawberries](https://www.hortidaily.com/article/9748129/uv-c-robot-expanded-to-count-flowers-and-strawberries); [village.ai profile](https://village.ai/company/saga-robotics)

**학술**
- 멀티 타깃 수확 로봇 리뷰(2026): 멀티로봇 시스템은 플랫폼 간 **인지 공유, 로봇 상태 동기화, 온라인 작업 스케줄링**에 의존한다. 멀티암·멀티로봇으로 갈수록 커버리지와 효율은 오르지만 **에이전트 간 정보 공유, 작업 할당, 충돌 해소**가 어려워진다. — [Multi-Target Harvesting Robots: Key Advances and Future Trends in Perception, Decision-Making, and Task Scheduling (Agriculture 2026)](https://doi.org/10.3390/agriculture16171926)
- 농업 멀티로봇 조정 리뷰는 **정찰(scout) 유닛이 먼저 개입이 필요한 지역을 찾고 작업 로봇이 대응하는** 구조를 대표 예로 든다(UAV 정찰 → UGV 개입). 과제 구조가 Robot A → Robot B와 같다. — [Multi-Robot Coordination and Fleet Management for Autonomous Agricultural Operations (ResearchGate)](https://www.researchgate.net/publication/392858778_Multi-Robot_Coordination_and_Fleet_Management_for_Autonomous_Agricultural_Operations)
- 포도 수확에서 인간-로봇 협업 플릿을 **미션 컨트롤 센터**가 조정하고, 로봇별 MQTT 토픽으로 텔레메트리를 전송하는 구조(2026). — [Intelligent coordination of a human-robot collaborative fleet for assistance in manual fruit harvesting (ScienceDirect 2026)](https://www.sciencedirect.com/science/article/pii/S2772375526004168)
- 분산 Thompson sampling으로 로봇들이 중앙 서버 없이 확률적 정보를 공유하는 농·임업 정보 수집 연구(2025). 예찰 로봇 여러 대 확장 시 참고할 수 있다. — [Distributed multi-robot active gathering for non-uniform agriculture and forestry information (PMC12586092)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12586092/)
- 협동 로봇 농업 개요(2021): 딸기 수확 로봇들이 서로 위치를 통신해 충돌을 피하는 사례. — [An Overview of Cooperative Robotics in Agriculture](https://www.researchgate.net/publication/354516809_An_Overview_of_Cooperative_Robotics_in_Agriculture)
- 이기종 협업 수확 시스템의 휴리스틱 조정(2025). — [Heuristic Approaches for Coordinating Collaborative Heterogeneous Robotic Systems in Harvesting Automation (PMC12568294)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12568294/)
- 운반 co-robot의 효과(수확 효율 약 10%)는 **스케줄링·배차 품질에 좌우**된다(2장의 Seyyedhasani 2020). 다른 로봇이나 FMS의 정보로 배차를 개선할 여지가 있다는 근거다. — [ADS Part II](https://ui.adsabs.harvard.edu/abs/2020CEAgr.17205323S/abstract)

**ROS 2 / 물류 분야 플릿 관리 기술**
- **Open-RMF**는 ROS 2 기반 미들웨어로 작업 큐잉, 충돌 없는 자원 스케줄링, 플릿 어댑터를 제공한다. 이기종 플릿을 연결할 때 "관측만 공유하는(FleetState)" 플릿과 "경로 명령까지 받는(Full Control / Traffic Light Control)" 플릿을 함께 운용할 수 있다. — [Open-RMF docs](https://openrmf.readthedocs.io/_/downloads/en/latest/epub/); [Ekumen: Nav2 + Open-RMF](https://ekumenlabs.com/blog/posts/nav2-open-rmf-fleet-coordination/); [Physical AI Portal: Open-RMF와 VDA 5050](https://physicaiportal.com/en/posts/multi-robot-fleet-orchestration-open-rmf-vda5050/)
- VDA 5050은 단일 로봇-마스터 제어 인터페이스이고, Open-RMF는 그 위에서 여러 플릿과 공유 인프라를 조정한다. Open-RMF는 오케스트레이션 계층이라 저수준 DDS 디스커버리 폭주나 네임스페이스 충돌은 해결하지 못한다(2026). — [Physical AI Portal](https://physicaiportal.com/en/posts/multi-robot-fleet-orchestration-open-rmf-vda5050/); [SFG-ROS (arXiv 2605.23832)](https://arxiv.org/pdf/2605.23832)
- 창고 시나리오에서 Open-RMF로 AMR 작업을 오케스트레이션하고, 보행자 회피는 저수준 제어기가 맡는 사례. — [Safe Human Robot Navigation in Warehouse Scenario (arXiv 2503.21141)](https://arxiv.org/pdf/2503.21141)
- ROS 2와 Unity를 결합해 AMR 플릿을 관리하는 디지털 트윈/가상화 툴킷(2026). — [VirTooS (arXiv 2608.26066)](https://arxiv.org/pdf/2608.26066)

### Inferences
- 기대효과(제안서 논리):
  1. **선제 배차**: Robot A가 수확 적기 과실과 해충 위치를 실시간으로 넘기면 Robot B는 작업자가 갈 통로를 미리 알고 대기 위치·경로를 계획할 수 있다. Seyyedhasani 연구에서 드러난 "대기 시간 손실"을 줄이는 방향이다.
  2. **위치 정확도**: 종이·구두 전달의 "동·구역" 해상도에서 로봇 좌표 수준(국내 실증 5 cm)으로 높아진다.
  3. **충돌·간섭 회피**: 좁은 통로에서 두 로봇의 실시간 위치를 공유하면 같은 통로에 동시에 들어가는 교착(deadlock)을 막을 수 있다. 농진청 통합관리 프로그램의 설계 목표와 같다.
  4. **이력 데이터화**: 공유한 위치·작업 정보를 Priva/Ridder 같은 환경제어·FMS 플랫폼이나 디지털 트윈에 쌓아 수확량 예측과 IPM에 재활용할 수 있다.
- 구현 측면: ROS 2 DDS 토픽(로컬 직접 공유)과 상위 FMS(Open-RMF 등) 또는 클라우드 MQTT를 이중으로 구성하는 아키텍처가 문헌 사례와 맞는다.

### Gaps
- 온실에서 **이기종 로봇 간 정보 공유의 효과(시간·노동 절감 %)를 실측한 동료 심사 논문**은 찾지 못했다. 국내 농진청 통합관리 프로그램의 정량 효과도 공개 자료에서 확인하지 못했다.
- Kubota, 대동, 그린씨에스의 온실 멀티로봇·FMS 사례는 이번 검색에서 찾지 못했다.
- Open-RMF를 농업·온실에 적용한 사례는 찾지 못했다(물류·창고 사례만 있음).

---

## 6. 관련 표준·안전 규격 (ISO 3691-4, ISO 18497)

### Takeaway
작업자를 따라다니며 사람과 같은 공간을 쓰는 운반 로봇(Robot B)에는 **ISO 3691-4:2023(무인 산업용 트럭/AGV·AMR)** 의 인원 감지, 속도 제어, 제동 요구가 직접 참고 기준이 된다. 농업기계 자율화에는 **ISO 18497 시리즈(2024년 파트 3·4 발행, 2018판 대체)** 가 자율 작업구역 이탈 방지와 검증·확인 원칙을 다룬다.

### Cited Findings
- **ISO 3691-4:2023** (제2판, "Industrial trucks — Part 4: Driverless industrial trucks and their systems"): 무인 산업용 트럭(AGV/AMR)과 그 시스템의 안전 요구사항을 규정한다. 기계적 수단으로만 유도되는 트럭과 원격 조종 트럭은 범위에서 제외된다. — [ANSI Blog: ISO 3691-4:2023](https://blog.ansi.org/iso-3691-4-2023-driverless-industrial-trucks/)
  - 인원 감지, 운전 모드, 제동 시스템 같은 안전 기능의 성능 수준(PL)을 규정한다. "제한 구역(restricted zones)"에서 더 빠르게 운행할 수 있는 조건을 정하며, 2023 개정에서 "active detection field"와 "operational stop" 요구사항을 명확히 했다. — [Pilz](https://www.pilz.com/en-INT/company/news/articles/238928)
  - 충돌 위험을 줄이는 핵심 수단은 **인원 감지 시스템, 속도 제어, 제동 제어**다. — [Control Engineering: Ensuring AGV safety with standards compliance](https://www.controleng.com/ensuring-agv-safety-with-standards-compliance)
  - 제동은 제조사가 정한 감지 범위 안에서 정지해야 하고, 정격 속도를 넘으면 정지가 시작돼야 한다. — [ANSI Blog](https://blog.ansi.org/iso-3691-4-2023-driverless-industrial-trucks/)
  - 북미에는 ANSI/ITSDF B56.5와 ANSI/RIA R15.08이 비슷한 범위를 다룬다. — [Fabrico](https://www.fabrico.io/cs/blog/iso-3691-4-driverless-industrial-trucks/)
- **ISO 18497 (농업기계 및 트랙터 — 고도 자동화 기계 안전)**: 2018판을 파트별로 나눠 대체했고, **Part 3과 Part 4가 2024년 7월 발행**됐다.
  - Part 3: 인지·감시 등의 시스템으로 **자율 작업구역 경계를 의도치 않게 벗어나지 않도록** 하는 설계 원칙(작업구역 자체는 범위 밖).
  - Part 4: 부분 자동, 반자율, 자율 기능의 **검증 방법과 확인(V&V) 원칙**. 발행일 이전에 제조된 기계에는 적용하지 않는다.
  - 두 파트 모두 임업과 공공도로 주행(제동·조향 요구 포함)은 제외한다. — [ISO 18497-4:2024 (iso.org)](https://www.iso.org/standard/82687.html?browse=tc); [Standards NZ: ISO 18497-4:2024](https://www.standards.govt.nz/shop/ISO-18497-42024); [Genorma: ISO 18497-3:2024](https://genorma.com/en/standards/iso-18497-3-2024)

### Inferences
- Robot B(작업자 추종, 사람 혼재 공간)는 ISO 3691-4의 인원 감지, 속도 제한, 제동 요구를 설계 기준으로 삼는다. 동시에 농업기계로서 ISO 18497-3의 "자율 작업구역 경계(온실 동·통로 경계) 이탈 방지"와 ISO 18497-4의 V&V 절차를 따르는 구성이 타당하다.
- 공유 위치 정보(Robot A → B)를 쓰면 ISO 3691-4의 "제한 구역" 개념을 동적으로 운영할 수 있다. 예를 들어 사람이 없는 통로에서는 증속하고 작업자가 있는 통로에서는 감속한다. 다만 이를 안전 기능으로 쓰려면 통신 지연·두절 시 안전 측(감속·정지)으로 동작하도록 설계해야 한다(필자 추론).

### Gaps
- ISO 3691-4의 구체 수치(예: 감지 무효화 시 0.3 m/s 제한)는 업체 블로그에만 나오고 표준 원문으로 확인하지 못했다. 보고서에 쓰면 안 된다.
- 국내 농업용 로봇 안전 기준(농업기계 검정 기준, KS 규격)과 온실 운반 로봇 인증 사례는 이번 검색에서 확인하지 못했다.
- ISO 18497-1/-2(설계 원칙, 장애물 보호) 파트의 발행 상태는 확인하지 못했다.
