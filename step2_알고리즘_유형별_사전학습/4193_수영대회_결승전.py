from collections import deque

def bfs(N, grid, start, finish):
    sx, sy = start
    fx, fy = finish

    if (sx, sy) == (fx, fy):
        return 0

    # visited[row][col][time % 3]
    visited = [[[False] * 3 for _ in range(N)] for _ in range(N)]
    visited[sx][sy][0] = True

    q = deque()
    q.append((sx, sy, 0))  # (row, col, time)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]  # 상 하 좌 우 정지

    while q:
        r, c, t = q.popleft()
        nt = t + 1
        phase = nt % 3

        for dr, dc in directions:
            if dr == 0 and dc == 0:
                nr, nc = r, c 
            else:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if grid[nr][nc] == 1:
                    continue
                if grid[nr][nc] == 2 and t % 3 != 2:
                    # 소용돌이가 아직 돌아가는 상태면 대기
                    continue

            if visited[nr][nc][phase]:
                continue
            visited[nr][nc][phase] = True

            if (nr, nc) == (fx, fy):
                return nt

            q.append((nr, nc, nt))

    return -1


T = int(input())
results = []
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())

    ans = bfs(N, grid, (sx, sy), (fx, fy))
    results.append(f"#{tc} {ans}")

print('\n'.join(results))