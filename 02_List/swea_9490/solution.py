import sys
sys.stdin = open("input.txt", "r")


def pang(ballons, r, c):
    radius = ballons[r][c]
    flowergaru = 0

    # row
    for pcol in range(c-radius, c+radius + 1):
        if 0 <= pcol < len(ballons[0]):
            flowergaru += ballons[r][pcol]

    # col
    for prow in range(r-radius, r+radius + 1):
        if 0 <= prow < len(ballons):
            flowergaru += ballons[prow][c]

    # twice : exclude
    flowergaru -= ballons[r][c]
    return flowergaru


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ballons = [list(map(int, input().split())) for _ in range(N)]
    best_garu = 0

    for row in range(N):
        for col in range(M):
            if best_garu < pang(ballons, row, col):
                best_garu = pang(ballons, row, col)

    print(f"#{tc} {best_garu}")
