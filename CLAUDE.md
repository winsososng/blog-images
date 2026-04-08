# CLAUDE.md — 변호사아빠의 수학특강 티스토리 빌드 시스템

> Anti(Claude Code)가 티스토리 블로그 HTML을 빌드할 때 **항상** 이 파일을 먼저 읽고 따를 것.

---

## 📌 프로젝트 정보

| 항목 | 내용 |
|:---|:---|
| 블로그 | fafamath.tistory.com |
| 블로그명 | 변호사아빠의 수학특강 |
| 이미지 repo | winsososng/blog-images (public) |
| 이미지 URL | `https://raw.githubusercontent.com/winsososng/blog-images/main/images/N편/파일명.png` |

---

## 🚫 절대 규칙

1. **Python 빌드 스크립트 사용 금지** — HTML 파일을 직접 작성할 것
2. **`<!DOCTYPE>`, `<html>`, `<head>`, `<body>` 태그 사용 금지** — 티스토리가 자동 추가
3. **파일 구조**: `<style>CSS</style>` → `<div class="pc">본문</div>` → `<script>JS</script>`
4. **외부 라이브러리 금지** (아래 허용 목록 제외)
5. **이미지는 반드시 GitHub raw URL 사용**
6. **마스터원고의 수학적 내용 임의 변경 금지**

### 허용 외부 리소스

```html
<!-- MathJax 3.x -->
<script>
MathJax = {
  tex: { inlineMath: [['$','$'], ['\\(','\\)']], displayMath: [['$$','$$'], ['\\[','\\]']] },
  options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>

<!-- 폰트 -->
<link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Hi+Melody&family=Gaegu&display=swap" rel="stylesheet">
```

---

## 🎨 디자인 토큰

### 색상

| 이름 | CSS변수 | Hex | 용도 |
|:---|:---|:---|:---|
| 메인 블루 | `--c-main` | `#2563EB` | 함수 곡선, 핵심 공식, 증가 구간, 링크 |
| 앰버 | `--c-accent` | `#F59E0B` | 강조, 접선, 넓이 영역 |
| 보라 | `--c-examiner` | `#7C3AED` | 출제자 관점 (고3), f'(x), 교점 |
| 빨강 | `--c-danger` | `#DC2626` | 주의, 극값, 감소 구간, 함정 |
| 초록 | `--c-ok` | `#16A34A` | 정답, x절편, 올바른 풀이 |
| 회색 | `--c-gray` | `#6B7280` | Step 번호, 보조선 |
| 배경 | `--c-bg` | `#FAFAFA` | 전체 배경 |
| 카드 배경 | `--c-card` | `#FFFFFF` | 카드 배경 |
| 텍스트 | `--c-text` | `#1F2937` | 본문 텍스트 |

### 타이포그래피

| 항목 | 값 |
|:---|:---|
| 본문 폰트 | `'Pretendard Variable', Pretendard, -apple-system, sans-serif` |
| 본문 크기 | `1.125rem` (18px) |
| 행간 | `1.8` |
| h2 크기 | `1.625rem` (26px) |
| h3 크기 | `1.375rem` (22px) |
| 최대 너비 | `720px` |

### 기본 CSS 변수 선언

```css
:root {
  --c-main: #2563EB;
  --c-accent: #F59E0B;
  --c-examiner: #7C3AED;
  --c-danger: #DC2626;
  --c-ok: #16A34A;
  --c-gray: #6B7280;
  --c-bg: #FAFAFA;
  --c-card: #FFFFFF;
  --c-text: #1F2937;
  --max-w: 720px;
  --radius: 12px;
}
```

---

## 🧩 컴포넌트 시스템

### 1. `reveal` — 스크롤 등장 애니메이션

```html
<div class="reveal">
  <!-- 내용 -->
</div>
```

```css
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```javascript
// Intersection Observer로 트리거
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

### 2. `math-hero` — 핵심 공식 히어로 블록

```html
<div class="math-hero">
  <div class="math-hero-label">핵심 공식</div>
  <div class="math-hero-formula">
    $$f(x) = h(x-a)(x-b)(x-c) + g(x)$$
  </div>
</div>
```

