# 백준 → 개념 정리 → GitHub → 티스토리

이 흐름은 사용자가 직접 푼 뒤 설명할 수 있게 만드는 학습 루틴이다.
Codex가 문제 선정·검증·정리를 이어서 수행하고, 파일 생성과 반복 검사는 CLI가 맡는다.
파일 저장 감시나 정기 예약은 설치하지 않았다. 이 레포에서 요청할 때 실행한다.

## 평소에는 이렇게 요청한다

| 요청 | 이어서 수행할 작업 |
|---|---|
| 오늘 문제 골라줘 | 진행 중·복습 기한·기존 해결 목록 확인 → 개념/실전/도전 추천 |
| 이 문제 시작하자 | 공식 원문·현재 난이도 확인 → 코드·예제·노트 생성 |
| 힌트 하나만 줘 | 관찰 수준의 힌트부터 제공, 정답 코드는 요청 전 보류 |
| 2559 풀이 확인해줘 | 직접 작성한 코드 보존 → 테스트·반례·정당성·복잡도 검토 |
| 백준에서 맞았어 | 현재 코드가 제출한 코드인지 확인 → 사용자 보고로 AC 기록 |
| 푼 문제 정리해줘 | 풀이 기록·개념 노트·복습일·글감 판단·인덱스·GitHub 반영 |
| 누적합을 티스토리 글로 정리해줘 | 기존 글 대조 → 관련 풀이 묶기 → 본문·그림·검수·채팅 복사본 |

## 1. 문제 선정: 개념 2 · 실전 2 · 도전 1

2026-11-23 공개 프로필 기준 `sunaje0111`은 Gold III / 1,222 / 해결 412문제다.
이 수치는 관측 시점의 기준이며 자동으로 갱신되지는 않는다. 프로필과 연결된 BOJ 핸들을 확인했다.
기본 진단 문제를 반복하는 대신 이미 해결한 문제는 복습 때만 꺼낸다.

- 5문제 묶음은 개념 확장 2개, 코딩테스트 실전 2개, 도전 1개를 기본으로 한다.
- 개념은 현재 주제를 이해했는지 확인할 문제, 실전은 여러 조건을 끝까지 구현할 문제로 고른다.
- 도전은 현재 풀이 경험보다 한 단계 어려운 문제다. 티어와 풀이시간을 함께 확인한다.
- 기본·실전을 독립적으로 풀고 정당성을 설명하면 다음 개념 또는 난이도로 이동한다.
- 두 문제 연속으로 핵심 힌트가 필요하면 같은 개념의 쉬운 변형으로 돌아간다.
- 당일 복습 또는 진행 중 문제가 있으면 새 문제보다 먼저 처리한다.
- 태그는 학습용 분류다. 실전 연습에서는 문제를 고른 뒤 핵심 태그·풀이 설명을 가리고 시작한다.

```bash
python3 study-workflow/scripts/study.py next
python3 study-workflow/scripts/study.py next --concept 01_누적합 --limit 3
python3 study-workflow/scripts/study.py start 2143
```

`curriculum.json`은 작게 유지하는 검증된 후보 목록이다. 추가할 때 공식 문제의 제목·제한·예제를
확인하고 `id`, `title`, `concept`, `track`, `reason`, `url`, `verified_at`, `cases`를 기록한다.
하나의 주 개념 폴더만 사용하고 연관 개념은 `tags`에 둔다. 코드를 복제하지 않는다.
현재의 13개 후보는 시작점이며, 나머지 개념의 문제는 학습 기록에 맞춰 추가한다.

### 계정 기록과 개편 대응

solved.ac v4는 자체 문제 번호와 별도 계정을 사용한다. BOJ ID와 solved.ac ID는 별도 필드다.
2026-11-23 브라우저에서 해결 목록 9쪽의 412개 고유 ID를 확인했고 로컬 추천 캐시에 보관했다.
관측한 7개 기존 후보의 해결 여부는 공개 후보 목록에도 남겨 다른 환경에서 중복 추천을 줄인다.
전체 캐시는 Git에 포함하지 않는다. 새 컴퓨터에서는 최신 목록을 다시 확인한다.

```bash
# BOJ 번호를 직접 확인한 목록: [1000, 1001]
python3 study-workflow/scripts/study.py import-solved solved-boj.json \
  --namespace boj --observed-at 2026-11-23 --source '실제로 확인한 공개 URL 또는 사용자 제공 근거'

# solved.ac 번호는 문자열: ["1000", "19759a"]
python3 study-workflow/scripts/study.py import-solved solved-ac.json \
  --namespace solved_ac --observed-at 2026-11-23 --source '실제로 확인한 공개 URL'
```

이 명령은 외부 API를 호출하지 않는다. `solved_ac_id` 매핑을 확인한 문제만 해당 목록으로 제외한다.
새 관측으로 기존 해결 분류가 바뀌면 `prior_solved`와 출처도 함께 갱신한다.
구 v3 API는 사용하지 않는다. v4 자동 수집은 공식 인증·명세를 확인한 뒤 연결할 확장 지점이다.
현재 백준→solved.ac 자동 갱신이 지연될 수 있으므로, 최근 제출은 BOJ 판정 또는 사용자 보고로 확인한다.

