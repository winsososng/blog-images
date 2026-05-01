# CLAUDE.md — 수학 블로그 HTML 빌더

## 🎯 역할 정의

너는 수학 교육 블로그 **"변호사아빠의 수학특강"** (fafamath.tistory.com)의 **프론트엔드 빌더**야.
input 폴더에 있는 마스터원고(md)와 이미지를 받아서, 티스토리에 바로 붙여넣을 수 있는 **고품질 HTML**을 만드는 게 네 일이야.

---

## 📂 폴더 구조

```
C:\Claude_Code\blog\
├── input/              ← 사용자가 넣는 재료
│   ├── work_order.md   ← 건별 작업지시서 (매번 달라짐)
│   ├── master_*.md     ← 마스터원고 (Phase 3 산출물)
│   └── images/         ← 이미지 파일들
│
├── output/             ← 네가 만드는 결과물
│   ├── post_고1.html   ← 완성된 HTML
│   ├── post_고3.html   ← 완성된 HTML
│   └── assets/         ← 필요시 추가 리소스
│
└── CLAUDE.md           ← 이 파일 (항상 적용되는 기본 룰)
```

---

## 🔧 작업 프로세스

```
1. work_order.md 읽기 (건별 지시사항 확인)
2. input/ 폴더 스캔 (마스터원고 + 이미지 확인)
3. 마스터원고 파싱 (섹션, 수식, 표, 이미지 위치 파악)
4. HTML 생성 (이 문서의 규칙 + work_order 지시 반영)
5. output/ 폴더에 저장
6. 결과 보고
```

---

## 🌐 티스토리 기술 환경

| 항목 | 설정 |
|:---|:---|
| 플랫폼 | 티스토리 (tistory.com) |
| 수식 렌더링 | MathJax 3.x (`<head>`에 설치 완료) |
| 입력 방식 | 에디터 → **HTML 모드**에서 통째로 붙여넣기 |
| 제약 | 외부 JS 파일 임포트 불가, 인라인 `<script>` + `<style>` 사용 |
| 이미지 | 티스토리 에디터에서 별도 업로드 (HTML에는 플레이스홀더) |

### ⚠️ 티스토리 제약사항

- **외부 CDN**: MathJax만 가능 (이미 `<head>`에 있음). 다른 CDN 사용 금지
- **인라인 스크립트**: `<script>` 태그 안에 직접 작성 OK
- **인라인 스타일**: `<style>` 태그 안에 직접 작성 OK
- **프레임워크 금지**: React, Vue 등 사용 불가. 순수 HTML/CSS/JS만
- **이미지 경로**: `<!-- [IMAGE: 파일명.png] -->` 플레이스홀더 사용
  - 사용자가 티스토리 에디터에서 수동 교체

---

## 🎨 디자인 시스템

### 컬러 팔레트

```css
:root {
  /* ── Primary ── */
  --color-primary: #2563EB;        /* 메인 블루 - 신뢰, 수학적 정밀함 */
  --color-primary-light: #3B82F6;
  --color-primary-dark: #1D4ED8;
  --color-primary-bg: #EFF6FF;     /* 블루 배경 (아주 연한) */

  /* ── Accent ── */
  --color-accent: #F59E0B;         /* 앰버/골드 - 핵심 강조, "아하!" 모먼트 */
  --color-accent-light: #FCD34D;
  --color-accent-dark: #D97706;
  --color-accent-bg: #FFFBEB;

  /* ── Semantic ── */
  --color-success: #10B981;        /* 정답, 확인, 패턴 발견 */
  --color-danger: #EF4444;         /* 주의, 함정, 오답 */
  --color-warning: #F97316;        /* 경고, 실수 유발 */
  --color-info: #6366F1;           /* 팁, 보충 설명 */

  /* ── Neutral ── */
  --color-text: #1E293B;           /* 본문 텍스트 */
  --color-text-secondary: #64748B; /* 보조 텍스트 */
  --color-text-muted: #94A3B8;     /* 약한 텍스트 */
  --color-bg: #FFFFFF;             /* 기본 배경 */
  --color-bg-subtle: #F8FAFC;      /* 미묘한 배경 */
  --color-bg-card: #FFFFFF;        /* 카드 배경 */
  --color-border: #E2E8F0;         /* 기본 테두리 */
  --color-border-strong: #CBD5E1;  /* 강한 테두리 */

  /* ── 고3 전용 (출제자 관점) ── */
  --color-examiner: #7C3AED;       /* 보라 - 출제자 시선 */
  --color-examiner-light: #8B5CF6;
  --color-examiner-bg: #F5F3FF;
  --color-trap: #DC2626;           /* 함정 강조 */
  --color-trap-bg: #FEF2F2;
}
```

