# Robot A 수확 적기(숙도) 판단 및 병해충 조기 탐지 필요성 조사

> 작성일: 2026-11-14 | 범위: 시설원예/수직농장 작물(토마토, 딸기, 파프리카, 오이, 엽채류), 2019–2026 자료 우선
> 검증 수준 안내: 이번 조사 세션에서는 frontiersin.org, hortidaily.com 등 일부 사이트의 원문 열람(fetch)이 네트워크 정책으로 막혀 있었습니다. 따라서 아래 수치 상당수는 **검색 결과의 발췌문 기준**이며 원문 전체를 확인하지 못했습니다. 비즈니스 요구사항 문서에 인용하기 전에 원문 대조가 필요한 항목은 [원문 미확인]으로 표시했습니다.

---

## 1. 사람이 수확 시기(숙도)를 판단할 때 생기는 문제

### Takeaway
사람이 눈으로 숙도를 판정하면 주관성, 조명 영향, 작업자 간 편차가 생긴다는 서술은 논문과 업계 자료에 반복해서 나옵니다. 그러나 **작업자 간 일치도(Cohen's kappa, ICC 등)를 측정한 정량 연구는 이번 조사에서 찾지 못했습니다.** 한국 시설원예는 인력 부족이 심하고 외국인 근로자 의존이 커지고 있어 숙련도 확보가 구조적으로 어렵다는 근거가 있습니다.

### Cited Findings
- 숙도 라벨은 연속적인 생물학적 과정을 특정 시점에서 주관적으로 끊어낸 값입니다. 전문 라벨러 사이에서도 단계 경계 부근에서는 판정이 엇갈릴 수 있다고 저자들은 지적합니다(FruitProM-V2, arXiv 2604.26084, 2026, 프리프린트). — [FruitProM-V2: Robust Probabilistic Maturity Estimation (arXiv 2026)](https://arxiv.org/html/2604.26084)
- 같은 논문은 수작업 숙도 판단이 색, 표면 외관, 향, 경도에 의존한다고 설명합니다. 또한 같은 과실을 작업자마다 다르게 등급 판정할 수 있다고 서술하지만, 일치율을 측정한 수치는 제시하지 않습니다. — [arXiv 2604.26084](https://www.alphaxiv.org/abs/2604.26084.md)
- 육안 평가는 본질적으로 주관적이며 조명 조건, 환경 요인, 개인의 지각에 따라 결과가 달라진다는 서술이 있습니다(측색계 제조사 자료이므로 홍보성 주장으로 보아야 함). — [Efficient Tomato Grading with Spectrophotometers (Konica Minolta)](https://sensing.konicaminolta.asia/efficient-tomato-grading-with-spectrophotometers/)
- 머신비전 리뷰 자료(Scribd 사본)는 사람 선별자가 일관성이 없고 인건비 부담이 크다고 서술합니다. 다만 해당 발췌에는 일치도 통계가 없습니다. — [Understanding Color Image Processing by Machine Vision (Scribd)](https://www.scribd.com/document/827167595/Understanding-Color-Image-Processing-by-Machine-Vision)
- **한국 인력 여건**
  - 2013년 한국농촌경제연구원(KREI) 조사에서 '최근 1년 사이 일손 부족으로 농사에 어려움을 겪었다'고 답한 비율은 87.4%였습니다. — [KREI 농어촌 고용실태와 인력정책 방향](https://repository.krei.re.kr/bitstream/2018.oak/19455/1/%eb%86%8d%ec%96%b4%ec%b4%8c%20%ea%b3%a0%ec%9a%a9%ec%8b%a4%ed%83%9c%ec%99%80%20%ec%9d%b8%eb%a0%a5%ec%a0%95%ec%b1%85%20%eb%b0%a9%ed%96%a5.pdf)
  - KREI 보고서에 따르면 시설원예 농가는 작업 특성상 주말·공휴일 잔업을 꺼리는 국내 인력보다 외국인 근로자를 선호하며, 농축산업 고용의 외국인 의존도가 커지는 추세입니다. — [KREI 보고서](https://repository.krei.re.kr/bitstream/2018.oak/19455/1/%eb%86%8d%ec%96%b4%ec%b4%8c%20%ea%b3%a0%ec%9a%a9%ec%8b%a4%ed%83%9c%ec%99%80%20%ec%9d%b8%eb%a0%a5%ec%a0%95%ec%b1%85%20%eb%b0%a9%ed%96%a5.pdf)
  - 농림축산식품부는 2026년 상반기 농업 분야 외국인 노동자를 약 102,104명 공급한다고 밝혔습니다. 상추·오이·토마토 등 시설원예의 고용허가 최소 재배면적 기준도 '2천~4천㎡ 미만 8명'에서 '1천~4천㎡ 미만 8명'으로 완화했습니다. — [농림축산식품부 보도자료](https://www.mafra.go.kr/bbs/home/792/592998/download.do)
  - 외국인 계절근로자 배정 인원은 2022년 19,718명에서 2025년 95,596명으로 약 5배 늘었습니다. 그런데도 농장주들은 요청보다 적게 배정된다고 호소합니다(2026년 7월 현장 보도). — [다음뉴스 르포 (2026-07-05)](https://v.daum.net/v/20260705100151928)
  - 베트남·태국 등에서 새로 들어온 근로자는 작업 숙련도가 매우 낮아 농번기 일을 감당하지 못한다는 농가 발언이 보도됐습니다(2022년, 시설원예가 아닌 양파 농가 사례). — [KED Global: Korea suffers from foreign workers shortage in farming (2022)](https://amp.kedglobal.com/newsAmp/ked202208110005)

### Inferences
- 숙도 판정은 '연속적 변화를 이산 등급으로 나누는' 작업이라 경계 구간에서 편차가 생길 수밖에 없습니다. 따라서 로봇 요구사항에는 단순 분류보다 **숙도 점수(연속값)를 출력하고 농가별 수확 임계값을 설정하는 기능**이 타당합니다.
- 한국에서는 외국인 근로자가 매년 새로 바뀌는 구조여서 숙련 축적이 어렵습니다. 그래서 '판정 기준의 일관성'과 '교육이 필요 없는 판정'이 로봇 도입 명분으로 설득력이 있습니다(추론).

### Gaps
- 토마토·딸기·파프리카 숙도의 작업자 간 일치도(kappa/ICC)를 정량화한 동료심사 논문은 찾지 못했습니다. 원예학/수확후관리 저널(Postharvest Biology and Technology, HortScience 등)을 대상으로 한 추가 검색이 필요합니다.
- 피로나 조명이 판정 정확도에 미치는 영향을 실험으로 측정한 연구도 찾지 못했습니다.
- 시설원예 분야 외국인 근로자 비율의 공식 통계도 찾지 못했습니다.

---

## 2. 수확 시기 오류(조기/지연 수확)에 따른 품질·경제적 손실

### Takeaway
FAO에 따르면 과일·채소는 수확 후 손실률이 가장 높은 품목군으로, 2023년 25.4%입니다. 딸기는 수확 시 숙도가 저장 기간보다 맛에 더 큰 영향을 주며, 늦게 수확하면 저장성이 짧아집니다. 다만 **'수확 시기 오류 때문에 발생한 과숙/미숙 과실 비율'이나 그에 따른 가격 손실을 직접 정량화한 자료는 찾지 못했습니다.**

### Cited Findings
- FAO 식량손실지수(FLI) 기준으로 과일·채소의 손실률은 2015년 23.2%에서 2023년 25.4%로 올라 모든 품목군 중 가장 높습니다. 높은 부패성과 취급 요건 때문입니다. 전 세계 전체 수확 후 손실률은 2023년 13.3%(2015년 13.0%)입니다. — [FAO SDG Indicators Data Portal: 12.3.1 Global food losses](https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/1231-global-food-losses/tracking-progress-on-food-and-agriculture-related-sdg-indicators-2022/en)
- FAO SOFA 2019의 FLI 최초 추정치(2016년 기준)에서 과일·채소 손실률은 21.6%였습니다. 산정 방법과 기준연도가 달라 2023년 수치와 직접 추세를 비교하면 안 됩니다. — [Statista: global shares of agricultural products thrown away](https://statista.com/chart/19672/global-shares-of-different-agricultural-products-thrown-away); [FAO SOFA 2019 요약 (Food Security Portal)](https://www.foodsecurityportal.org/blog/fao-sofa-report-2019-new-insights-food-loss-and-waste)
- FLI의 범위는 생산 현장의 수확 후 단계부터 시작하며, 수확 전 손실은 포함하지 않습니다. 수확 손실은 국가 단위에서만 포함됩니다. — [UN SDG Metadata 12.3.1a](https://unstats.un.org/sdgs/metadata/files/Metadata-12-03-01A.pdf)
- 와게닝겐대(WUR) 연구에서는 숙도 단계가 맛과 풍미에 주는 영향이 저장 기간의 영향보다 훨씬 컸습니다. 미숙 딸기의 맛은 저장 중에도 완숙 딸기 수준에 도달하지 못했습니다. — [WUR Factsheet GC19: Effect of maturity and shelf life](https://wur.nl/nl/show/factsheet-gc19-effect-of-maturity-and-shelf-life.htm)
- 일찍 수확하면 맛과 품질이 떨어지고, 늦게 수확하면 저장성이 짧아지고 이취가 생길 수 있습니다(수확 전 숙도 평가 리뷰). — [IntechOpen chapter 65574](https://intechopen.com/chapters/65574)
- 딸기는 비클라이맥터릭 과실이라 수확 후 수명이 짧습니다. 숙기 구간도 짧아 수확하지 않은 완숙 딸기는 쉽게 상합니다. — [Fruit Physiology and Postharvest Management of Strawberry](https://ouci.dntb.gov.ua/works/4YeGVP04); [Atlantis Press 논문](https://www.atlantis-press.com/article/126024027.pdf)
- 참고(수확 로봇 성능 맥락): 파프리카 수확 로봇 SWEEPER(Journal of Field Robotics, 2020)는 4주 동안 262개 과실로 현장 시험을 했습니다. 평균 사이클 타임은 24초였고, 수확 성공률은 최적 작형에서 61%, 현행 작형에서 18%였습니다. 2025년 리뷰는 선택 수확 로봇 전반의 성공률을 61–76.5%, 사이클 타임을 15–24초로 정리합니다. — [WUR: Development of a sweet pepper harvesting robot](https://research.wur.nl/en/publications/development-of-a-sweet-pepper-harvesting-robot/); [Vision Systems Design 기사](https://www.vision-systems.com/non-factory/scientific-industrial-research/article/16736124/autonomous-mobile-robot-aided-by-3d-vision-harvests-sweet-peppers) [2025 리뷰 원문 미확인]

### Inferences
- 과일·채소의 수확 후 손실 25%에는 숙도 오판이 '저장성 단축 → 유통 중 폐기'로 이어지는 몫이 포함되어 있을 것으로 보입니다. 다만 그 비중을 분리한 통계는 없으므로, 요구사항 문서에서는 '간접 근거'로만 써야 합니다.
- 딸기처럼 숙기 구간이 짧은 작물은 '적기 판정 + 수확 주기 관리'(예: 매일 전수 스캔)의 가치가 큽니다.

### Gaps
- 토마토·딸기·파프리카에서 수확 시기 오류에 따른 과숙/미숙 비율, 등급 하락률, 가격 손실(원/kg)을 정량화한 자료는 찾지 못했습니다. 국내 도매시장 등급별 가격차(aT 농산물유통정보 KAMIS) 분석으로 보완할 수 있습니다.
- 한국 시설원예 품목별 수확 후 손실률 통계도 찾지 못했습니다.

---

## 3. 병해충 조기 발견의 중요성 (주요 병해충 피해 규모, 조기 방제 효과)

### Takeaway
시설원예 주요 병해충은 조건이 맞으면 수확량을 30–100% 줄일 수 있습니다. 딸기 잿빛곰팡이병은 고습 시설에서 30–50%, TYLCV는 최대 100%까지 손실을 낼 수 있습니다. 조기 탐지의 방제비·농약 절감 효과는 주로 업체 주장(농약 최대 25%↓, 작물 손실 30%↓)으로만 확인됐습니다.

### Cited Findings
- **잿빛곰팡이병(Botrytis cinerea), 딸기**: 상대습도 90% 이상, 15–25°C 조건에서 30–50%의 수량 손실을 낼 수 있으며, 특히 시설·터널 재배에서 그렇습니다(Phyton 2024 리뷰). — [Phyton v95n10 (2024)](https://www.techscience.com/phyton/v95n10/69133/html)
- 딸기 잿빛곰팡이병으로 50%가 넘는 손실이 간혹 발생했으며, 주로 꽃과 과실이 감염된 경우입니다(UF/IFAS). — [UF/IFAS PP152](https://ask.ifas.ufl.edu/publication/pp152)
- **잿빛곰팡이병, 토마토**: 시설 토마토에서 흔하고 자주 심각해지는 곰팡이병으로 기술되지만, 손실률 수치는 확인하지 못했습니다. — [Agriculture Victoria: Grey mould in greenhouse tomato crops](https://agriculture.vic.gov.au/biosecurity/plant-diseases/vegetable-diseases/grey-mould-botrytis-in-greenhouse-tomato-crops)
- 예찰·예측 시스템 권고를 따르면 매주 살포하는 경우보다 평균 살균제 살포 횟수가 약 50% 줄었고, 발병률과 수량에는 차이가 없었습니다(딸기 잿빛곰팡이병, 미국 확장교육 자료). — [UF/IFAS PP152](https://ask.ifas.ufl.edu/publication/PP152)
- **토마토 황화잎말림바이러스(TYLCV)**: 지중해 지역에서 최대 100% 수량 손실을 낼 수 있습니다. 담배가루이(Bemisia tabaci)로 전염됩니다. — [Journal of Insect Science 14(1):183](https://academic.oup.com/jinsectscience/article/14/1/183/2387531); [Wikipedia: Tomato yellow leaf curl virus (2차 출처, 90–100%)](https://en.Wikipedia.com/wiki/Tomato_yellow_leaf_curl_virus)
- 묘 단계에서 가루이로 접종했을 때 내성 품종도 56%(Fiona), 67%(8484)의 수량 손실을 보였고, 감수성 품종은 수확이 없었습니다(Phytopathology 2001, 범위 밖 연도이지만 기초 근거). — [typeset.io 사본](https://typeset.io/pdf/effect-of-host-plant-resistance-to-tomato-yellow-leaf-curl-1uyswlkro5.pdf) [원문 미확인]
- **국내 사례**: 시설 토마토에서 TYLCV와 토마토퇴록바이러스(ToCV)가 복합감염된 경우, 복합감염률이 10% 늘 때마다 수량이 405.4 kg/10a 줄었습니다. — [KoreaScience JAKO202211261573256](https://koreascience.or.kr/article/JAKO202211261573256.pdf)
- **조기 탐지의 경제 효과(업체 주장)**: Viscon과 Fermata의 이동형 스카우팅 로봇 EVA는 화학 투입물을 최대 25%, 스카우팅 노동을 50%, 작물 손실을 30% 줄인다고 주장합니다. — [Viscon EVA brochure (2025)](https://viscongroup.eu/app/uploads/2025/06/EVA_A4-brochure-LQ.pdf); [HortiDaily: New autonomous scouting robot launched for greenhouses](https://www.hortidaily.com/article/9739545/new-autonomous-scouting-robot-launched-for-greenhouses)
- Fermata Croptimus 사례(캐나다 온타리오 Ridge Farms): 사람이 보기 전에 가루이 성충을 찾아내 대발생을 막았고, 그 덕분에 천적 방사를 수 주 늦출 수 있었다고 합니다(단일 일화, 업체 경유). — [HortiDaily: AI-powered scouting flags pests before outbreaks](https://www.hortidaily.com/article/9744871/ai-powered-scouting-flags-pests-before-outbreaks-cuts-labor-costs) [원문 미확인]
- Bogaerts 임원은 Ecoation 로봇 데이터로 국소 방제(spot-spraying)를 하면 시간, 인건비, 농약을 절감할 것이라고 말했습니다(측정치가 아닌 전망). — [Greenhouse Grower: Autonomous Robot Does the Greenhouse Scouting for You](https://www.greenhousegrower.com/technology/new-autonomous-robot-does-the-greenhouse-scouting-for-you/)

### Inferences
- TYLCV처럼 매개충(가루이)이 옮기는 바이러스는 일단 감염되면 치료할 수 없습니다. 따라서 '병징 탐지'보다 **매개충 조기 탐지**가 경제적으로 더 중요합니다. 로봇 요구사항에 가루이·총채벌레 개체 탐지를 포함해야 하는 근거입니다.
- 잿빛곰팡이병은 고습 조건에서 빠르게 번집니다. 그래서 환경 데이터(습도)와 영상 탐지를 결합한 위험 지도가 유용할 것입니다(추론).

### Gaps
- 흰가루병, 총채벌레, 온실가루이, 응애가 시설 토마토·파프리카·오이에 주는 피해율(%)은 이번 조사에서 신뢰할 만한 정량 자료를 찾지 못했습니다.
- 조기 발견에 따른 방제비·농약 절감을 독립 연구로 측정한 수치는 찾지 못했습니다(업체 주장만 있음).
- 국가농작물병해충관리시스템(NCPMS)의 국내 시설원예 병해충 발생·피해 통계는 직접 조회하지 못했습니다.

---

## 4. 기존 병해충 탐지 방식(육안 예찰, 끈끈이 트랩)의 한계

### Takeaway
육안 예찰과 끈끈이 트랩 수작업 판독은 노동집약적이고 사람의 실수에 취약하며 대응을 늦춥니다. 표본 조사 방식이어서 초기의 국소적 발생을 놓치기 쉽습니다. 다만 **로봇과 수작업 예찰의 탐지율·비용을 직접 비교한 시설원예 연구는 찾지 못했습니다.**

### Cited Findings
- 트랩 수작업 계수와 육안 점검은 노동집약적이고 사람의 실수에 취약하며, 결정적인 방제 개입을 늦출 수 있습니다. — [Greenhouse Management: IPM monitoring crop pests](https://www.greenhouse-management.com/greenhouse_management/integrated_pest_management_greenhouse_crops/integrated_pest_management_monitoring_crop_pests.htm)
- 현장 예찰은 대체로 병징을 보고 이루어지기 때문에 초기의 공간적으로 드문 발생을 자주 놓친다고 AI 식물건강 리뷰(MDPI AIPA, 2025)는 지적합니다. — [MDPI AI in Plant Agriculture 1(1):2](https://www.mdpi.com/3043-1204/1/1/2)
- 표준 표본 조사 예시로, 식물을 3개 층으로 나누고 층마다 잎 3장을 무작위로 골라 육안 점검하라고 권고합니다. 또한 많은 해충이 날개가 없어 끈끈이 트랩으로는 잡히지 않는다고 경고합니다(UVM 하우스 IPM 가이드, 2019). — [UVM Scouting Guidelines High Tunnel Pests (2019)](https://www.uvm.edu/~entlab/High%20Tunnel%20IPM/Factsheets/Scouting%20Guidelines%20High%20Tunnel%20Pests%20Natural%20Enemies%20Aug%202019%20UVM.pdf)
- 모든 식물을 보지 말고 대표 표본을 보라는 것이 확장교육의 일반적인 권고입니다(UMass). — [UMass: IPM Scouting & Decision Making](https://www.umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/ipm-scouting-decision-making)
- UC Davis 온실 IPM 원격탐사 프로젝트는 핵심 문제를 '초기·신생 해충 개체군을 정확히 찾아내기에 부족한 모니터링/예찰 절차'로 규정합니다. — [Greenhouse Grower: Using Remote Sensing to Optimize IPM in Greenhouses](https://www.greenhousegrower.com/?p=135282)
- 파프리카 병해 탐지 로봇 논문(Schor et al., Precision Agriculture, 2017)은 흰가루병과 TSWV를 대상으로 하며, 온실 70–80 ha마다 전담 예찰 인력 1명이 필요하다는 현황을 제시합니다. 이 수치의 맥락(국가, 작물)은 원문에서 확인해야 합니다. — [Schor et al. 2017, Precision Agriculture (s11119-017-9503-z, 미러)](https://springerlink.bibliotecabuap.elogim.com/doi/10.1007/s11119-017-9503-z) [원문 미확인]
- Ecoation 측 임원(Manotas, CRO)은 컴퓨터비전 시스템이 사람 예찰자보다 2–3일 일찍 문제를 탐지할 수 있다고 말했습니다(업계 추정치). 이 발언은 iUNU 관련 검색 결과의 업계지 기사에서 나왔으나 정확한 기사 URL은 특정하지 못했습니다. 아래 두 기사 중 하나로 추정됩니다. — [Produce Grower: Sixth sense](https://www.producegrower.com/article/sixth-sense) / [Greenhouse Grower: Computer Imaging For Early Detection](https://www.greenhousegrower.com/?p=165154) [출처 특정 미확인]

### Inferences
- 표본 예찰은 원리상 전체 식물 중 일부만 봅니다. 그래서 '전수(100%) 커버리지 + 정기 반복'이 로봇의 핵심 차별점입니다.
- 끈끈이 트랩은 날개 있는 성충만 잡으므로, 응애나 날개 없는 진딧물 같은 해충은 식물체를 직접 촬영해야 합니다. 요구사항에 잎 앞면·뒷면 촬영 또는 근접 촬영 능력을 포함할지 검토가 필요합니다(추론).

### Gaps
- 국내 시설원예 농가의 예찰 빈도, 소요 시간(시간/ha/주), 표본 비율 통계는 찾지 못했습니다.
- 수작업 예찰에서 발견이 얼마나 늦어지는지(일 수)를 측정한 독립 연구는 찾지 못했습니다(업체 추정 2–3일만 있음).

---

## 5. 자동 탐지(컴퓨터비전, 딥러닝, 초분광, 이동형 로봇 스카우팅)의 정확도·효율 개선 사례

### Takeaway
온실 토마토 숙도 탐지 논문들은 mAP@0.5 85–97.5%를 보고하고, 끈끈이 트랩 해충 자동 계수는 수작업 계수와 R² 0.96–0.996 수준으로 일치합니다. 다만 실험실 데이터셋(PlantVillage) 기준 95–99%인 병해 진단 정확도가 실제 현장에서는 70–85%로 떨어집니다. 상용 스카우팅 솔루션은 스카우팅 노동 50% 절감을 내세우지만, 대부분 업체 주장입니다.

### Cited Findings
**(a) 숙도 판정 정확도(논문)**
- S-YOLO(YOLOv8s 기반, 온실 토마토, Frontiers in Plant Science 2024): mAP 92.46%. 다른 출처는 mAP 92.1%, 45 FPS로 보고해 수치가 엇갈립니다. — [Frontiers in Plant Science 10.3389/fpls.2024.1451018](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1451018/pdf) [원문 미확인, 수치 불일치]
- SE-YOLOv3-MobileNetV1(Su et al., 2022): 토마토 숙도 분류 mAP 97.5%. 다만 모델 크기가 엣지 배포에는 부담이라고 후속 논문들이 지적합니다. — [Frontiers 2024 논문 내 인용](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1451018/epub) [원문 미확인]
- AFBF-YOLO(YOLO11n 개량, 온실 방울토마토 송이와 숙도 동시 탐지, Plants 2025): mAP@0.5 85.6%. 밀집·가림 환경을 대상으로 합니다. — [PMC12389433](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12389433/)
- YOLO26-RipeLoc Lite(arXiv 2026): 토마토 탐지, 숙도 분류, 수확점 위치 추정을 함께 수행하며 전체 mAP@0.5 92.9%(완숙 95.2%, 미숙 90.6%)입니다. — [arXiv 2605.27129](https://arxiv.org/html/2605.27129)
- 딸기 숙도: Swin Transformer + YOLOv9는 mAP@0.5 87.3%(YOLOv9 단독 86.1%, Big Data and Cognitive Computing 2024). LBS-YOLO(2025)는 mAP@0.5 88.6%, mAP@0.5:0.95 75.8%입니다. — [AUT 보고서](https://cerv.aut.ac.nz/wp-content/uploads/2024/08/ReportZhiyuan-Mi.pdf); [DOAJ: BDCC Aug 2024](https://doaj.org/article/c0ea31a344014bcd80ef9eea24bce9d1); [Frontiers fpls.2025.1584669](https://public-pages-files-2025.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2025.1584669/text) [LBS-YOLO의 정확한 논문 매칭은 원문 미확인]
- 주의: 이 수치들은 데이터셋과 지표(mAP@0.5 vs mAP@0.5:0.95)가 서로 달라 직접 비교할 수 없습니다.

**(b) 해충 자동 계수(끈끈이 트랩)**
- TPest-RCNN(Faster R-CNN 변형, 2021): 41일 동안 수작업 계수와 비교한 결정계수가 가루이 99.6%, 총채벌레 97.4%였습니다. — [X-MOL: Comput. Electron. Agric. 논문 상세](https://www.x-mol.com/paper/1365437537185263616) [원문 미확인]
- 개량 YOLOv4(ASABE): YOLOv3/v4 대비 mAP가 가루이 +8.2%p, 총채벌레 +3.4%p 높았습니다. 온실에서 2560×1920 해상도로 촬영했습니다. — [ASABE eLibrary aid=52210](https://elibrary.asabe.org/abstract.asp?aid=52210)
- Cascaded CNN(2020): 평균 계수 정확도 0.91/0.90, F1 0.92/0.90이었습니다. 별도의 6개월 데이터와 다른 온실 이미지로 검증했습니다. — [검색 결과 기준, 출처 매칭 원문 미확인](https://www.x-mol.com/paper/1365437537185263616)
- 분광잔차 + SVM(Frontiers in Plant Science 2022): 정확도 가루이 93.9%, 총채벌레 89.9%였고, 수작업 계수 대비 R²은 0.9785/0.9582였습니다. — [PMC9274131](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9274131/)
- 점 주석 기반 계수 파이프라인(Ecological Informatics 2023): 사람 계수 대비 평균 오차가 약 9%였습니다. — [AMiner: deep learning-based pipeline for whitefly abundance estimation](https://aminer.org/pub/656dd2ad939a5f4082fe158d/a-deep-learning-based-pipeline-for-whitefly-pest-abundance-estimation-on-chromotropic)

**(c) 병해 탐지: 실험실과 현장의 격차, 초분광 조기 탐지**
- 2025년 체계적 리뷰: 실험실 조건에서는 95–99%이지만 현장 배포에서는 70–85%로 성능 격차가 큽니다. — [PMC12565507: A Review on the Detection of Plant Disease Using ML and DL](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12565507/)
- 실험실 이미지로 학습한 딥러닝 모델은 현장 병해 식별에서 같은 수준으로 일반화되지 않습니다. 현장 데이터와 실험실 데이터를 섞으면 약 77–80% 수준까지 개선됐습니다(Ahmad et al., IEEE Access 2023, 옥수수). — [DOAJ: IEEE Access Jan 2023](https://doaj.org/article/e81741e8485f44b0b4f4ef55b92c95d0)
- PlantVillage에 과도하게 의존하면 성능 지표가 부풀려지고 일반화 한계가 가려집니다(Frontiers 2024 리뷰). — [Frontiers fpls.2024.1493322](https://frontiersin.org/articles/10.3389/fpls.2024.1493322/full)
- 토마토 잿빛곰팡이병 초분광(400–950 nm) 분류 정확도는 감염 1일차 86%에서 11일차 98%로 올랐습니다. 3일차부터 건전주와 감염주의 스펙트럼이 구분됐습니다. — [PMC11462246](https://pmc.ncbi.nlm.nih.gov/articles/PMC11462246)
- 육안 병징이 나타나기 최대 2일 전에 감염을 탐지했다는 결과가 있습니다(Sensors 2025, 25(14):4285). 대상 병원체는 원문에서 확인해야 합니다. — [MDPI Sensors 25(14):4285](https://mdpi.com/1424-8220/25/14/4285) [원문 미확인]
- 흰가루병: 호박에서는 초기 약 84%, 후기 약 97%였고, 오이에서는 접종 6일 후 89%였습니다. — [PMC11462246 검색 결과 기준](https://pmc.ncbi.nlm.nih.gov/articles/PMC11462246) [출처 매칭 원문 미확인]

**(d) 한국 사례**
- 농촌진흥청 AI 영상진단 서비스는 2023년부터 본격 운영 중입니다. 35작물 372종 병해충이 대상이며 2029년까지 82작목 744종으로 확대할 계획입니다. 영상 인식 정확도는 96.6%로 발표됐습니다(시험 조건 미확인). — [농촌진흥청 웹진 2025-09 Theme Insight](https://rda.go.kr/webzine/2025/09/sub_13.html); [농촌진흥청 웹진 2022-12](https://www.rda.go.kr/webzine/2022/12/sub1-6.html)
- 농진청 AI 트랩은 나방류·노린재 3종에 적용 중이며, 2027년까지 9종으로 늘리고 2029년까지 전 기종 자동화를 계획하고 있습니다. — [농촌진흥청 웹진 2025-09](https://rda.go.kr/webzine/2025/09/sub_13.html); [다음뉴스: 농진청 'K농업' 대전환 (2026-04)](https://v.daum.net/v/20260425070231485)
- 농진청은 시설 온실의 선제적 병해 진단을 위해 ICT 기반 AI 딸기 병해 진단 시스템을 개발했습니다. — [위키트리: 인공지능으로 딸기 병해 진단](https://www.wikitree.co.kr/articles/711186)
- 국내 학술 사례: 실제 시설농장에 병충해 진단 서비스를 적용한 결과 정확도 약 86%, F1 0.84, mAP 0.98로 보고됐습니다. — [KoreaScience CFKO202319254425939](https://koreascience.kr/article/CFKO202319254425939.pdf) [출처 매칭 원문 미확인]

**(e) 상용 스카우팅 솔루션**
- **Ecoation (캐나다)**: Bogaerts, Biobest와 함께 자율주행 IPM 스카우팅·수량예측 로봇(OTTO/ROYA)을 2022년에 발표했습니다. 360° 'Virtual Walk' 카메라로 온실 1㎡마다 이미지를 플랫폼에 전송하며, 주야간 모두 작동합니다. 초기에는 캐나다·유럽의 일부 온실에만 공급됐고, 현재 상용 보급 현황과 독립 현장 데이터는 확인하지 못했습니다. — [Greenhouse Grower (2022)](https://www.greenhousegrower.com/technology/new-autonomous-robot-does-the-greenhouse-scouting-for-you/); [AgriTech Tomorrow (2022-11-15)](https://www.agritechtomorrow.com/news/2022/11/15/world-meet-otto-%25E2%2580%2593-the-ipm-scouting-and-yield-forecasting-robot-for-greenhouses/14200/); [HortiDaily: OTTO](https://hortidaily.com/article/9476839/otto-the-ipm-scouting-and-yield-forecasting-greenhouse-robot)
- **Fermata Croptimus (미국)**: 고정형 카메라를 에이커당 약 4대 설치하고 컴퓨터비전으로 해충과 병을 식별합니다. CEO는 고객 중 최대 50%가 스카우팅 인력 투입을 줄였다고 말합니다. 업계지는 스카우팅 비용 50% 절감으로 보도했습니다. 2025 FRUIT LOGISTICA Innovation Award를 수상했습니다. — [The Packer: AI-powered crop monitoring](https://www.thepacker.com/news/packer-tech/ai-powered-crop-monitoring-keeps-watch-pests-and-disease); [finanzen.net: Croptimus wins 2025 FRUIT LOGISTICA Innovation Award](https://finanzen.net/nachricht/aktien/fermata-s-computer-vision-solution-croptimus-wins-the-2025-fruit-logistica-innovation-award-14257471); [NVIDIA Developer Blog](https://developer.nvidia.com/blog/ai-tool-helps-farmers-combat-crop-loss-and-climate-change)
- **Viscon EVA Scoutr (네덜란드, Fermata와 협력)**: 이동형 스카우팅 로봇으로, 화학 투입 최대 25%, 스카우팅 노동 50%, 작물 손실 30% 감소를 주장합니다(업체 주장). — [Viscon EVA brochure (2025-06)](https://viscongroup.eu/app/uploads/2025/06/EVA_A4-brochure-LQ.pdf)
- **iUNU LUNA (미국)**: 컴퓨터비전으로 작물 재고, 생육, 병해충 증상을 추적합니다. 엽채류 업체 Pure Green Farms가 원격 스카우팅과 'Time Travel'(과거 시점 식물 이미지 조회) 용도로 사용합니다. 3–5년 서비스 계약(SaaS) 모델이며, 병해충 탐지 정확도나 손실 감소 수치는 공개 자료로 확인하지 못했습니다. — [Greenhouse Grower: leafy greens grower invests in AI](https://www.greenhousegrower.com/technology/greenhouse-leafy-greens-grower-invests-in-ai-technology/?amp); [AgFunderNews: iUNU raises $7.5m](https://agfundernews.com/iunu-raises-7-5m-for-greenhouse-system-as-a-service-tech-platform); [iUNU: How it works](https://iunu.com/how-it-works)
- 연구용 사례: Schor et al.(2017)의 파프리카 병해 탐지 로봇은 흰가루병과 TSWV를 대상으로 합니다. — [Precision Agriculture s11119-017-9503-z](https://springerlink.bibliotecabuap.elogim.com/doi/10.1007/s11119-017-9503-z)

### Inferences
- 숙도 판정은 이미 논문 수준에서 mAP@0.5 90% 이상이 흔합니다. 따라서 기술 위험은 '알고리즘'보다 **현장 일반화(품종, 조명, 가림)와 엣지 실시간성**에 있습니다.
- 병해 진단은 실험실과 현장의 격차(약 15–25%p)가 크므로, 요구사항의 정확도 기준은 반드시 **현장 독립 테스트셋(대상 농장·카메라)** 에서 측정하도록 규정해야 합니다.
- 상용 솔루션은 고정 카메라형(Fermata, iUNU)과 이동 로봇형(Ecoation, Viscon EVA)으로 나뉩니다. 수확 로봇에 예찰 기능을 통합하면 '수확 동선 = 예찰 동선'이 되어 별도 장비 없이 전수 커버리지를 얻는다는 차별점이 있습니다(추론).
- Saga Robotics Thorvald와 Agrobotix는 이번 조사에서 병해충 탐지 관련 정량 자료를 확보하지 못했습니다(아래 Gaps 참고).

### Gaps
- Saga Robotics Thorvald(주로 UV-C 흰가루병 처리 로봇)와 Agrobotix에 대해서는 이번 조사 범위 안에서 탐지 성능 자료를 찾지 못했습니다.
- 파프리카와 오이의 숙도 탐지 정확도 논문 수치는 확보하지 못했습니다(토마토·딸기 중심).
- 응애, 흰가루병 잎 병징의 딥러닝 탐지 정확도(온실 현장)는 별도 검색이 필요합니다.
- 상용 솔루션의 탐지 정확도(정밀도, 재현율, 오탐률)를 독립 검증한 자료는 없습니다.

---

## 6. 비즈니스 요구사항으로 정리할 성능 지표(제안)

### Takeaway
위 근거를 종합하면 Robot A의 비전 기능 요구사항은 다음 다섯 축으로 정리할 수 있습니다. ① 숙도 탐지 정확도(현장 mAP), ② 해충 계수 정확도(수작업 대비 R²·오차), ③ 병해 현장 정확도, ④ 처리 속도(FPS·사이클 타임), ⑤ 커버리지와 탐지 선행 시간. 아래 수치는 문헌·업체 사례에서 **도출한 제안값(추론)** 이며 확정 기준이 아닙니다.

### Cited Findings
(요구사항 수치의 근거가 되는 벤치마크를 다시 정리합니다.)
- 토마토 숙도 mAP@0.5: 85.6%(밀집 방울토마토) ~ 97.5%. 완숙 클래스 95.2%. — [PMC12389433](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12389433/); [arXiv 2605.27129](https://arxiv.org/html/2605.27129)
- 실시간성: S-YOLO 45 FPS 보고(원문 미확인). — [Frontiers fpls.2024.1451018](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1451018/pdf)
- 해충 계수 정확도: 수작업 대비 R² 0.958–0.996, 계수 오차 약 9%. — [PMC9274131](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9274131/); [X-MOL TPest-RCNN](https://www.x-mol.com/paper/1365437537185263616); [AMiner](https://aminer.org/pub/656dd2ad939a5f4082fe158d/a-deep-learning-based-pipeline-for-whitefly-pest-abundance-estimation-on-chromotropic)
- 병해 현장 정확도: 70–85%(리뷰), 국내 시설농장 적용 약 86%. — [PMC12565507](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12565507/); [KoreaScience CFKO202319254425939](https://koreascience.kr/article/CFKO202319254425939.pdf)
- 조기 탐지 선행 시간: 사람보다 2–3일 빠름(업계 추정), 초분광으로 병징 2일 전 탐지, 감염 3일차부터 스펙트럼 구분. — [Produce Grower](https://www.producegrower.com/article/sixth-sense); [MDPI Sensors 25(14):4285](https://mdpi.com/1424-8220/25/14/4285); [PMC11462246](https://pmc.ncbi.nlm.nih.gov/articles/PMC11462246)
- 효율·경제 효과(업체 주장): 스카우팅 노동 −50%, 화학 투입 −25%, 작물 손실 −30%. — [Viscon EVA brochure](https://viscongroup.eu/app/uploads/2025/06/EVA_A4-brochure-LQ.pdf); [The Packer](https://www.thepacker.com/news/packer-tech/ai-powered-crop-monitoring-keeps-watch-pests-and-disease)
- 커버리지 참고: Ecoation 로봇은 온실 1㎡마다 이미지 확보, Fermata는 에이커당 고정 카메라 약 4대. — [AgriTech Tomorrow](https://www.agritechtomorrow.com/news/2022/11/15/world-meet-otto-%25E2%2580%2593-the-ipm-scouting-and-yield-forecasting-robot-for-greenhouses/14200/); [The Packer](https://www.thepacker.com/news/packer-tech/ai-powered-crop-monitoring-keeps-watch-pests-and-disease)
- 수확 사이클 참고: 선택 수확 로봇 15–24초/과실, 성공률 61–76.5%. — [WUR SWEEPER](https://research.wur.nl/en/publications/development-of-a-sweet-pepper-harvesting-robot/)

### Inferences (요구사항 초안 제안)
| 구분 | 지표 | 제안 목표값(초안) | 근거 |
|---|---|---|---|
| 숙도 판정 | 현장 테스트셋 mAP@0.5 (과실 탐지+숙도 등급) | ≥ 90% (수확 대상 완숙 클래스 정밀도 ≥ 95%) | 논문 85.6–97.5%, 완숙 95.2% |
| 숙도 판정 | 숙도 출력 형태 | 등급(예: 미숙/전환기/완숙/과숙) + 연속 숙도 점수, 농가별 임계값 설정 | 경계 구간 판정 편차 문제 |
| 숙도 판정 | 판정 일관성 | 같은 과실을 반복 촬영했을 때 판정 일치율 목표 설정(예: ≥ 95%, 값은 검증 필요) | 작업자 편차를 대체한다는 도입 명분 |
| 처리 속도 | 엣지 추론 속도 | ≥ 30 FPS 또는 과실당 판정 지연 < 수확 사이클(15–24초)의 일부 | S-YOLO 45 FPS, SWEEPER 24초 |
| 해충 탐지 | 가루이·총채벌레 계수 정확도 (수작업 대비) | R² ≥ 0.95, 계수 오차 ≤ 10% | 문헌 R² 0.958–0.996, 오차 약 9% |
| 병해 탐지 | 현장 독립 테스트셋 정확도/F1 | 정확도 ≥ 85%, F1 ≥ 0.85 (잿빛곰팡이병, 흰가루병, TYLCV 병징 우선) | 현장 70–85%, 국내 86%/F1 0.84 |
| 병해 탐지 | 오탐/미탐 정책 | 고위험 병해(TYLCV 등)는 재현율 우선(예: ≥ 90%), 의심 개체는 사람이 재확인하도록 알림 | 바이러스는 치료 불가, 조기 제거가 중요 |
| 커버리지 | 예찰 커버리지 | 전체 재배 구역의 100%를 주 n회 반복 스캔(수확 동선과 통합) | 표본 예찰의 한계, Ecoation 1㎡ 단위 |
| 조기성 | 탐지 선행 시간 | 사람 예찰 대비 ≥ 2일 조기 탐지(현장 실증으로 검증) | 업계 추정 2–3일, 초분광 2일 |
| 경제성 | 운영 효과 KPI | 스카우팅 노동 −50%, 농약 사용 −20~25% 목표(파일럿으로 검증) | Viscon/Fermata 주장 |
| 데이터 | 위치 기반 이력 | 탐지 결과를 식물·좌표 단위로 기록하고 히트맵/시계열 제공(iUNU 'Time Travel'류) | 상용 솔루션 기능 |

- 모든 정확도 지표는 '학습 데이터와 다른 농장·시즌·조명에서 수집한 독립 테스트셋'에서 측정하도록 요구사항에 명시하는 것이 바람직합니다(실험실-현장 격차 근거).

### Gaps
- 상용 솔루션이 공개한 정밀도·재현율이 없어, 상용 수준 벤치마크를 근거로 목표값을 정할 수 없습니다.
- 숙도 판정 오류가 경제적 손실로 이어지는 정도를 알 수 없어, 정확도 1%p 개선의 경제적 가치(ROI)를 계산할 수 없습니다.
- 파프리카, 오이, 엽채류 각각에 대한 품목별 목표값은 추가 문헌 조사가 필요합니다.