## 2. 직접 풀기

`백준/개념별/<개념>/<번호>/`에 `solution.py`, `README.md`, `meta.json`, `tests/`를 둔다.
처음에는 조건 요약·예상 복잡도·접근을 짧게 메모하고 구현한다. 한 번에 막힌 코드를 지우지 않는다.
필요하면 `attempts/`에 당시 코드를 남기고 이유를 적되 실제 경험만 쓴다.

개념 문제는 20~30분, 실전은 40~60분, 도전은 60~90분을 초기 타임박스로 삼는다.
이는 서비스 규칙이나 능력 평가 기준이 아니라 조정 가능한 학습 운영값이다.

## 3. 테스트와 온라인 판정

```bash
python3 study-workflow/scripts/study.py test 2559
python3 study-workflow/scripts/study.py test 2559 --timeout 3
```

공식 예제와 자체 경계 입력은 `tests/README.md`에 구별한다. 입력은 `.in`, 기댓값은 같은 이름의
`.out`이다. 테스트가 없거나 짝이 누락되면 실패한다. 빈 코드도 실패한다.
출력 비교는 줄 끝 공백과 마지막 줄바꿈만 무시한다. 실수 오차·스페셜 저지·다중 정답에는
이 단순 비교기를 정답 판정기로 사용하지 말고 문제별 검증기를 추가한다.
로컬 시간 제한은 개발 편의용이다. BOJ 시간·메모리 한도를 만족했다는 뜻이 아니다.

사용자가 직접 제출한 뒤 결과를 기록한다. 코드 해시를 남기므로 제출 코드와 로컬 코드가 같아야 한다.

```bash
python3 study-workflow/scripts/study.py record 2559 --verdict AC \
  --source user_report --evidence '사용자가 현재 solution.py로 맞았습니다를 받았다고 보고'
```

직접 채점 페이지를 열고 번호·계정·결과·대상 코드를 확인했다면 `--source page_verified`와
실제 BOJ URL을 사용한다. 명령에 URL을 입력한 것 자체는 자동 검증이 아니다.
틀린 결과도 `WA`, `TLE`, `MLE`, `RE`, `CE`로 기록한다. 과거 제출 이력은 보존한다.

## 4. 풀이·개념 정리와 복습

문제의 README에 조건 요약, 접근 선택, 정당성, 경계 입력, 시간·공간 복잡도,
다음에 기억할 판단 기준, 블로그 적합성을 쓴다. `TODO`를 채운 뒤 검토한다.
필요한 경우 작은 완전탐색 기준 구현과 무작위 입력을 비교하고 seed·실행 결과도 보관한다.
개념 폴더의 README에는 사용 조건·불변식·반례·다른 접근 비교를 축적한다.

```bash
python3 study-workflow/scripts/study.py review 2559 \
  --note '실제로 수행한 정당성·복잡도·경계 입력 검토 내용' \
  --blog candidate --blog-reason '여러 구간 처리 방식의 차이를 설명할 수 있음'
python3 study-workflow/scripts/study.py index
python3 study-workflow/scripts/study.py check
```

정리 완료에는 현재 코드의 로컬 통과, AC 근거, 완성된 노트가 필요하다.
코드·테스트·노트 수정 후에는 이전 검토가 만료되며 재검토해야 한다.
첫 검토 3일 뒤, 다음 성공 복습 7일 뒤, 그다음 21일 뒤를 기록한다.
복습에서는 노트를 가리고 아이디어·정당성·복잡도를 설명하거나 다시 구현한다.
막혔다면 같은 명령에 `--result retry`를 추가해 하루 뒤 다시 보게 한다.
이 날짜는 후보 선정용이며 알림을 예약하지 않는다.

## 5. GitHub 정리

학습 완료 요청에 대한 기본 마무리다. `check` 후 변경 파일을 확인하고 이번에 완성한 코드·노트·
메타데이터·테스트·생성 인덱스만 커밋한다. 코드가 비어 있는 시작 폴더를 준비할 때는
커밋 제목에 `start`를 사용해 완성 풀이와 구분한다.

```text
study(boj): start 2559 수열
solve(boj): review 2559 수열 and prefix-sum notes
review(boj): revisit 2559 and refine invariants
```

원격은 `Sunjae-L22/Algorithm`, 브랜치는 `master`다. 원격과 로컬이 동기화되어 있고 다른 작업의
미푸시 커밋이 없는지 확인한 뒤 명시적인 파일 목록으로 커밋·푸시한다. `git add .`를 쓰지 않는다.
커밋 SHA와 원격 SHA가 일치해야 완료다. 강제 푸시는 사용하지 않는다.
CI는 도구 회귀 테스트와 기록 구조를 검사한다. 빈 풀이를 정답으로 인증하지 않는다.