### 타이포그래피

```css
:root {
  /* ── 폰트 패밀리 ── */
  --font-heading: 'Pretendard', -apple-system, sans-serif;
  --font-body: 'Pretendard', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'D2Coding', monospace;
  --font-accent: 'RIDIBatang', 'Noto Serif KR', serif; /* 강조 인용구 */

  /* ── 폰트 크기 ── */
  --text-xs: 0.75rem;     /* 12px */
  --text-sm: 0.875rem;    /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.125rem;    /* 18px - 본문 기본 */
  --text-xl: 1.25rem;     /* 20px */
  --text-2xl: 1.5rem;     /* 24px */
  --text-3xl: 1.875rem;   /* 30px */
  --text-4xl: 2.25rem;    /* 36px - 포스트 제목 */

  /* ── 행간 ── */
  --leading-tight: 1.4;
  --leading-normal: 1.8;  /* 본문 기본 행간 */
  --leading-relaxed: 2.0;

  /* ── 자간 ── */
  --tracking-tight: -0.02em;
  --tracking-normal: -0.01em;
  --tracking-wide: 0.02em;
}
```

### 간격 시스템

```css
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */

  /* ── 섹션 간격 ── */
  --section-gap: var(--space-16);      /* 섹션 사이 */
  --paragraph-gap: var(--space-6);     /* 문단 사이 */
  --element-gap: var(--space-4);       /* 요소 사이 */

  /* ── 컨테이너 ── */
  --content-width: 720px;              /* 본문 최대 너비 */
  --content-padding: var(--space-6);   /* 좌우 패딩 */

  /* ── 둥근 모서리 ── */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;

  /* ── 그림자 ── */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
  --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
  --shadow-glow: 0 0 20px rgba(37,99,235,0.15); /* 블루 글로우 */
}
```

### Pretendard 폰트 로딩

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" />
```

> ⚠️ Pretendard CDN은 티스토리에서 사용 가능. `<head>`에 이미 추가되어 있다면 생략.
> 로딩 확인이 안 되면 fallback으로 시스템 폰트 사용.

---

## 🎬 애니메이션 시스템

### 1. 스크롤 등장 애니메이션 (Intersection Observer)

모든 주요 섹션은 스크롤 시 **fade-in + slide-up** 효과로 등장한다.

```html
<style>
/* ── 스크롤 등장 ── */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* 딜레이 변형 */
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('.reveal').forEach(function(el) {
    observer.observe(el);
  });
});
</script>
```

**적용 대상**: `<section>`, `<h2>`, 주요 카드, 표, 수식 블록

### 2. 수식 하이라이트 / 강조 애니메이션

핵심 수식이 화면에 들어오면 **글로우 + 배경색 펄스** 효과.

```css
/* ── 수식 강조 ── */
.math-highlight {
  display: block;
  padding: var(--space-6) var(--space-8);
  margin: var(--space-8) 0;
  background: var(--color-primary-bg);
  border-left: 4px solid var(--color-primary);
  border-radius: var(--radius-md);
  position: relative;
  overflow: hidden;
}

.math-highlight.visible {
  animation: mathGlow 1.5s ease-out;
}

@keyframes mathGlow {
  0% { box-shadow: 0 0 0 rgba(37,99,235,0); }
  30% { box-shadow: 0 0 30px rgba(37,99,235,0.2); }
  100% { box-shadow: var(--shadow-sm); }
}

