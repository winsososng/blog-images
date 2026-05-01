import os

css = """
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css');
@import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Nanum+Pen+Script&family=Hi+Melody&display=swap');

:root {
  --color-primary: #2563EB;
  --color-primary-light: #3B82F6;
  --color-primary-dark: #1D4ED8;
  --color-primary-bg: #EFF6FF;
  --color-accent: #F59E0B;
  --color-accent-light: #FCD34D;
  --color-accent-dark: #D97706;
  --color-accent-bg: #FFFBEB;
  --color-success: #10B981;
  --color-danger: #EF4444;
  --color-warning: #F97316;
  --color-info: #6366F1;
  --color-text: #1E293B;
  --color-text-secondary: #64748B;
  --color-text-muted: #94A3B8;
  --color-bg: #FFFFFF;
  --color-bg-subtle: #F8FAFC;
  --color-bg-card: #FFFFFF;
  --color-border: #E2E8F0;
  --color-border-strong: #CBD5E1;
  
  --font-heading: 'Pretendard', -apple-system, sans-serif;
  --font-body: 'Pretendard', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'D2Coding', monospace;
  --font-accent: 'RIDIBatang', 'Noto Serif KR', serif;
  
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  
  --leading-tight: 1.4;
  --leading-normal: 1.8;
  --leading-relaxed: 2.0;
  
  --tracking-tight: -0.02em;
  --tracking-normal: -0.01em;
  --tracking-wide: 0.02em;
  
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --section-gap: var(--space-16);
  --paragraph-gap: var(--space-6);
  --content-width: 720px;
  --content-padding: var(--space-6);
  
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
  --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
}

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
.post-container * { box-sizing: border-box; }
.post-container p { margin: 0 0 var(--paragraph-gap) 0; }
.post-container strong { color: var(--color-primary-dark); font-weight: 700; }
.post-container hr { border: none; height: 1px; background: var(--color-border); margin: var(--section-gap) 0; }
.post-container ul, .post-container ol { padding-left: var(--space-6); margin: var(--space-4) 0; }
.post-container li { margin-bottom: var(--space-2); }

.reveal {
  opacity: 0; transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.reveal.visible { opacity: 1; transform: translateY(0); }
.reveal-delay-1 { transition-delay: 0.1s; }

.section-header {
  display: flex; align-items: baseline; gap: var(--space-4);
  margin-bottom: var(--space-8); padding-bottom: var(--space-4);
  border-bottom: 2px solid var(--color-primary);
}
.section-number { font-size: var(--text-3xl); font-weight: 800; color: var(--color-primary); opacity: 0.3; font-family: var(--font-mono); }
.section-title { font-size: var(--text-2xl); font-weight: 700; color: var(--color-text); margin: 0; }

.key-message {
  display: flex; gap: var(--space-4); padding: var(--space-6);
  background: var(--color-accent-bg); border-radius: var(--radius-lg);
  border-left: 4px solid var(--color-accent); margin: var(--space-8) 0;
}
.key-message-icon { font-size: var(--text-2xl); flex-shrink: 0; }
.key-message-text { font-family: var(--font-accent); font-size: var(--text-lg); line-height: var(--leading-relaxed); color: var(--color-text); font-weight: 500; }

.math-highlight {
  display: block; padding: var(--space-6) var(--space-8); margin: var(--space-8) 0;
  background: var(--color-primary-bg); border-left: 4px solid var(--color-primary);
  border-radius: var(--radius-md); position: relative; overflow: hidden;
}
.math-highlight.visible { animation: mathGlow 1.5s ease-out; }
@keyframes mathGlow {
  0% { box-shadow: 0 0 0 rgba(37,99,235,0); }
  30% { box-shadow: 0 0 30px rgba(37,99,235,0.2); }
  100% { box-shadow: var(--shadow-sm); }
}

.math-steps { margin: var(--space-8) 0; }
.math-step { padding: var(--space-4) var(--space-6); margin: var(--space-2) 0; border-left: 3px solid var(--color-border); position: relative; }
.math-step:hover { border-left-color: var(--color-primary); background: var(--color-bg-subtle); }
.step-label { font-family: var(--font-mono); font-size: var(--text-xs); color: var(--color-primary); font-weight: 700; text-transform: uppercase; letter-spacing: var(--tracking-wide); }

.accordion { border: 1px solid var(--color-border); border-radius: var(--radius-md); overflow: hidden; margin: var(--space-6) 0; }
.accordion-header { display: flex; align-items: center; justify-content: space-between; padding: var(--space-4) var(--space-6); background: var(--color-bg-subtle); cursor: pointer; font-weight: 600; user-select: none; transition: background 0.2s ease; }
.accordion-header:hover { background: var(--color-border); }
.accordion-icon { transition: transform 0.3s ease; font-size: 1.2em; }
.accordion.open .accordion-icon { transform: rotate(180deg); }
.accordion-body { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out, padding 0.3s ease; padding: 0 var(--space-6); }
.accordion.open .accordion-body { max-height: 2000px; padding: var(--space-6); }

.chalkboard { background: linear-gradient(170deg, #2e4a3a 0%, #243832 40%, #1e3028 100%); border-radius: var(--radius-lg); padding: var(--space-8) var(--space-8) var(--space-12); position: relative; overflow: hidden; margin: var(--space-8) 0; }
.chalkboard::before { content: ''; position: absolute; inset: 0; background: url("data:image/svg+xml,%3Csvg width='200' height='200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.65' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E"); pointer-events: none; border-radius: var(--radius-lg); }
.chalk-tray { position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); display: flex; gap: 12px; opacity: 0.45; }
.chalk-tray-dot { width: 8px; height: 8px; border-radius: 50%; background: #EBE6DC; }
.chalk-tray-dot:nth-child(2) { background: #FCD34D; }
.chalk-tray-dot:nth-child(3) { background: #F87171; }
.chalk-tray-dot:nth-child(4) { background: #93C5FD; }

.chalk-w .ch { color: rgba(235, 230, 220, 0.88); text-shadow: 1px 1px 2px rgba(235,230,220,0.08), -0.5px 0 1px rgba(235,230,220,0.05); }
.chalk-y .ch { color: rgba(252, 211, 77, 0.9); text-shadow: 1px 1px 2px rgba(252,211,77,0.08); }
.chalk-r .ch { color: rgba(248, 113, 113, 0.88); text-shadow: 1px 1px 2px rgba(248,113,113,0.08); }
.chalk-b .ch { color: rgba(147, 197, 253, 0.88); text-shadow: 1px 1px 2px rgba(147,197,253,0.08); }

.chalk-row { font-size: 22px; line-height: 2.1; margin-bottom: 0.5rem; position: relative; white-space: pre-wrap; display: flex; flex-wrap: wrap; align-items: baseline; }
.ch { display: inline-block; opacity: 0; font-family: 'Nanum Pen Script', 'Hi Melody', 'Gaegu', cursive; }
.ch.on { opacity: 1; }
.chalk-dust { position: absolute; border-radius: 50%; pointer-events: none; animation: dustFall 1.2s ease-out forwards; }
@keyframes dustFall { 0% { opacity: 0.5; transform: translate(0, 0); } 100% { opacity: 0; transform: translate(var(--dx), var(--dy)); } }
.chalk-underline-draw { position: absolute; bottom: 2px; left: 0; height: 3px; border-radius: 2px; opacity: 0.5; width: 0; transition: width 0.6s ease-out; background: inherit; }
.chalk-underline-wrapper { position: relative; display: inline-block; }
.chalk-box { border: 2.5px dashed rgba(252, 211, 77, 0.3); border-radius: 10px; padding: 1rem 1.4rem; margin: 0.6rem 0 1rem; text-align: center; font-family: 'Nanum Pen Script', cursive; opacity: 0; transition: opacity 0.3s; }
.chalk-box.on { opacity: 1; }

.tabs { margin: var(--space-8) 0; }
.tab-buttons { display: flex; border-bottom: 2px solid var(--color-border); gap: 0; }
.tab-btn { padding: var(--space-3) var(--space-6); border: none; background: none; cursor: pointer; font-weight: 500; color: var(--color-text-secondary); border-bottom: 2px solid transparent; margin-bottom: -2px; transition: all 0.2s ease; font-size: var(--text-base); }
.tab-btn.active { color: var(--color-primary); border-bottom-color: var(--color-primary); font-weight: 700; }
.tab-btn:hover:not(.active) { color: var(--color-text); background: var(--color-bg-subtle); }
.tab-panel { display: none; padding: var(--space-6) 0; animation: fadeIn 0.3s ease; }
.tab-panel.active { display: block; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

.post-image { margin: var(--space-8) 0; text-align: center; }
.post-image img { max-width: 100%; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); }
"""

