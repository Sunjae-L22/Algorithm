N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
# 행, 열 따로 살펴보기
answer = 0
for row in range(N):
    max_cont = 1
    cont = 1
    prev = 0
    for col in range(N):
        if grid[row][col] == prev:
            cont += 1
            max_cont = max(max_cont, cont)
        else:
            prev = grid[row][col]
            cont = 1
    if max_cont >= M:
        answer += 1

for col in range(N):
    max_cont = 1
    cont = 1
    prev = 0
    for row in range(N):
        if grid[row][col] == prev:
            cont += 1
            max_cont = max(max_cont, cont)
        else:
            prev = grid[row][col]
            cont = 1
    if max_cont >= M:
        answer += 1

print(answer)