/* 핵심 공식 - 더 강한 강조 */
.math-hero {
  text-align: center;
  padding: var(--space-8) var(--space-10);
  background: linear-gradient(135deg, var(--color-primary-bg), #F0F4FF);
  border: 2px solid var(--color-primary);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}
```

### 3. 인터랙티브 표 (hover 효과)

```css
/* ── 인터랙티브 표 ── */
.table-interactive {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

.table-interactive th {
  background: var(--color-primary);
  color: white;
  padding: var(--space-3) var(--space-4);
  font-weight: 600;
  text-align: center;
}

.table-interactive td {
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--color-border);
  transition: background 0.2s ease, transform 0.2s ease;
  text-align: center;
}

.table-interactive tbody tr:hover td {
  background: var(--color-primary-bg);
  transform: scale(1.01);
}

/* 패턴 발견 행 강조 */
.table-interactive tr.pattern-found td {
  background: var(--color-accent-bg);
  font-weight: 600;
}
```

### 4. 아코디언 / 펼치기

```html
<style>
.accordion {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  margin: var(--space-6) 0;
}

.accordion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-6);
  background: var(--color-bg-subtle);
  cursor: pointer;
  font-weight: 600;
  user-select: none;
  transition: background 0.2s ease;
}

.accordion-header:hover {
  background: var(--color-border);
}

.accordion-icon {
  transition: transform 0.3s ease;
  font-size: 1.2em;
}

.accordion.open .accordion-icon {
  transform: rotate(180deg);
}

.accordion-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease-out, padding 0.3s ease;
  padding: 0 var(--space-6);
}

.accordion.open .accordion-body {
  max-height: 2000px;
  padding: var(--space-6);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.accordion-header').forEach(function(header) {
    header.addEventListener('click', function() {
      this.parentElement.classList.toggle('open');
    });
  });
});
</script>
```

**주 사용처**: 출제자 의도 섹션 (고3용), 상세 풀이 과정, 보충 설명

### 5. 탭 컴포넌트

```html
<style>
.tabs {
  margin: var(--space-8) 0;
}

.tab-buttons {
  display: flex;
  border-bottom: 2px solid var(--color-border);
  gap: 0;
}

.tab-btn {
  padding: var(--space-3) var(--space-6);
  border: none;
  background: none;
  cursor: pointer;
  font-weight: 500;
  color: var(--color-text-secondary);
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  transition: all 0.2s ease;
  font-size: var(--text-base);
}

.tab-btn.active {
  color: var(--color-primary);
  border-bottom-color: var(--color-primary);
  font-weight: 700;
}

.tab-btn:hover:not(.active) {
  color: var(--color-text);
  background: var(--color-bg-subtle);
}

.tab-panel {
  display: none;
  padding: var(--space-6) 0;
  animation: fadeIn 0.3s ease;
}

