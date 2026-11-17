// Firebase(Firestore) 연결부.
// 페이지 본문(index.html)은 claude.ai 아티팩트와 같은 코드를 쓰고,
// 여기서 같은 모양의 db / user / assets / downloads / room 객체를 Firestore로 만들어 넘긴다.
const SDK = window.FIREBASE_SDK_BASE || 'https://www.gstatic.com/firebasejs/10.12.2/';
const COLLS = ['tasks', 'refs', 'attempts', 'logs', 'media', 'interfaces', 'code', 'commands', 'settings', 'todos', 'notes', 'codeVersions', 'cmdSets', 'users'];
const ready = window.__fbResolve || (() => {});

const LS = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
};
const rand = n => Array.from(crypto.getRandomValues(new Uint8Array(n)), b => 'abcdefghijklmnopqrstuvwxyz0123456789'[b % 36]).join('');
const escH = v => String(v ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
async function sha256(s) {
  const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return Array.from(new Uint8Array(b), x => x.toString(16).padStart(2, '0')).join('');
}

const CFG = window.FIREBASE_CONFIG;
if (!CFG || !CFG.projectId) { window.__fbStatus = 'noconfig'; ready({}); }
else boot().catch(e => { console.error('[firebase]', e); window.__fbStatus = 'error'; ready({}); });

async function boot() {
  const [A, F] = await Promise.all([import(SDK + 'firebase-app.js'), import(SDK + 'firebase-firestore.js')]);
  const app = A.initializeApp(CFG);
  const fs = F.initializeFirestore(app, { ignoreUndefinedProperties: true });

  // ---------- 나(이름·팀 코드) ----------
  let me = LS.get('fb_uid');
  if (!me) { me = 'w_' + rand(20); LS.set('fb_uid', me); }
  const CODE = (window.EDIT_CODE_SHA256 || '').toLowerCase();
  let canWrite = !CODE;
  if (CODE) canWrite = (LS.get('fb_code') || '') === CODE;
  let nameP = null;
  function askName(force) {
    if (!force && LS.get('fb_name') && (!CODE || canWrite || LS.get('fb_viewonly') === '1')) return Promise.resolve();
    return new Promise(res => {
      const wrap = document.createElement('div');
      wrap.className = 'fb-gate';
      wrap.innerHTML = `<form class="fb-card">
        <h2>수확 로봇 작업 노트</h2>
        <p>기록에 표시될 이름을 적어 주세요. 이 브라우저에 저장됩니다.</p>
        <label>이름<input name="n" maxlength="20" required placeholder="예: 용현" value="${escH(LS.get('fb_name') || '')}"></label>
        ${CODE ? '<label>팀 코드<input name="c" type="password" autocomplete="off" placeholder="비우면 보기만 가능"></label><p class="fb-err" hidden>팀 코드가 맞지 않습니다.</p>' : ''}
        <button type="submit">시작</button></form>`;
      document.body.appendChild(wrap);
      const f = wrap.querySelector('form');
      setTimeout(() => f.n.focus(), 30);
      f.addEventListener('submit', async e => {
        e.preventDefault();
        const n = f.n.value.trim().slice(0, 20); if (!n) return;
        if (CODE) {
          const c = f.c.value.trim();
          if (c) {
            const h = await sha256(c);
            if (h !== CODE) { f.querySelector('.fb-err').hidden = false; return; }
            LS.set('fb_code', h); LS.set('fb_viewonly', '0'); canWrite = true;
          } else { LS.set('fb_viewonly', '1'); canWrite = false; }
        }
        LS.set('fb_name', n);
        wrap.remove();
        F.setDoc(F.doc(fs, 'users', me), { name: n, updatedAt: new Date().toISOString() }, { merge: true }).catch(() => {});
        res();
      });
    });
  }
  nameP = askName(false).then(() => {
    if (canWrite) F.setDoc(F.doc(fs, 'users', me), { name: LS.get('fb_name'), updatedAt: new Date().toISOString() }, { merge: true }).catch(() => {});
  });

  const names = {};
  let usersLoaded;
  const usersReady = new Promise(r => { usersLoaded = r; });
  F.onSnapshot(F.collection(fs, 'users'), snap => { snap.docs.forEach(d => { names[d.id] = d.data().name || '팀원'; }); usersLoaded(); }, () => usersLoaded());
  setTimeout(usersLoaded, 4000);

  const user = Object.freeze({
    async id() { await nameP; return me; },
    async can() { await nameP; return canWrite; },
    async profiles(ids) { await usersReady; const out = {}; (ids || []).forEach(id => { out[id] = { name: id === me ? (LS.get('fb_name') || names[id] || '나') : (names[id] || '팀원') }; }); return out; },
  });

  // ---------- db ----------
  const mapErr = e => {
    const code = e && e.code;
    const x = new Error(e && e.message || 'write failed');
    x.code = code === 'permission-denied' ? 'invalid_argument' : code === 'resource-exhausted' ? 'quota_exceeded' : code || 'unknown';
    return x;
  };
  const guard = fn => async (...a) => { if (!canWrite) { const x = new Error('read only'); x.code = 'invalid_argument'; throw x; } try { return await fn(...a); } catch (e) { throw mapErr(e); } };
  const docW = ref => Object.freeze({
    id: ref.id,
    set: guard(d => F.setDoc(ref, d)),
    update: guard(d => F.updateDoc(ref, d)),
    delete: guard(() => F.deleteDoc(ref)),
  });
  const db = Object.freeze({
    collection(name) {
      const c = F.collection(fs, name);
      return Object.freeze({
        add: guard(async d => docW(await F.addDoc(c, d))),
        doc: id => docW(id ? F.doc(c, id) : F.doc(c)),
        onSnapshot: (cb, err) => F.onSnapshot(c, cb, err),
      });
    },
    doc: path => docW(F.doc(fs, path)),
  });

  // ---------- 이미지(Storage 대신 문서에 압축해 저장) ----------
  async function shrink(file) {
    const url = URL.createObjectURL(file);
    try {
      const img = await new Promise((res, rej) => { const i = new Image(); i.onload = () => res(i); i.onerror = rej; i.src = url; });
      for (const [max, q] of [[1600, 0.82], [1280, 0.75], [1000, 0.7], [800, 0.6]]) {
        const s = Math.min(1, max / Math.max(img.width, img.height));
        const cv = document.createElement('canvas'); cv.width = Math.round(img.width * s); cv.height = Math.round(img.height * s);
        const g = cv.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, cv.width, cv.height); g.drawImage(img, 0, 0, cv.width, cv.height);
        const d = cv.toDataURL('image/jpeg', q);
        if (d.length < 850000) return d;
      }
      const x = new Error('too large'); x.code = 'too_large'; throw x;
    } finally { URL.revokeObjectURL(url); }
  }
  const assets = Object.freeze({ async upload(file) { if (!canWrite) { const x = new Error('read only'); x.code = 'invalid_argument'; throw x; } return { id: 'img_' + rand(12), url: await shrink(file) }; } });

  // ---------- 파일 저장 ----------
  function saveFile(filename, data, type) {
    const blob = data instanceof Blob ? data : new Blob([data], { type: type || 'text/plain;charset=utf-8' });
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = filename || 'download.txt';
    document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  }
  const downloads = Object.freeze({ async save(o) { saveFile(o.filename, o.data, o.mimeType); return { ok: true }; } });

  // ---------- 지금 접속한 사람 ----------
  const peer = 'p_' + rand(10);
  let mine = {}, raw = [], list = [];
  const subs = new Set();
  const STALE = 75e3;
  const myRef = F.doc(fs, 'presence', peer);
  const beat = () => (document.visibilityState === 'hidden' ? Promise.resolve() : nameP.then(() => F.setDoc(myRef, { by: me, presence: mine, at: Date.now() })).catch(() => {}));
  function recompute() {
    const now = Date.now();
    list = raw.filter(p => now - (p.at || 0) < STALE).map(p => ({ peer: p.id, by: p.by, kind: 'viewer', isMe: p.id === peer, presence: p.presence || {} }));
    if (!list.some(p => p.isMe)) list.push({ peer, by: me, kind: 'viewer', isMe: true, presence: mine });
    subs.forEach(cb => { try { cb({ peers: list }); } catch (e) {} });
    raw.filter(p => now - (p.at || 0) > 10 * 60e3).slice(0, 5).forEach(p => F.deleteDoc(F.doc(fs, 'presence', p.id)).catch(() => {}));
  }
  F.onSnapshot(F.collection(fs, 'presence'), s => { raw = s.docs.map(d => ({ id: d.id, ...d.data() })); recompute(); }, () => {});
  setInterval(() => { beat(); recompute(); }, 30e3);
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') beat(); });
  window.addEventListener('pagehide', () => { F.deleteDoc(myRef).catch(() => {}); });
  const room = Object.freeze({
    presence(p) { mine = p || {}; return beat(); },
    peers: () => list,
    onPeers(cb) { subs.add(cb); return () => subs.delete(cb); },
  });

  // ---------- 아래쪽 도구 막대: 이름 바꾸기 · 백업 ----------
  async function backup() {
    const out = { exportedAt: new Date().toISOString(), collections: {} };
    for (const c of COLLS) {
      const s = await F.getDocs(F.collection(fs, c));
      out.collections[c] = {}; s.docs.forEach(d => { out.collections[c][d.id] = d.data(); });
    }
    const t = new Date(Date.now() + 9 * 3600e3).toISOString().slice(0, 16).replace(/[-:T]/g, '');
    saveFile(`작업노트_백업_${t}.json`, JSON.stringify(out, null, 1), 'application/json');
  }
  async function restore(file) {
    const j = JSON.parse(await file.text());
    const cols = j.collections || j;
    let n = 0, batch = F.writeBatch(fs), inBatch = 0;
    for (const c of Object.keys(cols)) {
      if (!COLLS.includes(c)) continue;
      for (const [id, d] of Object.entries(cols[c] || {})) {
        batch.set(F.doc(fs, c, id), d); n++; inBatch++;
        if (inBatch >= 400) { await batch.commit(); batch = F.writeBatch(fs); inBatch = 0; }
      }
    }
    if (inBatch) await batch.commit();
    return n;
  }
  const bar = document.createElement('div');
  bar.className = 'fb-bar';
  const drawBar = () => {
    bar.innerHTML = `<span>${escH(LS.get('fb_name') || '')}${canWrite ? '' : ' · 보기 전용'}</span>
      <button data-fb="name">${CODE && !canWrite ? '팀 코드 입력' : '이름 바꾸기'}</button>
      <button data-fb="backup">백업 저장</button>
      ${canWrite ? '<button data-fb="restore">백업 불러오기</button>' : ''}`;
  };
  nameP.then(() => { drawBar(); document.body.appendChild(bar); });
  bar.addEventListener('click', async e => {
    const b = e.target.closest('[data-fb]'); if (!b) return;
    const k = b.dataset.fb;
    if (k === 'name') { const was = canWrite; await askName(true); drawBar(); if (was !== canWrite) location.reload(); }
    if (k === 'backup') { b.disabled = true; try { await backup(); } catch (err) { alert('백업하지 못했습니다: ' + (err && err.message)); } b.disabled = false; }
    if (k === 'restore') {
      const inp = document.createElement('input'); inp.type = 'file'; inp.accept = '.json,application/json'; inp.hidden = true;
      document.body.appendChild(inp);
      inp.onchange = async () => {
        const f = inp.files[0]; inp.remove(); if (!f) return;
        if (!confirm('백업 파일의 내용을 저장소에 덮어씁니다. 같은 ID의 기록은 백업 내용으로 바뀌고, 백업에 없는 기록은 그대로 남습니다. 계속할까요?')) return;
        try { const n = await restore(f); alert(`${n}개 기록을 불러왔습니다.`); } catch (err) { alert('불러오지 못했습니다: ' + (err && err.message)); }
      };
      inp.click();
    }
  });

  window.__fbStatus = 'ok';
  ready({ db, user, assets, downloads, room });
}
