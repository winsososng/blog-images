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