```css
.math-hero {
  background: linear-gradient(135deg, #EFF6FF, #F0F9FF);
  border: 2px solid var(--c-main);
  border-radius: var(--radius);
  padding: 2rem 1.5rem;
  text-align: center;
  margin: 2rem 0;
  position: relative;
}
.math-hero-label {
  position: absolute;
  top: -14px;
  left: 24px;
  background: var(--c-main);
  color: white;
  padding: 4px 16px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
}
.math-hero-formula {
  font-size: 1.3rem;
  padding-top: 0.5rem;
}
```

### 3. `math-steps` — 수식 단계별 전개

```html
<div class="math-steps">
  <div class="math-step reveal">
    <span class="step-num">Step 1</span>
    <div class="step-content">$$수식$$</div>
    <p class="step-desc">설명</p>
  </div>
  <!-- 반복 -->
</div>
```

```css
.math-step {
  padding: 1rem 1.5rem;
  border-left: 3px solid var(--c-main);
  margin-bottom: 1rem;
  background: #F8FAFC;
  border-radius: 0 var(--radius) var(--radius) 0;
}
.step-num {
  display: inline-block;
  background: var(--c-gray);
  color: white;
  padding: 2px 12px;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}
.step-desc {
  color: var(--c-gray);
  font-size: 0.95rem;
  margin-top: 0.5rem;
}
```

### 4. `key-message` — 핵심 메시지 박스

```html
<div class="key-message">
  <span class="key-icon">💡</span>
  <p>핵심 메시지 텍스트</p>
</div>
```

```css
.key-message {
  background: #FEF3C7;
  border-left: 4px solid var(--c-accent);
  border-radius: 0 var(--radius) var(--radius) 0;
  padding: 1.2rem 1.5rem;
  margin: 1.5rem 0;
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.key-icon { font-size: 1.5rem; flex-shrink: 0; }
.key-message p { margin: 0; font-weight: 500; }
```

### 5. `table-interactive` — 인터랙티브 표

```html
<table class="table-interactive">
  <thead><tr><th>항목</th><th>값</th></tr></thead>
  <tbody>
    <tr><td>데이터</td><td>값</td></tr>
  </tbody>
</table>
```

```css
.table-interactive {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.table-interactive th {
  background: var(--c-main);
  color: white;
  padding: 12px 16px;
  font-weight: 600;
  text-align: left;
}
.table-interactive td {
  padding: 12px 16px;
  border-bottom: 1px solid #E5E7EB;
}
.table-interactive tbody tr:hover {
  background: #EFF6FF;
  transition: background 0.2s ease;
}
```

### 6. `trap-box` — 함정 경고 (고3용)

```html
<div class="trap-box">
  <div class="trap-label">⚠️ 출제자가 노린 함정</div>
  <p>함정 설명</p>
  <div class="trap-avoid">✅ 회피법: 회피법 설명</div>
</div>
```

```css
.trap-box {
  background: #FEF2F2;
  border: 2px solid var(--c-danger);
  border-radius: var(--radius);
  padding: 1.5rem;
  margin: 1.5rem 0;
}
.trap-label {
  font-weight: 700;
  color: var(--c-danger);
  margin-bottom: 0.5rem;
  font-size: 1.05rem;
}
.trap-avoid {
  background: #F0FDF4;
  border-left: 3px solid var(--c-ok);
  padding: 0.75rem 1rem;
  margin-top: 0.75rem;
  border-radius: 0 8px 8px 0;
  font-weight: 500;
}
```

### 7. `examiner-block` — 출제자 관점 (고3용)

```html
<div class="examiner-block">
  <div class="examiner-header">🎯 출제자의 의도</div>
  <div class="examiner-content">
    <!-- 4대 질문 등 -->
  </div>
</div>
```

```css
.examiner-block {
  background: linear-gradient(135deg, #F5F3FF, #EDE9FE);
  border: 2px solid var(--c-examiner);
  border-radius: var(--radius);
  padding: 0;
  margin: 2rem 0;
  overflow: hidden;
}
.examiner-header {
  background: var(--c-examiner);
  color: white;
  padding: 12px 20px;
  font-weight: 700;
  font-size: 1.15rem;
}
.examiner-content {
  padding: 1.5rem;
}
.examiner-content h4 {
  color: var(--c-examiner);
  margin-top: 1rem;
}
```

### 8. `accordion` — 펼치기/접기