## 6. 글감 선별 → 본문·그림 패키지

모든 문제를 블로그 글로 만들지는 않는다. 다음 중 설명할 가치가 있는 질문을 골라 묶는다.

- 비슷한 방법의 사용 조건이 갈리는가? 예: 누적합과 고정/가변 구간.
- 자주 틀리는 경계를 작은 반례 하나로 설명할 수 있는가?
- 같은 개념이 다른 문제에서 어떻게 변형되는가?
- 더 빠른 구현을 선택한 근거를 정당성과 복잡도로 설명할 수 있는가?

실제 풀이가 정리된 뒤 패키지를 만든다. 아래 명령의 번호는 해당 문제를 완료한 뒤 사용한다.

```bash
python3 -m pip install -r study-workflow/requirements-blog.txt
python3 study-workflow/scripts/blog.py catalog --config blog-workflow/config.json
python3 study-workflow/scripts/study.py blog prefix-sum-windows \
  --ids 2559 2143 --title '구간 합을 계산하는 방법을 어떻게 고를까?'
```

`blog-workflow/posts/<slug>/`는 Git에서 제외한 로컬 작성 공간이다.
`post.md` 본문, `post.json` 제목·태그·출처·그림 목록, `visual-brief.md` 제작 계획,
`img/` 실제 이미지, `QA_REPORT.md` 실제 검수, `evidence/` 버전 고정 풀이 기록을 보관한다.
생성 명령은 초안 틀과 근거 묶음만 만든다. 완성 글·그림은 Codex가 `tistory-post` 스킬에 따라 작성한다.

기존 공개 글 목록과 TIL을 확인해 신규/보강을 판단한다. 제목 유사도만으로 중복이라고 확정하지 않는다.
현재 Algorithm의 개념 노트를 원본으로 삼고 TIL에 같은 글을 자동 중복 생성하지 않는다.
자연스러운 -다체, 독자 질문, 자체 예제, 증명, 코드, 반례, 복잡도를 연결한다.
사용자가 제공하지 않은 실패 경험이나 해결 성과를 만들어내지 않는다.
그림은 루트 `DESIGN.md` 기준으로 만들고 실제 크기와 모바일에서 검수한다.

```bash
python3 study-workflow/scripts/blog.py check blog-workflow/posts/prefix-sum-windows
python3 study-workflow/scripts/blog.py preview blog-workflow/posts/prefix-sum-windows
# 본문·메타데이터·그림·QA를 실제로 검토하고 review의 technical/visual을 true로 기록한 뒤:
python3 study-workflow/scripts/study.py blog-ready prefix-sum-windows
python3 study-workflow/scripts/study.py handoff prefix-sum-windows
```

`blog-ready`는 미완성 표시, 없는 그림, 바뀐 근거, 검수 기록 누락을 막는다.
검사 통과가 기술적 정답·시각 품질의 자동 보증은 아니다. 검수 플래그는 실제 관찰 뒤에만 올린다.
원고·이미지를 바꾸면 다시 준비 상태를 검증해야 한다.
`handoff`는 본문 전체를 코드 블록 하나에 담고 이미지 위치 주석을 유지하며 실제 이미지 경로를
순서대로 출력한다. Codex는 이 내용을 채팅에 전달한다. ZIP은 요청할 때만 만든다.

## 7. 티스토리 직접 작성 후 연결

기본 완료 상태는 `ready_for_user_authoring`이다. 사용자가 직접 작성·업로드·발행한다.
공개 URL을 제공하고 검증을 요청하면 다음 읽기 전용 절차를 사용한다.

```bash
python3 study-workflow/scripts/blog.py verify-public blog-workflow/posts/prefix-sum-windows \
  --config blog-workflow/config.json --url '실제 공개 글 URL'
python3 study-workflow/scripts/blog.py record-publication blog-workflow/posts/prefix-sum-windows \
  --config blog-workflow/config.json --url '실제 공개 글 URL' --status published \
  --observation '실제로 확인한 본문·코드·이미지 표시 결과'
```

HTTP 200만으로 발행을 확인하지 않는다. 실제 본문과 이미지 표시까지 확인한 뒤
개념 노트의 관련 글 링크를 추가하고 선택한 공개 노트만 GitHub에 반영한다.

## 설치와 점검

핵심 학습 CLI는 Python 3.11 이상 표준 라이브러리로 실행된다.
블로그 도구는 `markdown-it-py`가 필요하며 현재 macOS/Linux를 대상으로 검증한다.
재사용한 `blog.py`의 출처는 `SOURCES.md`에 기록했다.

```bash
python3 -m unittest discover -s study-workflow/tests -v
python3 study-workflow/scripts/study.py check
```

여러 프로세스에서 같은 문제의 메타데이터를 동시에 수정하지 않는다. 파일 저장은 원자적으로
교체하지만 작업 전체에 대한 동시 편집 병합 기능은 없다.
