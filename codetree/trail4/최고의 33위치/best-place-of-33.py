N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# Please write your code here.
for row in range(N-2):
    for col in range(N-2):
        coin = 0
        for r in range(row, row+3):
            for c in range(col, col+3):
                if grid[r][c] == 1:
                    coin += 1
        answer = max(coin, answer)

print(answer)