#!/usr/bin/env python3
"""robotA-workflow.html(아티팩트 원본) → docs/index.html(GitHub Pages + Firebase 판).

아티팩트를 고친 뒤 이 스크립트를 다시 돌리면 웹페이지도 같은 내용으로 갱신된다.
    python3 reports/robotA_web/build_pages.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "robotA-workflow.html"
OUT = HERE.parents[1] / "docs" / "index.html"

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<script src="firebase-config.js"></script>
<script>
  // 아티팩트용 본문 코드가 기대하는 window.claude.use()를 Firebase 연결부(fb-shim.js)로 채운다.
  window.__fbReady = new Promise(function (r) { window.__fbResolve = r; });
  window.claude = { use: function (n) { return window.__fbReady.then(function (ns) { return (ns && ns[n]) || null; }); } };
</script>
<script type="module" src="fb-shim.js"></script>
<style>
.fb-gate { position: fixed; inset: 0; z-index: 90; background: rgba(10,16,12,.45); display: grid; place-items: center; padding: 16px; }
.fb-card { width: min(380px, 100%); background: var(--panel, #fff); color: var(--fg, #17201b); border: 1px solid var(--line, #d9e0d6); border-radius: 12px; padding: 20px; display: grid; gap: 12px; font-family: var(--font, sans-serif); box-shadow: 0 10px 30px rgba(0,0,0,.18); }
.fb-card h2 { margin: 0; font-size: 18px; }
.fb-card p { margin: 0; font-size: 13px; color: var(--muted, #5b6a61); }
.fb-card label { display: grid; gap: 4px; font-size: 13px; color: var(--muted, #5b6a61); }
.fb-card input { font: inherit; font-size: 15px; padding: 9px 10px; border: 1px solid var(--line, #d9e0d6); border-radius: 8px; background: var(--bg, #f4f6f3); color: var(--fg, #17201b); }
.fb-card button { font: inherit; font-weight: 600; padding: 10px; border: 0; border-radius: 8px; background: var(--accent, #2f8a5a); color: var(--accent-ink, #fff); cursor: pointer; }
.fb-card .fb-err { color: var(--bad, #c0392b); }
.fb-bar { position: fixed; left: 12px; bottom: calc(12px + env(safe-area-inset-bottom, 0px)); z-index: 35; display: flex; flex-wrap: wrap; align-items: center; gap: 6px; max-width: calc(100% - 24px); background: var(--panel, #fff); border: 1px solid var(--line, #d9e0d6); border-radius: 10px; padding: 5px 6px 5px 10px; font-family: var(--font, sans-serif); font-size: 12px; color: var(--muted, #5b6a61); box-shadow: 0 2px 10px rgba(0,0,0,.08); }
.fb-bar button { font: inherit; font-size: 12px; padding: 4px 8px; border: 1px solid var(--line, #d9e0d6); border-radius: 6px; background: var(--panel-2, #eef2ec); color: var(--fg, #17201b); cursor: pointer; }
body { padding-bottom: 56px; }
</style>
"""

# 아티팩트 전용 문구 → 웹페이지용 문구
REPLACE = [
    ('<meta name="claude:viewport-fit-sides" content="cover">\n', ''),
    ("toast('이 계정은 기록을 저장할 권한이 없습니다. 공유 설정에서 참여자 이상 권한이 필요합니다.')",
     "toast('저장 권한이 없습니다. 왼쪽 아래 [팀 코드 입력]에서 팀 코드를 넣어 주세요.')"),
    ("'<div class=\"notice\">보기 전용입니다. 기록을 남기려면 공유 설정에서 참여자(Contributor) 이상 권한을 받아야 합니다.</div>'",
     "'<div class=\"notice\">보기 전용입니다. 기록을 남기려면 왼쪽 아래 [팀 코드 입력]에서 팀 코드를 넣어 주세요.</div>'"),
    ("'<div class=\"notice warn\">공유 저장소를 쓸 수 없는 화면입니다(로그인하지 않았거나 권한이 없음). 기록 보기·저장이 막혀 있습니다.</div>'",
     "(window.__fbStatus === 'noconfig' ? '<div class=\"notice warn\">아직 공유 저장소(Firebase)가 연결되지 않았습니다. docs/firebase-config.js에 firebaseConfig를 넣어 주세요.</div>' : '<div class=\"notice warn\">공유 저장소(Firebase)에 연결하지 못했습니다. 인터넷 연결이나 firebase-config.js 설정을 확인한 뒤 새로고침하세요.</div>')"),
]


def main():
    html = SRC.read_text(encoding="utf-8")
    for old, new in REPLACE:
        if old not in html:
            raise SystemExit(f"치환할 문구를 찾지 못했습니다: {old[:60]}...")
        html = html.replace(old, new, 1)
    title_end = html.index("</style>") + len("</style>")
    out = HEAD + html[:title_end] + "\n</head>\n<body>\n" + html[title_end:].lstrip("\n") + "\n</body>\n</html>\n"
    OUT.write_text(out, encoding="utf-8")
    print(f"wrote {OUT} ({len(out):,} bytes)")


if __name__ == "__main__":
    main()
