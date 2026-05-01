# 🌐 멀티PC 블로그 시스템 운영 가이드 v1.0

## 📌 버전 정보

| 항목 | 내용 |
|:---|:---|
| 버전 | v1.0 |
| 정립일 | 2026-05-01 |
| 적용 범위 | 변호사아빠의 수학특강 블로그 시스템 전체 |
| 다음 검토 | 1개월 후 (사용자 직접 운영 전환 검토) |

---

## 🎯 핵심 운영 원칙

### 원칙 1: Git이 모든 동기화의 허브

> **모든 PC가 GitHub 저장소를 통해 동일한 작업 환경을 공유한다.**

- 작업 자료(input/, output/, archive/, images/)는 모두 Git에 들어감
- 어느 PC에서든 `git clone` 한 번이면 똑같은 환경
- 작업 시작 전 `git pull`, 작업 후 `git push`가 표준 패턴

### 원칙 2: 보안 정보는 별도 채널

> **비밀번호/토큰은 Git에 절대 들어가지 않는다.**

- 네이버 로그인 정보 → `.env` 파일에 분리 (코드에서 `os.getenv()`로 읽음)
- `.env` 파일은 `.gitignore`로 추적 차단
- `.env` 백업본 → Google Drive **비공개 문서**에 보관

### 원칙 3: 동영상은 별도 보관

> **동영상은 GitHub이 아닌 로컬/Google Drive/YouTube에 보관한다.**

- 이유: GitHub 1GB 권장 한도, 동영상은 50~100MB/편
- Manim `.py` 스크립트는 Git에 (재현 가능성)
- 완성된 `.mp4`, `.mov` 등은 별도 채널

### 원칙 4: 관리자(클로드)와 작업자(Anti)의 분리

> **명령어는 클로드가 만들고, 실행은 Anti가 한다.**

- 사용자(Song님)는 클로드에게 "작업 시작하자" / "작업 끝났어" 정도만 전달
- 클로드는 매번 상황에 맞는 Anti 명령어를 생성
- Anti는 명령을 그대로 실행
- (한 달 후 사용자가 직접 실행하는 단계로 전환 검토)

---

## 📂 시스템 폴더 구조

### Git 추적되는 것 (모든 PC가 공유)

```
C:\Claude_Code\blog\
├── CLAUDE.md                    ← Anti 빌더 룰
├── README.md                    ← 프로젝트 안내
├── work_order_template.md       ← 작업지시서 템플릿
├── setup.sh                     ← 신규 PC 세팅 스크립트
├── .gitignore                   ← Git 정책
│
├── build_html.py                ← 티스토리 빌드용
├── selectors.json               ← 네이버 셀렉터
├── v_103_naver_publish_*.py     ← Selenium 발행 코드
│
├── input/                       ← 작업 재료 (마스터원고, JSON 등)
├── output/                      ← 빌드 결과 HTML
├── images/                      ← 티스토리 이미지 호스팅 + 백업
│   ├── 0편/
│   ├── 차함수002/
│   └── ...
└── archive/                     ← 발행 완료 백업 (200편 비전 재료)
    ├── 차함수002/
    └── ...
```

### Git 추적 안 되는 것 (각 PC 로컬 또는 별도 보관)

| 항목 | 위치 | 동기화 채널 |
|:---|:---|:---|
| `.env` | 로컬 루트 | Google Drive 비공개 문서 |
| `*.bak`, `*.tmp` | 로컬 | 동기화 불필요 |
| `_local_backup/`, `_remote_preview/` | 로컬 | Git 작업 임시폴더 |
| `NaverBlogProfile/` | 로컬 | 각 PC에서 첫 로그인 시 자동 생성 |
| `__pycache__/`, `*.pyc` | 로컬 | Python 자동 생성 |
| `*.mp4`, `media/`, `manim_env/` | 로컬 | YouTube + Google Drive |
| `.vscode/`, `.idea/` | 로컬 | 에디터 개인 설정 |

---

## 🔄 표준 워크플로우

### 패턴 A: 작업 시작 (어느 PC에서든)

**Song님이 클로드에게**: "작업 시작하자" 또는 "[N편] 작업 시작"

**클로드가 Anti에게 줄 명령**:

```
[관리자 지시 / Anti의 Gemini에게]
작업 시작 전 동기화 절차야.

1. cd C:\Claude_Code\blog (현재 위치 확인)
2. git status → 깨끗한 상태인지 확인
   - 만약 변경사항이 남아 있으면 즉시 멈추고 보고. 자동 처리하지 마.
3. git pull origin main → 다른 PC에서 한 작업 받아오기
4. 결과 보고:
   [A] 받아온 커밋 수
   [B] 변경된 파일 목록 (있으면)
   [C] 현재 git status: clean 인지
   [D] 작업 시작 가능 여부: ✅ / ❌
```