```html
<div class="accordion">
  <div class="accordion-header" onclick="this.parentElement.classList.toggle('open')">
    <span>제목</span><span class="accordion-arrow">▸</span>
  </div>
  <div class="accordion-body">
    <p>내용</p>
  </div>
</div>
```

```css
.accordion {
  border: 1px solid #E5E7EB;
  border-radius: var(--radius);
  margin: 1rem 0;
  overflow: hidden;
}
.accordion-header {
  padding: 14px 20px;
  background: #F9FAFB;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 600;
}
.accordion-arrow { transition: transform 0.3s; }
.accordion.open .accordion-arrow { transform: rotate(90deg); }
.accordion-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
  padding: 0 20px;
}
.accordion.open .accordion-body {
  max-height: 1000px;
  padding: 14px 20px;
}
```

### 9. `tabs` — 탭 전환

```html
<div class="tabs">
  <div class="tab-buttons">
    <button class="tab-btn active" onclick="switchTab(this, 'tab1')">탭1</button>
    <button class="tab-btn" onclick="switchTab(this, 'tab2')">탭2</button>
  </div>
  <div class="tab-content active" id="tab1">탭1 내용</div>
  <div class="tab-content" id="tab2">탭2 내용</div>
</div>
```

```javascript
function switchTab(btn, tabId) {
  const tabs = btn.closest('.tabs');
  tabs.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  tabs.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  tabs.querySelector('#' + tabId).classList.add('active');
}
```

---

## 🎓 칠판 판서 시스템 ⭐

### 사용 원칙

- 포스트당 **1~3개** (과용 금지)
- work_order의 판서 지시에 따라 구현
- 스크롤 진입 시 자동 시작 (Intersection Observer)

### 4색 분필

| 색상 | CSS | 용도 |
|:---|:---|:---|
| 흰색 | `rgba(255,255,255,0.95)` | 기본 텍스트 |
| 노란색 | `#FFD700` | 강조 |
| 빨간색 | `#FF6B6B` | 주의 |
| 파란색 | `#6CB4EE` | 공식 |

### HTML 구조

```html
<div class="chalkboard reveal" data-chalk='[
  {"text": "핵심 공식", "color": "blue", "effect": "none"},
  {"text": "f(x) = h(x-a)(x-b)(x-c) + g(x)", "color": "yellow", "effect": "underline"},
  {"text": "↑ 거리곱 + 보정", "color": "white", "effect": "star"}
]'>
  <div class="chalk-surface"></div>
</div>
```

### CSS

```css
.chalkboard {
  background: #2D5016;
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 30px 30px;
  border: 12px solid #8B6914;
  border-radius: 4px;
  box-shadow: inset 0 0 40px rgba(0,0,0,0.3), 0 4px 12px rgba(0,0,0,0.2);
  padding: 2.5rem 2rem;
  margin: 2rem 0;
  min-height: 160px;
  position: relative;
  overflow: hidden;
}
.chalk-surface {
  font-family: 'Nanum Pen Script', 'Hi Melody', 'Gaegu', cursive;
  font-size: 1.6rem;
  line-height: 2.2;
}
.chalk-char {
  display: inline-block;
  opacity: 0;
  text-shadow: 0 0 4px rgba(255,255,255,0.3);
}
.chalk-char.show { opacity: 1; }
.chalk-dust {
  position: absolute;
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: rgba(255,255,255,0.6);
  pointer-events: none;
  animation: dustFall 1.5s ease-out forwards;
}
@keyframes dustFall {
  0% { opacity: 1; transform: translate(0, 0); }
  100% { opacity: 0; transform: translate(var(--dx), var(--dy)); }
}
```

### JavaScript (자연스러운 필기 효과)

