from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    # N, M : underground 크기
    # R, C : 처음 탈주범이 들어간 맨홀 위치
    # L : 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())
    underground = []
    for i in range(N):
        underground.append(list(map(int, input().split())))

    # 상하좌우 갈수있는 곳 -> 상좌우하로 풂 이번엔 (상하, 좌우 합이 3이 되는게 뒤에서 편함)
    pipe = {1 : [0, 1, 2, 3], 
            2 : [0, 3],
            3 : [1, 2], 
            4 : [0, 2], 
            5 : [2, 3],
            6 : [1, 3],
            7 : [0, 1]}

    # 맨홀 뚜껑으로부터 거리를 구한다음에, L 이하인 거리의 개수가 답이 될듯
    distance = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]

    # 갈 수 있는 곳을 모두 탐색
    q = deque([(R, C)])
    visited[R][C] = True

    while q:
        r, c = q.popleft()
        # 1 ~ 7번 파이프인 경우 이동할 수 있는 위치는 pipe[pipe_n]으로 확인
        pipe_n = underground[r][c]

        if pipe_n == 0:
            continue
        else:
            for d in pipe[pipe_n]:
                nr, nc = r + dr[d], c + dc[d]

                # 다음 위치의 파이프와 연결되어있으면(합이 3이면 연결됨)
                connected = False
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                next_pipe_n = underground[nr][nc]
                if next_pipe_n != 0:
                    for next_d in pipe[next_pipe_n]:
                        if d + next_d == 3:
                            connected = True
                    # 방문안했으면, 연결되어있으면
                    if not visited[nr][nc] and connected:
                        distance[nr][nc] = distance[r][c] + 1
                        q.append((nr, nc))
                        visited[nr][nc] = True

    # 이제 전체 underground에서 맨홀부터 거리가 L 이하인거 찾기(맨홀 위치 포함 -> 1에서 시작)
    answer = 1
    for row in range(N):
        for col in range(M):
            if 0 < distance[row][col] < L:
                answer += 1

    print(f"#{test_case} {answer}")