### 패턴 B: 작업 종료 / 중간 저장

**Song님이 클로드에게**: "작업 끝났어, 저장해줘" 또는 "[N편] 발행 완료"

**클로드가 Anti에게 줄 명령**:

```
[관리자 지시 / Anti의 Gemini에게]
작업 마무리 동기화야.

⚠️ 절대 금지:
- git push --force
- .env, *.bak 등 ignored 파일을 무리하게 add

1. git status → 변경사항 확인 (먼저 사용자에게 보여주기)
2. git add . 
3. git status 재확인:
   ✅ 들어가야 할 것: input/, output/, images/, archive/, 수정된 코드/문서
   ❌ 절대 없어야 할 것: .env, *.bak, _local_backup/, _remote_preview/
   - 만약 ❌ 항목이 staging에 보이면 즉시 멈추고 보고
4. git commit -m "[메시지 — 사용자가 알려준 내용]"
5. git push origin main
6. 결과 보고:
   [A] 추가된 파일 수
   [B] 커밋 해시
   [C] push 성공 여부
   [D] 최종 git status: clean 인지
```

### 패턴 C: 새 PC 추가 시

**Song님이 클로드에게**: "새 PC에 환경 세팅해줘"

**클로드가 Anti에게 줄 명령** (3단계 + 보안 1단계):

```
[관리자 지시 / Anti의 Gemini에게]
새 PC 환경 구성이야.

1. C:\Claude_Code\ 폴더로 이동 (없으면 생성)
2. git clone https://github.com/winsososng/blog-images.git C:\Claude_Code\blog
3. cd C:\Claude_Code\blog
4. pip install python-dotenv (Selenium 발행용)
5. bash setup.sh (작업 폴더 자동 생성)
6. 폴더 구조 확인 후 보고

⚠️ .env 파일은 사용자가 Google Drive 비공개 문서에서 직접 복사해 와야 함. 
   Anti가 만들지 마. 사용자에게 Google Drive 백업본을 가져오라고 안내해.
```

그 후 **Song님이 직접**: Google Drive 비공개 문서에서 `.env` 내용 복사 → `C:\Claude_Code\blog\.env`로 저장

---

## 🔐 보안 운영

### .env 파일 구조

```
NAVER_ID=실제ID
NAVER_PW=실제비번
```

### .env 백업 위치

- **Google Drive 비공개 문서**: "🔒 블로그 시스템 비밀 (Naver Login)"
- 일반 액세스: **"제한됨"** (본인만)
- 새 PC 추가 시 이 문서에서 복사

### .env 변경 시 (비번 변경 등)

```
[관리자 지시 / Anti의 Gemini에게]
.env 변경 후 동기화 점검만 해줘. push 절대 금지.

1. git check-ignore -v .env → ignored 확인
2. git ls-files | Select-String "\.env" → 출력 비어있어야 함
3. 보고만.
```

그 후 **Song님이 직접** Google Drive 문서도 같이 업데이트.

---

## 🎬 미래 확장: Manim 동영상 시스템

### 동영상 파이프라인 흐름

```
input/마스터원고.md
       ↓
[Manim 스크립트 작성 — Anti 또는 사용자]
       ↓
archive/[N편]/scene.py  ← 스크립트는 Git에
       ↓
[manim 렌더링]
       ↓
[N편].mp4 (로컬, ~50-100MB)
       ↓
   ┌───┴───┐
   ↓       ↓
YouTube  Google Drive
(공개)    (백업)
       ↓
[Git에는 안 올림 — .gitignore에서 *.mp4 차단됨]
```

### Manim 환경 처음 구축 시

```
[관리자 지시 / Anti의 Gemini에게]

1. cd C:\Claude_Code\blog
2. python -m venv manim_env
3. manim_env\Scripts\activate
4. pip install manim
5. (FFmpeg, MiKTeX 별도 설치 필요 — 사용자 확인)
6. 테스트 hello.py 만들고 manim -pql hello.py 실행
7. 결과 보고
```

`manim_env/`, `media/`는 이미 `.gitignore`로 차단되어 있음.

---

## 🚨 트러블슈팅

### 문제 1: `git pull` 실패 — 충돌 발생

**증상**: "Your local changes would be overwritten by merge"

**클로드가 Anti에게 줄 명령**:
```
1. git status로 충돌 파일 정확히 확인
2. 그 파일들을 _local_backup/에 복사 (안전 백업)
3. 어떤 파일인지 보고만 하고 멈춰. 사용자 결정 대기.
```

### 문제 2: `git push` 거부 — non-fast-forward

**증상**: "Updates were rejected because the remote contains work..."

**원인**: 다른 PC에서 push한 게 있는데 이 PC가 못 받음.

