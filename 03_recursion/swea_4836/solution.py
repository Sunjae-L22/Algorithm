import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    board = [[0] * 10 for _ in range(10)]
    N = int(input())
    for coloring in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                board[row][col] += color
    print(board)

    cnt = 0
    for row in range(0, 10):
        for col in range(0, 10):
            if board[row][col] == 3:
                cnt += 1

    print(f"#{tc} {cnt}")