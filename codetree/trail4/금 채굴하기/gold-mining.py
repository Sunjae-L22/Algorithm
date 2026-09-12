N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

# k와 grid, 중심 위치가 주어졌을 때 영역 안에 있는 금의 개수 return하는 함수
def mareummo(k, grid, center):
    center_r, center_c = center
    gold = 0

    for row in range(center_r - k, center_r + k + 1):
        for col in range(center_c - (k - (abs(row - center_r))), center_c + (k - (abs(row - center_r))) + 1):
            if 0 <= row < N and 0 <= col < N and grid[row][col] == 1:
                gold += 1

    return gold


answer = 0
for k in range(N+1):
    for r in range(N):
        for c in range(N):
            gold_n = mareummo(k, grid, (r, c))
            gold_value = gold_n * M
            if gold_value >= (k ** 2 + (k + 1) ** 2):
                answer = max(answer, gold_n)

print(answer)