**클로드가 Anti에게 줄 명령**:
```
1. git fetch origin
2. git status → 차이 확인
3. git pull origin main (자동 merge 시도)
   - 충돌 시 즉시 멈추고 보고
4. 성공 시 다시 git push origin main
```

⚠️ `git push --force`는 **절대 금지**. 이미지가 사라질 수 있음.

### 문제 3: `.env`가 실수로 staging에 들어감

**즉시 조치**:
```
git reset HEAD .env
git check-ignore -v .env  ← ignored 확인
```

만약 이미 commit/push 됐다면: 비번을 즉시 변경하고 별도 정리 작업 필요.

### 문제 4: 이미지가 티스토리에서 깨짐

**원인**: GitHub에서 이미지가 사라짐 또는 repo 이름 변경됨.

**확인**:
- `https://raw.githubusercontent.com/winsososng/blog-images/main/images/[편명]/[파일명]` URL을 브라우저에서 직접 열어보기
- 404면 GitHub repo에서 해당 이미지 복원 필요

⚠️ `winsososng/blog-images` repo 이름은 **절대 변경 금지** (모든 발행 포스트의 이미지 URL이 이 이름을 가리킴).

---

## 📋 매 작업마다 클로드의 역할

### 작업 시작 시
1. Song님: "작업 시작" / "[주제] 새 포스트 시작" 등
2. 클로드: 위 [패턴 A: 작업 시작] 명령어 생성
3. Song님이 Anti에게 복붙 → 결과 받아오기
4. 클로드: 결과 검증 후 다음 단계로

### 작업 중간
1. Phase 1~7 진행 (기존 가이드 v.140 참조)
2. 각 Phase마다 클로드가 산출물 생성
3. Song님이 다운로드 → blog/ 폴더에 넣기

### 작업 종료 시
1. Song님: "작업 끝, 저장해줘"
2. 클로드: 위 [패턴 B: 작업 종료] 명령어 생성
   - 커밋 메시지는 사용자에게 확인 후 결정
3. Song님이 Anti에게 복붙 → push 완료

---

## 🗓️ 자가 운영 전환 로드맵

### 현재 (Day 1~30)
- 모든 명령어를 클로드가 만듦
- Song님은 복붙만

### 1개월 후 (Day 31~)
- 자주 쓰는 명령(`git pull`, `git add . / commit / push`)은 Song님이 직접
- 복잡한 상황(충돌, 보안 점검)은 여전히 클로드에게 의뢰

### 3개월 후
- 표준 작업 흐름은 100% 자가 운영
- 새 PC 추가, Manim 도입 등 큰 변화만 클로드와 상의

> 무리해서 빨리 익히지 않아도 됩니다. **시스템이 안정적으로 굴러가는 게 우선**, 자가 운영은 그 다음입니다.

---

## 📊 시스템 운영 체크리스트

### 매일 작업 시 (✅ 체크하면서)

- [ ] 작업 시작 전 `git pull` 했는가?
- [ ] 작업 중간에 큰 진전 있을 때마다 commit했는가?
- [ ] 작업 종료 시 `git push` 했는가?
- [ ] `.env`가 실수로 add되지 않았는지 확인했는가?

### 주간 점검

- [ ] GitHub repo 용량 확인 (1GB 이내)
- [ ] archive/ 폴더에 모든 발행 포스트 백업되어 있는가?
- [ ] 이미지 호스팅 URL 작동 확인 (랜덤 1편 검증)

### 월간 점검

- [ ] Google Drive `.env` 백업본이 최신인가?
- [ ] 자가 운영 가능한 명령은 어디까지인가?
- [ ] 다음 단계(Manim 등) 도입 준비 상태

---

## 🔗 관련 자료

| 자료 | 위치 |
|:---|:---|
| GitHub repo | https://github.com/winsososng/blog-images |
| 티스토리 블로그 | https://fafamath.tistory.com |
| 네이버 블로그 (메인) | https://blog.naver.com/winsosong |
| 네이버 수학블로그 | https://blog.naver.com/winsosong2 |
| 비번 백업 | Google Drive 비공개 문서 (본인만) |
| Phase 1~7 워크플로우 | 프로젝트 지식 v.140 가이드 참조 |

---

## 📝 정립 히스토리

### 2026-05-01 — v1.0 정립
- 예산컴퓨터에 두 번째 환경 구성
- 비번 하드코딩 → `.env` 분리 보안 조치
- Google Drive 비공개 문서로 비번 백업 채널 확립
- 멀티PC 동기화 정책 확립 (Git 중심)
- 동영상 별도 보관 정책 명시
- 관리자(클로드) / 작업자(Anti) 역할 분리 명문화

---

[멀티PC 블로그 시스템 운영 가이드 v1.0 — END]