.tab-panel.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.tab-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var tabGroup = this.closest('.tabs');
      tabGroup.querySelectorAll('.tab-btn').forEach(function(b) { b.classList.remove('active'); });
      tabGroup.querySelectorAll('.tab-panel').forEach(function(p) { p.classList.remove('active'); });
      this.classList.add('active');
      tabGroup.querySelector('#' + this.dataset.tab).classList.add('active');
    });
  });
});
</script>
```

### 6. 칠판 판서 애니메이션 (Chalkboard Handwriting) ⭐

> **모든 블로그 포스트에 공통 적용!**
> 핵심 문장을 선생님이 칠판에 판서하는 느낌으로 보여주는 시스템.
> 스크롤로 뷰포트에 들어오면 자동 트리거.

#### 필수 폰트 로딩

```html
<link href="https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Nanum+Pen+Script&family=Hi+Melody&display=swap" rel="stylesheet">
```

#### 칠판 컨테이너 스타일

```css
/* ── 칠판 배경 ── */
.chalkboard {
  background: linear-gradient(170deg, #2e4a3a 0%, #243832 40%, #1e3028 100%);
  border-radius: var(--radius-lg);
  padding: var(--space-8) var(--space-8) var(--space-12);
  position: relative;
  overflow: hidden;
}

/* 칠판 텍스처 (노이즈) */
.chalkboard::before {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg width='200' height='200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.65' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  border-radius: var(--radius-lg);
}

/* ── 분필 받침대 ── */
.chalk-tray {
  position: absolute;
  bottom: 8px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  opacity: 0.45;
}

.chalk-tray-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
```

#### 4색 분필 시스템

```css
/* ── 분필 색상 (글자별 적용) ── */
/* 흰색: 기본 설명 */
.chalk-w .ch {
  color: rgba(235, 230, 220, 0.88);
  text-shadow: 1px 1px 2px rgba(235,230,220,0.08), -0.5px 0 1px rgba(235,230,220,0.05);
}

/* 노란색: 핵심 강조, "아하!" 포인트 */
.chalk-y .ch {
  color: rgba(252, 211, 77, 0.9);
  text-shadow: 1px 1px 2px rgba(252,211,77,0.08);
}

/* 빨간색: 주의, 함정, 위험 */
.chalk-r .ch {
  color: rgba(248, 113, 113, 0.88);
  text-shadow: 1px 1px 2px rgba(248,113,113,0.08);
}

/* 파란색: 공식, 단계, 보조 강조 */
.chalk-b .ch {
  color: rgba(147, 197, 253, 0.88);
  text-shadow: 1px 1px 2px rgba(147,197,253,0.08);
}
```

#### 글자별 자연스러운 손글씨 효과

핵심: **글자 하나하나를 `<span class="ch">`로 감싸고**, 각각에 미세한 회전/크기/위치 변동을 줌.

```css
.chalk-row {
  font-size: 22px;
  line-height: 2.1;
  margin-bottom: 0.5rem;
  position: relative;
  white-space: pre-wrap;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
}

.ch {
  display: inline-block;
  opacity: 0;
  font-family: 'Nanum Pen Script', 'Hi Melody', 'Gaegu', cursive;
}

.ch.on {
  opacity: 1;
}
```

```javascript
// 글자 스팬 생성 시 자연스러움 적용
function makeCharSpans(container, text, size, bold) {
  var spans = [];
  for (var i = 0; i < text.length; i++) {
    var sp = document.createElement('span');
    sp.className = 'ch';
    sp.textContent = text[i];
    if (size) sp.style.fontSize = size + 'px';
    if (bold) sp.style.fontWeight = '700';

    // ★ 핵심: 글자마다 미세한 변동
    var rot = (Math.random() - 0.5) * 2.5;   // 회전: ±2.5도
    var scl = 0.97 + Math.random() * 0.06;    // 크기: 97~103%
    var ty = (Math.random() - 0.5) * 1.5;     // 수직: ±1.5px
    sp.style.transform = 'rotate(' + rot + 'deg) scale(' + scl + ') translateY(' + ty + 'px)';

    if (text[i] === ' ') sp.style.width = '0.3em';
    container.appendChild(sp);
    spans.push(sp);
  }
  return spans;
}
```

#### 타이핑 애니메이션 + 분필 가루

```javascript
// 글자 순차 등장 (32ms/글자 = 적당히 빠른 속도)
function animateChars(spans, speed, dustColor) {
  return new Promise(function(resolve) {
    var i = 0;
    var iv = setInterval(function() {
      if (i < spans.length) {
        spans[i].classList.add('on');
        // 3글자마다 분필 가루 생성
        if (i % 3 === 0 && spans[i].textContent !== ' ') {
          spawnDust(spans[i], dustColor);
        }
        i++;
      } else {
        clearInterval(iv);
        resolve();
      }
    }, speed);
  });
}

// 분필 가루 파티클
function spawnDust(charEl, color) {
  var rect = charEl.getBoundingClientRect();
  var bdRect = board.getBoundingClientRect();
  for (var i = 0; i < 2; i++) {
    var d = document.createElement('div');
    d.className = 'chalk-dust';
    var sz = 1.5 + Math.random() * 2;
    d.style.width = sz + 'px';
    d.style.height = sz + 'px';
    d.style.background = color;
    d.style.left = (rect.right - bdRect.left) + 'px';
    d.style.top = (rect.bottom - bdRect.top - 6) + 'px';
    d.style.setProperty('--dx', (Math.random() * 10 - 5) + 'px');
    d.style.setProperty('--dy', (4 + Math.random() * 8) + 'px');
    board.appendChild(d);
    setTimeout(function(el) {
      return function() { if (el.parentNode) el.parentNode.removeChild(el); };
    }(d), 1300);
  }
}
```

```css
.chalk-dust {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  animation: dustFall 1.2s ease-out forwards;
}

@keyframes dustFall {
  0% { opacity: 0.5; transform: translate(0, 0); }
  100% { opacity: 0; transform: translate(var(--dx), var(--dy)); }
}
```

#### 밑줄 긋기 효과

```css
.chalk-underline-draw {
  position: absolute;
  bottom: 2px;
  left: 0;
  height: 3px;
  border-radius: 2px;
  opacity: 0.5;
  width: 0;
  transition: width 0.6s ease-out;
}
/* JS에서 width를 100%로 변경하면 밑줄이 그어짐 */
```

#### 점선 박스 강조

```css
.chalk-box {
  border: 2.5px dashed rgba(252, 211, 77, 0.3);
  border-radius: 10px;
  padding: 1rem 1.4rem;
  margin: 0.6rem 0 1rem;
  text-align: center;
  font-family: 'Nanum Pen Script', cursive;
}
```

#### 스크롤 트리거 연동

블로그 포스트에서는 버튼 대신 **Intersection Observer로 자동 트리거**:

```javascript
// 칠판 블록이 화면에 들어오면 판서 시작
var chalkObserver = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting && !entry.target.dataset.played) {
      entry.target.dataset.played = 'true';
      runChalkboard(entry.target); // 해당 칠판의 판서 시작
    }
  });
}, { threshold: 0.3 });

