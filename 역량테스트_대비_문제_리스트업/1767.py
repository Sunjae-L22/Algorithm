
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 가장자리 코어는 이미 연결됨 → 탐색 대상에서 제외 (보드엔 1로 남아 장애물 역할)
    cores = []
    for r in range(1 ,N-1):
        for c in range(1, N-1):
            if board[r][c] == 1:
                cores.append((r, c))
    M = len(cores)

    best_cnt, best_len = -1, 0

    def dfs(idx, cnt, length):
        global best_cnt, best_len

        # 가지치기: 남은 코어를 전부 연결해도 최고 기록을 못 넘으면 버림
        if cnt + (M - idx) < best_cnt:
            return

        if idx == M:
            # 연결된 코어 수가 더 많거나 코어 수는 같은데 길이가 더 짧을 때
            if cnt > best_cnt or (cnt == best_cnt and length < best_len):
                best_cnt, best_len = cnt, length
            return

        r, c = cores[idx]
        for d in range(4):
            # 경로가 뚫려 있는지 확인
            nr, nc, steps, ok = r + dr[d], c + dc[d], 0, True
            while 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != 0:
                    ok = False
                    break
                nr += dr[d]; nc += dc[d]
                steps += 1
            if not ok:
                continue

            # 뚫려있는 경로(상하좌우 중) 전선 그리기
            # 코어는 제외하고 주위부터 시작
            nr, nc = r + dr[d], c + dc[d]
            while 0 <= nr < N and 0 <= nc < N:
                board[nr][nc] = 2
                nr += dr[d]
                nc += dc[d]

            dfs(idx + 1, cnt + 1, length + steps)

            # 되돌리기
            nr, nc = r + dr[d], c + dc[d]
            while 0 <= nr < N and 0 <= nc < N:
                board[nr][nc] = 0
                nr += dr[d]
                nc += dc[d]

        dfs(idx + 1, cnt, length)  # 이 코어는 포기

    dfs(0, 0, 0)
    print(f'#{test_case} {best_len}')