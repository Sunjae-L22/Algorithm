# 출처와 확인 범위

확인일: 2026-11-23 (Asia/Seoul).

- [BOJ 서비스 재개 안내](https://acmicpc.net/): 공식 홈의 서비스 재개 안내 확인.
- [solved.ac 개편 공지](https://solved.ac/notices/v4): 별도 핸들, 자체 문제 ID, 태그 변경 확인.
- [API 제공 공지](https://solved.ac/notices/261117-api): 구 v3 지원 종료와 v4 안내 확인.
- [v4 문서](https://backstage.solved.ac/developer/docs): 공개 요청에서는 로그인 진입만 확인.
  인증과 세부 스키마는 검증하지 않았으므로 자동 API 연동을 구현하지 않았다.
- [BOJ 수동 갱신 안내](https://solved.ac/notices/261120-boj-manual): 실시간 갱신 지연 안내 확인.
- [sunaje0111 프로필](https://solved.ac/u/sunaje0111): 브라우저에서 Gold III, 1,222,
  해결 412문제와 연결된 BOJ 계정 확인. 일반 HTTP 접근 실패를 브라우저 조회로 보완했다.
- [해결 목록](https://solved.ac/ko/problems?q=%40sunaje0111): 브라우저의 9쪽, 고유 ID 412개.
  solved.ac ID는 BOJ 번호로 일괄 변환하지 않고 별도 캐시에 저장했다.
- 후보 문제의 공식 원문 링크와 확인일은 `curriculum.json`에 있다.
  문제 전체 지문과 공식 이미지를 복사하지 않고 제목·링크·필요한 예제만 사용했다.
- 2143 난이도는 [계정의 미해결 누적합 검색](https://solved.ac/ko/problems?q=-%40sunaje0111+%23prefix_sum)
  결과에서 Gold III로 확인했다. 난이도를 조회하지 않은 후보는 null로 유지한다.

## 블로그 연결

대상 블로그는 기존 TIL 프로젝트의 현재 설정에서 확인한
[공부 기록 블로그](https://it-study-2002.tistory.com)다.
새 글마다 공개 목록과 실제 본문을 다시 대조한다. 이번 설치가 기존 글의 일괄 조사·수정은 아니다.

`scripts/blog.py`는 현재 설치된 사용자 `tistory-post` 스킬의 블로그 검사·미리보기·공개 검증 도구를
2026-11-23에 복사해 재사용했다. 사용자 홈의 절대 경로에 의존하지 않도록 저장소에 포함했다.
기존 TIL 전용 `github_sync.py`는 가져오지 않았다. 원격·파일 구조가 달라 이 레포의 명시적 Git 절차를 사용한다.

도구의 회귀 테스트는 임시 폴더의 합성 문제로 수행한다. 합성 테스트의 판정 기록은 사용자 풀이 실적이 아니다.
