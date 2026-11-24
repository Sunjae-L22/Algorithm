# Algorithm

알고리즘 개념을 배우고, 직접 문제를 풀고, 설명할 수 있는 지식으로 정리한다.
기존 SWEA·Programmers·Codetree 풀이에 백준 학습 파이프라인을 추가했다.

- **[브라우저에서 풀이 시작·이어하기](https://codespaces.new/Sunjae-L22/Algorithm?ref=master&quickstart=1)**
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

## 다른 컴퓨터에서 이어하기

GitHub에 같은 계정으로 로그인하고 위의 브라우저 풀이 링크를 연다. 처음에는 Codespace를 한 번 생성하고, 다른 컴퓨터에서는 기존 공간을 다시 연다. [내 Codespaces 목록](https://github.com/codespaces)에서도 이름으로 찾을 수 있다.

초기 설정을 마치면 브라우저 VS Code에서 Python 3.12로 풀이와 테스트를 실행할 수 있다. 코드의 인라인 제안은 꺼져 있다. 작업 중인 파일은 저장한 뒤 같은 공간에서 이어간다. 장기 보관할 풀이와 검토 기록은 검수 후 GitHub에 커밋·푸시한다. 대시보드에는 master에 올린 기록이 반영된다.

티스토리 초안과 계정 캐시는 해당 공간의 비공개 작업 파일이다. 공간을 삭제하면 함께 사라지므로 필요한 초안은 삭제 전에 개인 저장소에 백업한다. 기존 컴퓨터에만 있는 비공개 파일은 새 공간에 자동 복사되지 않는다.

터미널에서 다음 명령으로 시작한다.

```bash
python3 study-workflow/scripts/study.py next
python3 study-workflow/scripts/study.py test 2559
```

기존 해결 목록과 새로 검토한 풀이,
로컬 테스트와 온라인 판정, GitHub 반영과 티스토리 공개 상태는 각각 구분한다.