document.querySelectorAll('.chalkboard').forEach(function(el) {
  chalkObserver.observe(el);
});
```

#### 판서 스크립트 데이터 형식

```javascript
// work_order.md에서 지정한 판서 내용을 이 형식으로 변환
var chalkScript = [
  { type: 'line', color: 'chalk-y', text: '★ 핵심 메시지', size: 26, bold: true },
  { type: 'pause', ms: 300 },
  { type: 'line', color: 'chalk-w', text: '설명 텍스트', size: 21 },
  { type: 'box', color: 'chalk-y', main: '박스 메시지', sub: '보조 설명', underline: true },
  { type: 'line', color: 'chalk-r', text: '⚠ 주의 메시지', size: 20 },
  { type: 'line', color: 'chalk-b', text: '공식/단계', size: 20, underline: true },
];
```

#### 판서 속도 가이드

| 항목 | 값 | 비고 |
|:---|:---|:---|
| 글자 등장 속도 | **32ms/글자** | 빠르지만 읽을 수 있는 속도 |
| 줄 사이 대기 | **250~400ms** | 내용에 따라 조절 |
| 밑줄 긋기 | **0.6s ease-out** | 부드럽게 |
| 박스 등장 | **opacity 0.3s** | 자연스럽게 |
| 분필 가루 빈도 | **3글자마다 2개** | 너무 많지 않게 |

#### 판서 내용 결정 기준

| 상황 | 판서 내용 |
|:---|:---|
| **도입부** | 오늘의 핵심 메시지 예고 |
| **핵심 원리** | "~의 본질은 ~이다" 류 문장 |
| **공식 소개** | 최종 공식 또는 방법론 단계 |
| **주의사항** | 함정, 실수 유발 포인트 (빨간 분필) |
| **정리** | 오늘 배운 것 요약 |

> ⚠️ **과용 금지**: 한 포스트에 판서 블록 **1~3개**가 적당. 남발하면 효과 반감.

---

## 📐 콘텐츠 컴포넌트

### 섹션 헤더

```html
<section class="reveal">
  <div class="section-header">
    <span class="section-number">01</span>
    <h2 class="section-title">섹션 제목</h2>
  </div>
  <!-- 섹션 내용 -->
</section>
```

```css
.section-header {
  display: flex;
  align-items: baseline;
  gap: var(--space-4);
  margin-bottom: var(--space-8);
  padding-bottom: var(--space-4);
  border-bottom: 2px solid var(--color-primary);
}

.section-number {
  font-size: var(--text-3xl);
  font-weight: 800;
  color: var(--color-primary);
  opacity: 0.3;
  font-family: var(--font-mono);
}

.section-title {
  font-size: var(--text-2xl);
  font-weight: 700;
  color: var(--color-text);
  margin: 0;
}
```

### 핵심 메시지 박스

```html
<div class="key-message">
  <div class="key-message-icon">💡</div>
  <div class="key-message-text">
    "함수 그래프를 평행이동시켜도, 넓이는 변하지 않아."
  </div>
