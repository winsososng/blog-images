#!/bin/bash
# ═══════════════════════════════════════════════
# 📂 수학 블로그 HTML 빌더 — 프로젝트 초기 세팅
# ═══════════════════════════════════════════════
#
# 사용법:
#   cd C:\Claude_Code\blog
#   bash setup.sh
#
# 또는 안티(Claude Code)에게:
#   "setup.sh 실행해서 폴더 세팅해줘"
#
# ═══════════════════════════════════════════════

set -e

# ── 프로젝트 루트 ──
PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
echo ""
echo "═══════════════════════════════════════════════"
echo "📂 수학 블로그 HTML 빌더 — 초기 세팅"
echo "═══════════════════════════════════════════════"
echo ""
echo "📍 프로젝트 경로: $PROJECT_ROOT"
echo ""

# ── 폴더 생성 ──
echo "📁 폴더 구조 생성 중..."

mkdir -p "$PROJECT_ROOT/input/images"
mkdir -p "$PROJECT_ROOT/output/assets"
mkdir -p "$PROJECT_ROOT/archive"

echo "   ✅ input/"
echo "   ✅ input/images/"
echo "   ✅ output/"
echo "   ✅ output/assets/"
echo "   ✅ archive/"
echo ""

# ── work_order 템플릿 복사 ──
if [ ! -f "$PROJECT_ROOT/input/work_order.md" ]; then
  if [ -f "$PROJECT_ROOT/work_order_template.md" ]; then
    cp "$PROJECT_ROOT/work_order_template.md" "$PROJECT_ROOT/input/work_order.md"
    echo "📋 work_order.md 템플릿 → input/ 복사 완료"
  else
    echo "⚠️  work_order_template.md가 없습니다. 수동으로 넣어주세요."
  fi
else
  echo "📋 input/work_order.md 이미 존재 — 건너뜀"
fi

# ── .gitignore 생성 ──
if [ ! -f "$PROJECT_ROOT/.gitignore" ]; then
  cat > "$PROJECT_ROOT/.gitignore" << 'EOF'
# 산출물 (빌드할 때마다 재생성)
output/*.html
output/assets/*

# OS
.DS_Store
Thumbs.db
desktop.ini

# 에디터
*.swp
*.swo
*~
EOF
  echo "📄 .gitignore 생성 완료"
else
  echo "📄 .gitignore 이미 존재 — 건너뜀"
fi

# ── README 생성 ──
if [ ! -f "$PROJECT_ROOT/README.md" ]; then
  cat > "$PROJECT_ROOT/README.md" << 'EOF'
# 📐 수학 블로그 HTML 빌더

**변호사아빠의 수학특강** (fafamath.tistory.com) 티스토리 포스트 빌드 시스템

## 📂 폴더 구조

```
blog/
├── CLAUDE.md               ← 안티의 기본 룰 (항상 적용)
├── work_order_template.md   ← 작업지시서 템플릿 (원본)
├── setup.sh                 ← 이 세팅 스크립트
├── README.md                ← 이 파일
│
├── input/                   ← 🔽 재료를 여기에 넣기
│   ├── work_order.md        ← 건별 작업지시서 (매번 수정)
│   ├── master_고1.md        ← 마스터원고 (Phase 3)
│   ├── master_고3.md        ← 마스터원고 (Phase 3)
│   └── images/              ← 이미지 파일들
│       ├── img01.png
│       └── ...
│
├── output/                  ← 🔼 결과물이 여기에 생성됨
│   ├── post_고1.html        ← 완성 HTML (티스토리 붙여넣기)
│   ├── post_고3.html        ← 완성 HTML (티스토리 붙여넣기)
│   └── assets/              ← 추가 리소스 (필요시)
│
└── archive/                 ← 📦 발행 완료된 파일 보관
    ├── 2026-04-02_이차함수넓이/
    └── ...
```

## 🔄 작업 흐름

1. `input/work_order.md` 작성 (템플릿에서 [...] 부분 채우기)
2. `input/`에 마스터원고(md) + 이미지 넣기
3. 안티에게: **"work_order 읽고 빌드해줘"**
4. `output/`에서 HTML 확인
5. 티스토리 글쓰기 → HTML 모드 → 붙여넣기 → 발행
6. 발행 완료 후 `archive/`로 이동 (선택)

## 📋 안티에게 주는 명령어 예시

```
# 기본 빌드
"work_order 읽고 빌드해줘"

# 고1만
"고1용만 빌드해줘"

# 수정
"output/post_고1.html의 섹션 3 수식 강조 더 세게 해줘"

# 아카이브
"오늘 결과물 archive에 정리해줘"
```
EOF
  echo "📖 README.md 생성 완료"
else
  echo "📖 README.md 이미 존재 — 건너뜀"
fi

# ── 최종 구조 출력 ──
echo ""
echo "═══════════════════════════════════════════════"
echo "✅ 세팅 완료! 최종 폴더 구조:"
echo "═══════════════════════════════════════════════"
echo ""
echo "  $PROJECT_ROOT/"
echo "  ├── CLAUDE.md              ← 기본 룰"
echo "  ├── work_order_template.md ← 템플릿 원본"
echo "  ├── setup.sh"
echo "  ├── README.md"
echo "  ├── .gitignore"
echo "  │"
echo "  ├── input/"
echo "  │   ├── work_order.md      ← 여기에 건별 지시 작성"
echo "  │   └── images/"
echo "  │"
echo "  ├── output/"
echo "  │   └── assets/"
echo "  │"
echo "  └── archive/"
echo ""
echo "═══════════════════════════════════════════════"
echo ""
echo "📋 다음 단계:"
echo "  1. input/work_order.md 에서 [...] 부분을 채우세요"
echo "  2. input/ 에 마스터원고(md)와 이미지를 넣으세요"
echo "  3. 안티에게: \"work_order 읽고 빌드해줘\""
echo ""
echo "═══════════════════════════════════════════════"