js = """
document.addEventListener('DOMContentLoaded', function() {
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(function(el) { observer.observe(el); });

  document.querySelectorAll('.accordion-header').forEach(function(header) {
    header.addEventListener('click', function() {
      this.parentElement.classList.toggle('open');
    });
  });

  document.querySelectorAll('.tab-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var tabGroup = this.closest('.tabs');
      tabGroup.querySelectorAll('.tab-btn').forEach(function(b) { b.classList.remove('active'); });
      tabGroup.querySelectorAll('.tab-panel').forEach(function(p) { p.classList.remove('active'); });
      this.classList.add('active');
      tabGroup.querySelector('#' + this.dataset.tab).classList.add('active');
    });
  });

  function makeCharSpans(container, text, size, bold) {
    var spans = [];
    for (var i = 0; i < text.length; i++) {
      var sp = document.createElement('span');
      sp.className = 'ch';
      sp.textContent = text[i];
      if (size) sp.style.fontSize = size + 'px';
      if (bold) sp.style.fontWeight = '700';
      var rot = (Math.random() - 0.5) * 2.5;
      var scl = 0.97 + Math.random() * 0.06;
      var ty = (Math.random() - 0.5) * 1.5;
      sp.style.transform = 'rotate(' + rot + 'deg) scale(' + scl + ') translateY(' + ty + 'px)';
      if (text[i] === ' ') sp.style.width = '0.3em';
      container.appendChild(sp);
      spans.push(sp);
    }
    return spans;
  }

  function spawnDust(board, charEl, color) {
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
      setTimeout(function(el) { return function() { if (el.parentNode) el.parentNode.removeChild(el); }; }(d), 1300);
    }
  }

  function animateChars(board, spans, speed, dustColor, onComplete) {
    var i = 0;
    var iv = setInterval(function() {
      if (i < spans.length) {
        spans[i].classList.add('on');
        if (i % 3 === 0 && spans[i].textContent !== ' ') spawnDust(board, spans[i], dustColor);
        i++;
      } else {
        clearInterval(iv);
        if(onComplete) onComplete();
      }
    }, speed);
  }

  function runChalkboard(board) {
    var scriptData = JSON.parse(board.dataset.script || '[]');
    var currentStep = 0;
    function nextStep() {
      if(currentStep >= scriptData.length) return;
      var step = scriptData[currentStep++];
      if(step.type === 'pause') {
        setTimeout(nextStep, step.ms || 300);
      } else if(step.type === 'line' || step.type === 'box') {
        var row = document.createElement('div');
        row.className = 'chalk-row ' + (step.color || 'chalk-w');
        if(step.type === 'box') row.className += ' chalk-box';
        var textInner = document.createElement('div');
        textInner.className = step.underline ? 'chalk-underline-wrapper' : '';
        row.appendChild(textInner);
        
        var dustColor = '#FFF';
        if(step.color === 'chalk-y') dustColor = '#FCD34D';
        if(step.color === 'chalk-b') dustColor = '#93C5FD';
        if(step.color === 'chalk-r') dustColor = '#F87171';
        
        var txt = step.main ? (step.main + '\\n' + step.sub) : step.text;
        var spans = makeCharSpans(textInner, txt, step.size, step.bold);
        board.appendChild(row);
        
        if(step.type === 'box') setTimeout(function(){ row.classList.add('on'); }, 100);

        animateChars(board, spans, 32, dustColor, function() {
          if(step.underline) {
            var ul = document.createElement('div');
            ul.className = 'chalk-underline-draw';
            ul.style.backgroundColor = dustColor;
            textInner.appendChild(ul);
            setTimeout(function(){ ul.style.width = '100%'; }, 50);
            setTimeout(nextStep, 600);
          } else {
            nextStep();
          }
        });
      }
    }
    nextStep();
    
    // Add tray
    var tray = document.createElement('div');
    tray.className = 'chalk-tray';
    for(var i=0; i<4; i++) {
       var d = document.createElement('div');
       d.className = 'chalk-tray-dot';
       tray.appendChild(d);
    }
    board.appendChild(tray);
  }

  var chalkObserver = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting && !entry.target.dataset.played) {
        entry.target.dataset.played = 'true';
        setTimeout(function() { runChalkboard(entry.target); }, 300);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('.chalkboard').forEach(function(el) {
    chalkObserver.observe(el);
  });
});
"""