</div>
```

```css
.key-message {
  display: flex;
  gap: var(--space-4);
  padding: var(--space-6);
  background: var(--color-accent-bg);
  border-radius: var(--radius-lg);
  border-left: 4px solid var(--color-accent);
  margin: var(--space-8) 0;
}

.key-message-icon {
  font-size: var(--text-2xl);
  flex-shrink: 0;
}

.key-message-text {
  font-family: var(--font-accent);
  font-size: var(--text-lg);
  line-height: var(--leading-relaxed);
  color: var(--color-text);
  font-weight: 500;
}
```

### 함정 경고 박스 (고3용)

```html
<div class="trap-box">
  <div class="trap-header">⚠️ 출제자가 노린 함정</div>
  <div class="trap-content">
    <!-- 내용 -->
  </div>
</div>
```

```css
.trap-box {
  background: var(--color-trap-bg);
  border: 1px solid var(--color-trap);
  border-radius: var(--radius-md);
  overflow: hidden;
  margin: var(--space-6) 0;
}

.trap-header {
  background: var(--color-trap);
  color: white;
  padding: var(--space-3) var(--space-6);
  font-weight: 700;
  font-size: var(--text-base);
}

.trap-content {
  padding: var(--space-6);
}
```

### 출제자 관점 블록 (고3 전용)

```html
<div class="examiner-block">
  <div class="examiner-badge">🎯 출제자 시선</div>
  <!-- 내용 -->
</div>
```

```css
.examiner-block {
  background: var(--color-examiner-bg);
  border: 1px solid var(--color-examiner);
  border-radius: var(--radius-lg);
  padding: var(--space-8);
  margin: var(--space-10) 0;
  position: relative;
}

.examiner-badge {
  position: absolute;
  top: calc(-1 * var(--space-3));
  left: var(--space-6);
  background: var(--color-examiner);
  color: white;
  padding: var(--space-1) var(--space-4);
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
  font-weight: 700;
}
```

### 패턴 발견 하이라이트

```html
<div class="pattern-discovery">
  <div class="pattern-label">🔍 패턴 발견!</div>
  <div class="pattern-content">
    <!-- 내용 -->
  </div>
</div>
```

```css
.pattern-discovery {
  background: linear-gradient(135deg, var(--color-accent-bg), #FFF8E1);
  border: 2px dashed var(--color-accent);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  margin: var(--space-6) 0;
}

.pattern-label {
  font-weight: 800;
  color: var(--color-accent-dark);
  font-size: var(--text-lg);
  margin-bottom: var(--space-3);
}
```

---

## 📝 수식 처리 규칙

### MathJax 문법 (그대로 사용)

| 유형 | 문법 | 용도 |
|:---|:---|:---|
| 인라인 | `$수식$` | 문장 안에 수식 삽입 |
| 블록 | `$$수식$$` | 독립된 수식 강조 |

### 수식 래핑

```html
<!-- 일반 블록 수식 -->
<div class="math-highlight reveal">
  $$S = \frac{1}{6} |a| (\beta - \alpha)^{3}$$
</div>

<!-- 핵심 공식 (히어로) -->
<div class="math-hero reveal">
  $$S = \frac{1}{6} |a| (\beta - \alpha)^{3}$$
</div>
```

### 수식 전개 (단계별)

```html
<div class="math-steps">
  <div class="math-step reveal">
    <span class="step-label">Step 1</span>
    $$수식1$$
  </div>
  <div class="math-step reveal reveal-delay-1">
    <span class="step-label">Step 2</span>
    $$수식2$$
  </div>
</div>
```

```css
.math-steps {
  margin: var(--space-8) 0;
}

.math-step {
  padding: var(--space-4) var(--space-6);
  margin: var(--space-2) 0;
  border-left: 3px solid var(--color-border);
  position: relative;
}

.math-step:hover {
  border-left-color: var(--color-primary);
  background: var(--color-bg-subtle);
}

.step-label {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--color-primary);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: var(--tracking-wide);
}
```

---

## 📊 이미지 처리

### 플레이스홀더 형식

마스터원고에 이미지가 있는 경우:

```html
<!-- [IMAGE: filename.png | alt텍스트 | 캡션] -->
<figure class="post-image reveal">
  <div class="image-placeholder">
    <!-- 사용자가 티스토리 에디터에서 이미지로 교체 -->
    <p>🖼️ 여기에 이미지 삽입: <strong>filename.png</strong></p>
  </div>
  <figcaption>캡션 텍스트</figcaption>
