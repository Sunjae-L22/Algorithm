T = int(input())


def paris(grid, start_x, start_y, size):
    sum_paris = 0
    for i in range(size):
        for j in range(size):
            sum_paris += grid[start_x + i][start_y + j]
    return sum_paris


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [[0] * N for i in range(N)]
    for i in range(N):
        grid[i] = list(map(int, input().split()))

    max_paris = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            max_paris = max(max_paris, paris(grid, i, j, M))
    print(f"#{test_case} {max_paris}")