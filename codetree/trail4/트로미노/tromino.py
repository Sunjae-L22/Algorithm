N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
nums = []
# 기다란 모양 먼저
# 누운 경우
for row in range(N):
    for col in range(M-2):
        nums.append(grid[row][col] + grid[row][col+1] + grid[row][col+2])

# 서있는 경우
for col in range(M):
    for row in range(N-2):
        nums.append(grid[row][col] + grid[row+1][col] + grid[row+2][col])

# 이제 ㄴ자 모양 
# 그대로인 경우
for row in range(N-1):
    for col in range(M-1):
        nums.append(grid[row][col] + grid[row+1][col] + grid[row+1][col+1])

# 90도 회전
for row in range(N-1):
    for col in range(M-1):
        nums.append(grid[row][col] + grid[row+1][col] + grid[row][col+1])

# 180도 회전
for row in range(N-1):
    for col in range(M-1):
        nums.append(grid[row][col] + grid[row][col+1] + grid[row+1][col+1])

# 270도 회전
for row in range(N-1):
    for col in range(M-1):
        nums.append(grid[row+1][col] + grid[row][col+1] + grid[row+1][col+1])

print(max(nums))        