</figure>
```

```css
.post-image {
  margin: var(--space-8) 0;
  text-align: center;
}

.image-placeholder {
  background: var(--color-bg-subtle);
  border: 2px dashed var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-10);
  color: var(--color-text-muted);
}

.post-image figcaption {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-top: var(--space-3);
}
```

---

## 📏 글로벌 스타일

```css
/* ── 글로벌 리셋 & 기본 ── */
.post-container {
  max-width: var(--content-width);
  margin: 0 auto;
  padding: var(--space-8) var(--content-padding);
  font-family: var(--font-body);
  font-size: var(--text-lg);
  line-height: var(--leading-normal);
  color: var(--color-text);
  letter-spacing: var(--tracking-normal);
  word-break: keep-all;
  overflow-wrap: break-word;
}

.post-container * {
  box-sizing: border-box;
}

/* ── 문단 ── */
.post-container p {
  margin: 0 0 var(--paragraph-gap) 0;
}

/* ── 강조 ── */
.post-container strong {
  color: var(--color-primary-dark);
  font-weight: 700;
}

/* ── 구분선 ── */
.post-container hr {
  border: none;
  height: 1px;
  background: var(--color-border);
  margin: var(--section-gap) 0;
}

/* ── 리스트 ── */
.post-container ul, .post-container ol {
  padding-left: var(--space-6);
  margin: var(--space-4) 0;
}

.post-container li {
  margin-bottom: var(--space-2);
}
```

---

## ✅ 품질 체크리스트 (모든 결과물에 적용)

### 필수 확인
- [ ] `<div class="post-container">` 로 전체 래핑
- [ ] CSS 변수 선언 포함
- [ ] Intersection Observer 스크립트 포함
- [ ] 아코디언/탭 사용 시 관련 스크립트 포함
- [ ] MathJax 수식이 `$...$` 또는 `$$...$$` 형식
- [ ] 모든 주요 섹션에 `.reveal` 클래스 적용
- [ ] 이미지 위치에 플레이스홀더 삽입
- [ ] 한글 word-break: keep-all 적용
- [ ] 모바일 반응형 (max-width: 720px 기준)

### 고3용 추가 확인
- [ ] 출제자 관점 섹션 `.examiner-block` 사용
- [ ] 함정 박스 `.trap-box` 사용
- [ ] 아코디언 활용 (출제자 의도 펼치기)

---

## 🚫 금지 사항

1. **외부 라이브러리 임포트 금지** (MathJax, Pretendard 제외)
2. **React/Vue 등 프레임워크 코드 사용 금지**
3. **`<html>`, `<head>`, `<body>` 태그 사용 금지** (티스토리가 자동 추가)
4. **`<form>` 태그 사용 금지**
5. **`localStorage`, `sessionStorage` 사용 금지**
6. **내용 임의 변경 금지** — 마스터원고의 수학적 내용을 수정하지 말 것
7. **수식 문법 변경 금지** — LaTeX 코드 그대로 유지

---

## 📤 결과물 형식

output 폴더에 저장할 HTML 파일의 기본 구조:

```html
<style>
  /* CSS 변수 + 모든 스타일 */
</style>

<div class="post-container">
  <!-- 포스트 전체 내용 -->
</div>

<script>
  /* Intersection Observer + 아코디언/탭 스크립트 */
</script>
```

> 파일 하나에 스타일 + 콘텐츠 + 스크립트 모두 포함 (단일 파일)

---

## 📝 작업 완료 보고 형식

```
✅ 작업 완료

파일: output/post_고1.html (또는 post_고3.html)
섹션: N개
수식: N개 (인라인 N + 블록 N)
표: N개
애니메이션: 스크롤 등장 / 수식 강조 / 아코디언 / 탭
이미지 플레이스홀더: N개

⚠️ 사용자 할 일:
1. output/post_고1.html 내용을 복사
2. 티스토리 글쓰기 → HTML 모드에서 붙여넣기
3. 이미지 플레이스홀더를 실제 이미지로 교체
4. 미리보기 확인 → 발행
```

---

[CLAUDE.md — END]