def get_image(num):
    return f'<figure class="post-image reveal"><img src="https://raw.githubusercontent.com/winsososng/blog-images/main/images/0편/함수그래프변형_제0편_page{num:02d}.png" alt="page{num:02d}"></figure>'

html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>{css}</style>
</head>
<body>
<div class="post-container">

<section class="reveal">
  <div class="section-header">
    <span class="section-number">00</span>
    <h2 class="section-title">관계식의 눈으로 보라</h2>
  </div>
  {get_image(1)}
  <p>아빠가 오늘 좀 중요한 이야기를 하려고 해.</p>
  <p>너, 함수 그래프 변형 공부할 때 공식 몇 개나 외워야 하는지 알아? 평행이동, 대칭이동, 압축, 팽창, 축소, 확대... 하나하나 공식을 다 외우려고 하면 대충 10개는 넘어. 그런데 문제는 말이야, 오늘 외운 공식을 한 달 뒤 시험장에서 정확히 써먹을 수 있느냐는 거야.</p>
  <p>솔직히 말해볼까? 못 써.</p>
  <p>아니, 정확히 말하면 "약간 다르게" 기억해서 틀려. "x에 마이너스를 붙이는 건가, 플러스를 붙이는 건가?" "2를 곱하는 건가, 2분의 1을 곱하는 건가?" 이런 데서 실수가 나. 분명히 외웠는데, 시험장에서 손이 멈춰. 그리고 결국 감으로 찍어. 이게 현실이야.</p>
  <p>그래서 아빠는 이 시리즈에서 전혀 다른 접근법을 제안하려고 해.</p>
  <div class="key-message">
    <div class="key-message-icon">💡</div>
    <div class="key-message-text">"외우지 마. 유도해. 30초면 돼."</div>
  </div>
  <p>응? 30초 안에 유도한다고? 그게 가능하냐고? 가능해. 정말 간단한 아이디어 하나만 알면 돼. 그 아이디어를 지금부터 알려줄게.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">01</span>
    <h2 class="section-title">공식을 외우면 왜 틀리는가</h2>
  </div>
  {get_image(2)}
  <p>학교에서 이런 문장을 배운 적 있지?</p>
  <p><em>"y = f(x)의 그래프를 x축 방향으로 3만큼 평행이동하려면, x 대신 x빼기3을 대입하면 된다."</em></p>
  <p>처음 이 말을 들었을 때 어떤 생각이 들었어? 아마 이랬을 거야. "어... 플러스 3 이동인데 왜 마이너스 3을 대입하지?" 그러면서도 "선생님이 그렇다고 하니까 일단 외우자"라고 했겠지.</p>
  <div class="key-message">
    <div class="key-message-icon">⚠️</div>
    <div class="key-message-text">여기서 문제가 시작돼. 이해하지 못하고 외운 공식은 반드시 흔들려.</div>
  </div>
  <p>시험장에서 긴장하면 더 흔들려. 플러스인지 마이너스인지, 곱하는지 나누는지, 그 순간 머릿속이 하얘지는 경험, 해본 적 있지? 그건 네가 멍청해서가 아니야. 이해 없이 외운 공식의 당연한 결말이야.</p>
  <p>공식을 10개 외우면 10개가 다 흔들려. 근데 원리 하나를 이해하면? 시험장에서 30초 만에 직접 유도해낼 수 있어. 유도한 공식은 절대 안 흔들려. 네가 직접 만든 거니까.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">02</span>
    <h2 class="section-title">깨봉 박사님의 네트워크 — 여기서 시작이야</h2>
  </div>
  {get_image(3)}
  <p>아빠가 존경하는 깨봉 선생님의 유튜브 영상 하나를 봤어. 연립방정식을 설명하는 영상이었는데, 거기서 깨봉 선생님이 이런 말씀을 하셨어.</p>
  <p><em>"연립방정식을 네트워크로 생각하면 쉬워요."</em></p>
  <p>5개의 식, 5개의 변수. 보통은 대입법이니 가감법이니 해서 기계적으로 풀잖아. 그런데 깨봉 선생님은 완전히 다르게 접근하셨어. 각각의 식을 "변수들 사이의 관계"로 보고, 그 관계들을 네트워크처럼 연결해서 시각화하신 거야.</p>
  <p>a와 e의 관계, b와 e의 관계, c와 e의 관계... 이렇게 e를 중심으로 모든 변수가 네트워킹이 되어 있으니까, 테두리에 있는 a, b, c, d를 전부 e로 나타낼 수 있어. 마지막 관계식에 대입하면 e 하나로 된 식이 나오고. 끝.</p>
  <p>아빠가 이 영상을 보고 정말 감동받았어.</p>
  <div class="key-message">
    <div class="key-message-icon">🔍</div>
    <div class="key-message-text">방정식은 "답을 구하는 계산"이 아니라 "변수들 사이의 관계"다.</div>
  </div>
  <p>그리고 그 관계를 네트워크로 보면, 복잡한 것도 하나씩 연결해서 풀어낼 수 있다. 이 사고방식이 너무 좋아서, 아빠는 이걸 함수에도 적용해보기로 했어. 그리고 놀라운 걸 발견했어. 함수 그래프 변형 문제가 확 쉬워지더라고.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">03</span>
    <h2 class="section-title">함수식이라는 감옥</h2>
  </div>
  {get_image(4)}
  <p>우리가 수학 시간에 배우는 함수. y = f(x). 이걸 어떻게 배웠어?</p>
  <p>"x에 어떤 값을 넣으면 y가 나온다."</p>
  <p>맞지? x가 입력이고 y가 출력이야. 자판기처럼. 동전을 넣으면 음료수가 나오듯이, x를 넣으면 y가 나와. 이 사고방식, 나쁘지 않아. 함수의 기본 개념으로는 완벽해.</p>
  {get_image(5)}
  <p>근데 문제가 하나 있어.</p>
  <p>이 사고방식은 철저하게 <strong>x 중심</strong>이야. x가 주인공이고, y는 x에 종속된 부하 같은 존재야. x가 결정되면 y는 자동으로 따라오는 거니까.</p>
  <p>그런데 말이야, 요즘 수학 문제를 잘 들여다보면 재미있는 변화가 보여. 예전에는 "x=2일 때 y의 값을 구하시오" 같은 문제가 많았어. 전형적인 x 중심 문제지. 근데 요즘은? "y=0이 되는 x의 개수를 구하시오", "y가 0보다 큰 x의 범위를 구하시오" 이런 문제가 늘고 있어.</p>
  <p>심지어 킬러 문항에서는 y의 조건을 먼저 주고, 거기서 x를 역추적하라는 문제가 나와.</p>
  <p>무슨 말이냐면, 이제 <strong>y도 x만큼 중요한 주인공이 됐다</strong>는 거야. x에서 y로의 일방통행이 아니라, x와 y가 서로 대등하게 얽혀 있는 관계. 그 관계를 읽어내는 능력을 시험하겠다는 거지.</p>
  <p>그런데 우리는 여전히 "y = f(x)"라는 함수식에 갇혀서, x를 넣어서 y를 구한다는 생각만 하고 있어. 이게 감옥이야. 이 감옥에서 나와야 해.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">04</span>
    <h2 class="section-title">관계식이라는 자유 — x와 y를 평등하게</h2>
  </div>
  {get_image(6)}
  <p>감옥에서 나오는 방법은 간단해. <strong>"함수식"을 "관계식"으로 바꿔서 보는 거야.</strong></p>
  <p>\\(y = 2x + 3\\)이라는 함수식을 생각해봐. 이건 "x를 넣으면 y가 나온다"는 사고방식이야. 그런데 이걸 이렇게 써보면 어떨까?</p>
  
  <div class="math-highlight reveal">
    $$2x - y + 3 = 0$$
  </div>
  
  <p>뭐가 달라졌냐고? 글자만 바뀌었지 같은 거 아니냐고?</p>
  <p>아니, 달라. 놀라울 정도로 달라.</p>
  <p>첫 번째 형태 \\(y = 2x + 3\\)에서는 x가 원인이고 y가 결과야. x → y. 일방통행. 그런데 두 번째 형태 \\(2x - y + 3 = 0\\)에서는? x와 y가 <strong>평등해</strong>. 둘 다 이 관계식을 만족시키는 파트너야. 어느 쪽이 입력이고 어느 쪽이 출력이라는 위계가 없어.</p>
  <p>신기한 게 있어. 이렇게 표현을 바꾸는 것만으로도 우리 뇌의 사고방식이 바뀌어. \\(y = 2x + 3\\)을 보면 뇌가 자동으로 "x값을 대입해서 y값을 구해야지"라는 1차적 사고를 해. 그런데 \\(2x - y + 3 = 0\\)을 보면? "x와 y가 어떤 관계로 엮여 있구나"라는 2차적 사고로 업그레이드돼.</p>
  <p>이 2차적 사고가 바로 요즘 수능 문제에서 요구하는 트렌드야.</p>

  <div class="chalkboard reveal" data-script='[
    {{"type": "line", "color": "chalk-y", "text": "★ 핵심은 딱 하나야.", "size": 26, "bold": true}},
    {{"type": "pause", "ms": 300}},
    {{"type": "line", "color": "chalk-w", "text": "y = 2x + 3  ← 함수식. x가 주인.", "size": 21}},
    {{"type": "pause", "ms": 250}},
    {{"type": "line", "color": "chalk-b", "text": "2x - y + 3 = 0  ← 관계식. x와 y가 평등.", "size": 21}},
    {{"type": "pause", "ms": 350}},
    {{"type": "box", "color": "chalk-y", "main": "함수식 말고 관계식으로 봐.", "sub": "이 작은 시선의 전환이 모든 걸 바꾼다.", "underline": true}}
  ]'></div>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">05</span>
    <h2 class="section-title">방법론 하나로 공식 10개를 대체한다</h2>
  </div>
  {get_image(7)}
  <p>자, 이제 핵심이야. 관계식의 눈으로 그래프 변형을 바라보면, 모든 변형에 적용되는 <strong>하나의 방법론</strong>이 보여.</p>
  <p>그 방법론은 딱 4단계야.</p>
  {get_image(8)}
  
  <div class="math-steps">
    <div class="math-step reveal">
      <span class="step-label">Step 1</span>
      <div>주어진 함수를 관계식으로 본다. \\(f(x, y) = 0\\).</div>
    </div>
    <div class="math-step reveal reveal-delay-1">
      <span class="step-label">Step 2</span>
      <div>변형 조건에서, 원래 점 (x, y)와 새 점 (X, Y) 사이의 관계식을 뽑아낸다.</div>
    </div>
    <div class="math-step reveal reveal-delay-2">
      <span class="step-label">Step 3</span>
      <div>x = 뭔가, y = 뭔가 형태로 정리한다.</div>
    </div>
    <div class="math-step reveal reveal-delay-3">
      <span class="step-label">Step 4</span>
      <div>원래 관계식에 대입한다. 새 관계식 완성.</div>
    </div>
  </div>

  <p>끝이야. 이게 전부야.</p>
  <p>평행이동이든 대칭이동이든 압축이든 팽창이든 축소든 확대든, 이 4단계 구조는 <strong>절대 변하지 않아</strong>. 달라지는 건 딱 2단계뿐이야. 2단계의 관계식이 뭔지만 알면, 나머지는 기계적으로 따라가면 돼.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">06</span>
    <h2 class="section-title">직접 해보자 — 4단계 실전 적용</h2>
  </div>
  {get_image(9)}
  <p>말로만 하면 와닿지 않으니까, 직접 해보자.</p>
  <p><strong>문제</strong>: 관계식이 \\(x + y + 3 = 0\\)인 그래프를 x축으로 +3, y축으로 -2만큼 평행이동한 그래프의 관계식을 구하여라.</p>
  <p>자, 잠깐. 시작하기 전에 딱 한 가지만 정리하고 가자.</p>
  <p>우리가 구하려는 건 <strong>평행이동한 새 그래프</strong>야. 이 새 그래프 위의 임의의 점을 <strong>(X, Y)</strong> 라고 하자. 그러면 우리의 목적은 딱 하나야.</p>
  
  <div class="key-message">
    <div class="key-message-text">x, y에 관한 관계식을 이용해서, X, Y에 관한 관계식을 구하는 것.</div>
  </div>
  
  <p>원래 관계식은 x, y의 언어로 쓰여 있어. 우리는 그걸 X, Y의 언어로 번역하고 싶은 거야. 이 목적을 머릿속에 딱 박아두고, 이제 4단계를 차근차근 따라가 보자.</p>

  <div class="accordion">
    <div class="accordion-header">
      <span>1단계 — 원래 관계식 확인</span>
      <span class="accordion-icon">▼</span>
    </div>
    <div class="accordion-body">
      <p>원래 그래프의 관계식을 확인해.</p>
      <div class="math-highlight">$$x + y + 3 = 0$$</div>
      <p>이게 우리가 가진 출발점이야. 이 관계식을 만족하는 점 (x, y)가 원래 그래프 위에 있어.</p>
    </div>
  </div>

  {get_image(10)}

  <div class="accordion">
    <div class="accordion-header">
      <span>2단계 — 점의 이동 관계식 뽑기</span>
      <span class="accordion-icon">▼</span>
    </div>
    <div class="accordion-body">
      <p>이제 핵심이야. 원래 그래프 위의 점 (x, y)가 평행이동을 통해 새 그래프 위의 점 (X, Y)로 옮겨간다고 생각해봐.</p>
      <p>x축으로 +3만큼 이동했으니까, X좌표는 원래 x좌표보다 3이 커. 즉:</p>
      <div class="math-highlight">$$X = x + 3$$</div>
      <p>y축으로 -2만큼 이동했으니까, Y좌표는 원래 y좌표보다 2가 작아. 즉:</p>
      <div class="math-highlight">$$Y = y - 2$$</div>
      <p>이게 2단계야. "점이 어떻게 움직였는가"를 수식으로 표현한 것뿐이야. 어렵지 않지?</p>
    </div>
  </div>

  <div class="accordion">
    <div class="accordion-header">
      <span>3단계 & 4단계 — 정리 및 대입</span>
      <span class="accordion-icon">▼</span>
    </div>
    <div class="accordion-body">
      <p>2단계에서 얻은 두 식을, x와 y를 주인공으로 다시 정리해.</p>
      <div>$$X = x + 3 \quad \Rightarrow \quad x = X - 3$$</div>
      <div>$$Y = y - 2 \quad \Rightarrow \quad y = Y + 2$$</div>
      <p>이게 3단계야. 원래 좌표 x, y를 새 좌표 X, Y로 나타낸 거야. 이제 마지막으로 1단계 관계식에 이걸 대입해.</p>
      <div class="math-steps">
        <div class="math-step">
          $$x + y + 3 = 0$$
        </div>
        <div class="math-step">
          $$(X - 3) + (Y + 2) + 3 = 0$$
        </div>
      </div>
      <p>정리하면 <strong>\\(X + Y + 2 = 0\\)</strong></p>
      <p>끝! 새 관계식 완성.</p>
    </div>
  </div>

  {get_image(11)}
  <h3>잠깐, 이게 왜 되는 거야?</h3>
  <p>한 발짝 물러서서 생각해봐.</p>
  <p>원래 그래프 위의 점 (x, y)는 관계식 \\(x + y + 3 = 0\\)을 만족해. 이 점이 이동해서 새 그래프 위의 점 (X, Y)가 됐어. X, Y와 x, y 사이에는 \\(x = X - 3\\), \\(y = Y + 2\\)라는 관계가 성립하지? 그러면 원래 관계식에 이걸 대입하면, 새 그래프 위의 점 (X, Y)가 만족해야 하는 관계식이 나오는 거야. 논리가 딱 맞아떨어지지?</p>
  <p>뭘 외웠어? 아무것도 안 외웠어. "오른쪽으로 3 가면 X = x + 3"이라는 건 외우는 게 아니야. 당연한 사실이야. 나머지는 그냥 대입했을 뿐이야.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">07</span>
    <h2 class="section-title">왜 마이너스를 대입하는가 — 드디어 풀리는 의문</h2>
  </div>
  {get_image(12)}
  <p>여기서 아주 중요한 포인트가 하나 나와.</p>
  <p>수학 시간에 이런 말 들었지? "x축으로 +3만큼 평행이동하려면, x 자리에 x빼기3을 대입하면 된다." 처음 들었을 때 이상하지 않았어? 플러스 3 이동인데 왜 마이너스 3을 대입하는 거지?</p>
  <p>그 의문이 지금 완전히 풀려.</p>
  
  <div class="key-message">
    <div class="key-message-icon">💡</div>
    <div class="key-message-text">우리가 한 걸 봐. 오른쪽으로 3 이동하면 X = x + 3이야. 여기서 x를 정리하면 x = X - 3이잖아. 이걸 원래 관계식에 대입하니까, x 자리에 X - 3이 들어간 거야.</div>
  </div>

  <p>새 그래프의 좌표 X 기준으로 원래 좌표 x를 표현하면 X - 3이 되니까, 당연히 마이너스 3이 나오는 거야.</p>
  <p>당연한 거야. 전혀 이상할 게 없어.</p>
  <p>이걸 이해했다는 건, 이제 외울 필요가 없다는 거야. 시험장에서 30초 안에 직접 유도해낼 수 있어. 유도한 공식은 틀릴 수가 없어. 네가 그 자리에서 직접 만든 거니까.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">08</span>
    <h2 class="section-title">잠깐, 라이프니츠 이야기</h2>
  </div>
  {get_image(13)}
  <p>여기서 잠깐 옆길로 새볼게. 재미있는 이야기니까.</p>
  <p>미분을 처음 만든 사람이 두 명이야. 뉴턴과 라이프니츠. 뉴턴은 미분을 \\(f'(x)\\), 하나의 숫자로 봤어. 깔끔하지? 근데 라이프니츠는 달랐어. 미분을 \\(dy/dx\\)라고 썼어. y의 아주 작은 변화량을 x의 아주 작은 변화량으로 나눈 것. 분수처럼 보이지?</p>
  
  <div class="tabs">
    <div class="tab-buttons">
      <button class="tab-btn active" data-tab="tab-newton">뉴턴의 시선</button>
      <button class="tab-btn" data-tab="tab-leibniz">라이프니츠의 시선</button>
    </div>
    <div id="tab-newton" class="tab-panel active">
      <p><strong>함수식 사고</strong></p>
      <p>\\(f'(x)\\)는 "x를 넣으면 기울기가 나오는" 철저한 x중심 사고방식.</p>
    </div>
    <div id="tab-leibniz" class="tab-panel">
      <p><strong>관계식 사고</strong></p>
      <p>\\(dy/dx\\)는 x와 y 변화량의 파트너십. x도 변하고 y도 변하는 대등한 관계.</p>
    </div>
  </div>

  <p>이게 관계식 사고랑 정확히 같은 맥락이야. 시험장에서 뭐가 더 유용할까? 솔직히 말하면 라이프니츠 쪽이야. 특히 치환적분이나 매개변수 미분에서, dy/dx를 분수처럼 다루면 놀라울 정도로 간단해져.</p>
  <p>핵심은 이거야. <strong>x와 y를 평등하게 보는 관점이, 수학 여러 분야에서 강력하다.</strong> 그래프 변형에서도, 미분에서도.</p>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">09</span>
    <h2 class="section-title">앞으로 7편의 여정</h2>
  </div>
  {get_image(14)}
  <p>이 시리즈에서 우리가 갈 길을 미리 보여줄게. 매 편마다 같은 4단계 방법론을 사용할 거야. 달라지는 건 2단계뿐이야.</p>
  <ul>
    <li><strong>1편 — 평행이동:</strong> 2단계 관계식이 \\(X = x + a\\), \\(Y = y + b\\). 가장 기본이야.</li>
    <li><strong>2편 — 대칭이동:</strong> 2단계 관계식이 부호 바꾸기. \\(X = -x\\) 또는 교환.</li>
    <li><strong>3편 — 복합이동:</strong> 대칭이랑 평행이동을 합치면 순서가 중요한데, 4단계를 거치면 순서 문제가 해결돼.</li>
    <li><strong>4편 — 압축과 팽창:</strong> 최근 킬러 문항에서 자주 나와. 2단계 관계식이 \\(X = kx\\).</li>
    <li><strong>5편 — 임의의 기준점:</strong> 기준점이 원점이 아닐 때의 변형.</li>
    <li><strong>6편 — 모든 이차함수의 귀결:</strong> 모든 이차함수가 \\(y = x^2\\) 하나로 귀결된다는 걸 보여줄 거야.</li>
    <li><strong>7편 — 지수함수의 변환:</strong> 밑이 달라도 다 똑같은 함수의 압축팽창이라는 놀라운 사실.</li>
  </ul>
</section>

<section class="reveal">
  <div class="section-header">
    <span class="section-number">10</span>
    <h2 class="section-title">오늘의 핵심 — 딱 하나만 기억해</h2>
  </div>
  {get_image(15)}
  <p>오늘 이야기가 좀 길었지? 근데 핵심은 딱 하나야.</p>
  <p><strong>함수식 말고 관계식으로 봐.</strong></p>
  <p>x와 y를 주종관계로 보지 말고, 평등한 파트너로 봐. 그리고 그래프를 변형할 때는 4단계를 따라가면 돼. 공식 10개를 외울 필요가 없어. 방법론 1개만 이해하면 시험장에서 30초 안에 유도할 수 있어.</p>

  <div class="chalkboard reveal" data-script='[
    {{"type": "line", "color": "chalk-y", "text": "★ 오늘 핵심 — 딱 하나만 기억해.", "size": 26, "bold": true}},
    {{"type": "pause", "ms": 300}},
    {{"type": "line", "color": "chalk-w", "text": "외우지 마. 유도해. 30초면 돼.", "size": 22}},
    {{"type": "pause", "ms": 280}},
    {{"type": "line", "color": "chalk-b", "text": "1→관계식 확인  2→이동관계식  3→정리  4→대입", "size": 20, "underline": true}},
    {{"type": "pause", "ms": 300}},
    {{"type": "line", "color": "chalk-r", "text": "⚠ 공식 10개 외우면 시험장에서 반드시 흔들려.", "size": 20}},
    {{"type": "pause", "ms": 250}},
    {{"type": "line", "color": "chalk-y", "text": "★ 유도한 공식은 절대 안 흔들려.", "size": 23, "bold": true}},
    {{"type": "pause", "ms": 200}},
    {{"type": "line", "color": "chalk-y", "text": "    네가 직접 만든 거니까.", "size": 22}}
  ]'></div>

  <p>어렵다고? 아니야. 정말 간단한 아이디어야. 다음 편부터 하나씩 보여줄게. 나만 믿고 따라와.</p>
  <hr>
  <p><em>다음 편 예고: 1편 — 평행이동. "x 대신 x빼기3을 넣어라"를 외우지 말고, 왜 x빼기3인지를 30초 만에 유도하는 법.</em></p>
</section>

</div>
<script>{js}</script>
</body>
</html>
"""

with open("output/post_0편.html", "w", encoding="utf-8") as f:
    f.write(html)

print("success")
