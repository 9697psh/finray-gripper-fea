// Firebase 콘솔 → 프로젝트 설정 → 내 앱(웹)에서 보이는 firebaseConfig 값을 그대로 붙여 넣으세요.
// 이 값은 원래 웹페이지에 공개로 들어가는 값입니다(비밀번호 아님). 실제 접근 제어는 firestore.rules가 합니다.
window.FIREBASE_CONFIG = null;
// 예:
// window.FIREBASE_CONFIG = {
//   apiKey: "AIza...",
//   authDomain: "my-project.firebaseapp.com",
//   projectId: "my-project",
//   storageBucket: "my-project.appspot.com",
//   messagingSenderId: "1234567890",
//   appId: "1:1234567890:web:abcdef"
// };

// 팀 코드(선택): 비워 두면 누구나 수정할 수 있습니다.
// 넣으면 처음 들어올 때 팀 코드를 물어보고, 모르는 사람은 보기만 할 수 있습니다.
// 코드 원문이 아니라 SHA-256 값을 넣습니다. 예) 터미널에서:  printf '%s' '우리팀코드' | sha256sum
// 주의: 화면에서 막는 장치일 뿐 보안 장치는 아닙니다(실수 방지용).
window.EDIT_CODE_SHA256 = '';