```javascript
function animateChalkboard(el) {
  const data = JSON.parse(el.dataset.chalk);
  const surface = el.querySelector('.chalk-surface');
  const colors = { white: 'rgba(255,255,255,0.95)', yellow: '#FFD700', red: '#FF6B6B', blue: '#6CB4EE' };
  let totalDelay = 0;

  data.forEach((line, lineIdx) => {
    const lineDiv = document.createElement('div');
    lineDiv.style.marginBottom = '0.5rem';
    const chars = line.text.split('');
    
    chars.forEach((char, i) => {
      const span = document.createElement('span');
      span.className = 'chalk-char';
      span.textContent = char;
      span.style.color = colors[line.color] || colors.white;
      // 자연스러움: 미세 회전, 크기 변동, 수직 흔들림
      const rot = (Math.random() - 0.5) * 5; // ±2.5°
      const scale = 0.97 + Math.random() * 0.06; // 97~103%
      const dy = (Math.random() - 0.5) * 3; // ±1.5px
      span.style.transform = `rotate(${rot}deg) scale(${scale}) translateY(${dy}px)`;
      
      setTimeout(() => {
        span.classList.add('show');
        // 분필 가루: 3글자마다 2개 파티클
        if (i % 3 === 0) {
          for (let p = 0; p < 2; p++) {
            const dust = document.createElement('div');
            dust.className = 'chalk-dust';
            dust.style.left = span.offsetLeft + 'px';
            dust.style.top = span.offsetTop + 'px';
            dust.style.setProperty('--dx', (Math.random()-0.5)*20 + 'px');
            dust.style.setProperty('--dy', Math.random()*15 + 5 + 'px');
            el.appendChild(dust);
            setTimeout(() => dust.remove(), 1500);
          }
        }
      }, totalDelay + i * 32); // 32ms/글자
    });
    
    // 밑줄 효과
    if (line.effect === 'underline') {
      setTimeout(() => {
        lineDiv.style.borderBottom = `2px solid ${colors[line.color]}`;
        lineDiv.style.paddingBottom = '4px';
      }, totalDelay + chars.length * 32 + 200);
    }
    // 별표 팝 효과
    if (line.effect === 'star') {
      setTimeout(() => {
        const star = document.createElement('span');
        star.textContent = ' ⭐';
        star.style.fontSize = '1.4rem';
        star.style.animation = 'starPop 0.4s ease';
        lineDiv.appendChild(star);
      }, totalDelay + chars.length * 32 + 200);
    }
    
    totalDelay += chars.length * 32 + 300;
    surface.appendChild(lineDiv);
  });
}

// 스크롤 진입 시 자동 시작
const chalkObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !entry.target.dataset.animated) {
      entry.target.dataset.animated = 'true';
      entry.target.classList.add('visible');
      animateChalkboard(entry.target);
    }
  });
}, { threshold: 0.3 });
document.querySelectorAll('.chalkboard').forEach(el => chalkObserver.observe(el));
```

---

## 📐 HTML 파일 구조 (최종 output)

```
<style>
  /* CSS 변수 + 전체 스타일 + 컴포넌트 스타일 */
</style>

<div class="pc">
  <!-- MathJax 로드 -->
  <script>MathJax = {...};</script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
  <link href="Pretendard CDN" rel="stylesheet">
  <link href="Google Fonts (필기체)" rel="stylesheet">
  
  <!-- 본문 시작 -->
  <div class="post-wrapper">
    <h2>섹션 제목</h2>
    <div class="reveal">
      <p>본문 텍스트...</p>
    </div>
    <!-- 컴포넌트들 -->
  </div>
</div>

<script>
  /* Intersection Observer + 칠판 판서 JS + 탭/아코디언 JS */
</script>
```

---

## 📋 빌드 프로세스

1. `input/work_order_N편.md` 읽기
2. `input/master_N편.md` 읽기
3. `input/` 내 이미지 파일 → `images/N편/` 으로 복사 → `git add + commit + push`
4. GitHub raw URL 확보
5. 마스터원고 내용 + work_order 지시 → 이 CLAUDE.md 디자인 시스템 적용 → HTML 직접 작성
6. `output/post_N편.html` 저장
7. 완료 보고

---

## ⚠️ 체크리스트 (빌드 완료 전 확인)

- [ ] `<!DOCTYPE>`, `<html>`, `<head>`, `<body>` 태그 없음
- [ ] 이미지 src가 전부 GitHub raw URL
- [ ] MathJax 로드 코드 포함
- [ ] 수식이 `$...$` 또는 `$$...$$` 형식
- [ ] 칠판 판서 블록이 work_order 지시대로 배치
- [ ] reveal 클래스가 주요 섹션에 적용
- [ ] 마스터원고의 수학 내용이 변경되지 않음
- [ ] Python 빌드 스크립트가 아닌 HTML 직접 작성

---

[END OF CLAUDE.md]
