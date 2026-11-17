# 작업 노트 웹페이지(GitHub Pages + Firebase) 설정

로그인 없이 주소만 알면 누구나 열 수 있는 판입니다. 내용은 claude.ai 아티팩트판과 같고,
저장소만 Firebase Firestore로 바뀝니다.

| 파일 | 역할 |
|---|---|
| `docs/index.html` | 페이지 본문. `build_pages.py`가 `robotA-workflow.html`에서 만듭니다(직접 고치지 마세요) |
| `docs/fb-shim.js` | Firestore 연결부(실시간 동기화, 이름, 접속자, 이미지, 백업) |
| `docs/firebase-config.js` | Firebase 설정값과 팀 코드 |
| `docs/firestore.rules` | Firestore 보안 규칙(콘솔에 붙여 넣기) |

## 1. Firebase 만들기 (한 번만)
1. https://console.firebase.google.com 에서 **프로젝트 추가**를 누릅니다. Google 애널리틱스는 꺼도 됩니다.
2. 왼쪽 **빌드 → Firestore Database → 데이터베이스 만들기**를 누릅니다. 위치는 `asia-northeast3 (서울)`, 모드는 **프로덕션 모드**로 고릅니다.
3. **규칙** 탭에 `docs/firestore.rules` 내용을 붙여 넣고 **게시**합니다.
4. **프로젝트 설정(톱니바퀴) → 내 앱 → 웹(</>)**을 누르고 앱 이름을 정해 등록합니다. Hosting은 체크하지 않습니다.
5. 화면에 나온 `firebaseConfig` 값을 `docs/firebase-config.js`의 `window.FIREBASE_CONFIG`에 넣습니다.

## 2. GitHub Pages 켜기
저장소 **Settings → Pages → Build and deployment**에서 Source를 `Deploy from a branch`로 고르고,
브랜치를 `ccr-93580126-w94tus`, 폴더를 `/docs`로 정한 뒤 **Save**를 누릅니다.
1~2분 뒤 `https://9697psh.github.io/finray-gripper-fea/` 에서 열립니다.

## 3. 기존 기록 옮기기
페이지 왼쪽 아래 **백업 불러오기**를 누르고, 아티팩트에서 내보낸 `작업노트_백업_아티팩트에서.json`을 고릅니다.

## 쓰는 법
- 처음 들어오면 이름을 묻습니다. 팀 코드를 설정했다면 팀 코드도 함께 묻습니다. 둘 다 이 브라우저에 저장됩니다.
- 왼쪽 아래 막대에서 이름을 바꾸거나, **백업 저장**으로 전체 기록을 JSON 파일로 내려받을 수 있습니다.
  누구나 지울 수 있는 구조이니 하루 한 번은 백업을 저장해 두세요.
- 이미지는 Storage를 쓰지 않습니다. 무료 요금제에서도 되도록, 압축해서 문서 안에 저장합니다.

## 아티팩트를 고친 뒤 웹페이지도 갱신하기
```
python3 reports/robotA_web/build_pages.py
```
위 명령으로 `docs/index.html`을 다시 만든 뒤 커밋하고 푸시하면 Pages에 반영됩니다.

## 주의
- 주소를 아는 사람은 누구나 읽고 쓸 수 있습니다. 팀 코드는 화면에서만 막는 실수 방지용입니다.
  비밀번호, 개인정보, API 키는 올리지 마세요.
- 저장소가 공개이므로 `docs/` 아래 파일도 공개됩니다(설정값은 원래 공개해도 되는 값입니다).
