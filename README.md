# Algorithm

알고리즘 개념을 배우고, 직접 문제를 풀고, 설명할 수 있는 지식으로 정리한다.
기존 SWEA·Programmers·Codetree 풀이에 백준 학습 파이프라인을 추가했다.

- **[백준 학습 현황·개념별 목차](백준/README.md)**
- **[문제 선정부터 티스토리 작성 준비까지](study-workflow/PIPELINE.md)**
- [첫 학습 세션](study-workflow/FIRST_SESSION.md)
- **[선재의 문제 수첩 · 웹 대시보드](https://sunjae-problem-notebook.vongole.chatgpt.site)** · [사용법과 동기화](study-workflow/dashboard/README.md)

```text
문제 선정 → 직접 풀이 → 로컬 테스트 → BOJ 판정 기록
         → 정당성·복잡도 검토 → 개념 노트·복습일 → GitHub
         → 글감 선별 → 티스토리 본문·그림·검수 → 직접 작성
```

이 레포를 열고 “오늘 문제 골라줘”, “2559 풀이 확인해줘”,
“푼 문제 정리하고 GitHub에 반영해줘”, “이 개념을 티스토리 글로 정리해줘”라고 요청하면 된다.
구체적인 처리 기준은 [AGENTS.md](AGENTS.md)에 있다.

터미널에서는 다음 명령으로 시작한다. Python 3.11 이상이 필요하다.

```bash
python3 study-workflow/scripts/study.py next
python3 study-workflow/scripts/study.py test 2559
```

첫 문제의 `solution.py`는 직접 풀 수 있도록 비어 있다. 기존 해결 목록과 새로 검토한 풀이,
로컬 테스트와 온라인 판정, GitHub 반영과 티스토리 공개 상태는 각각 구분한다.
