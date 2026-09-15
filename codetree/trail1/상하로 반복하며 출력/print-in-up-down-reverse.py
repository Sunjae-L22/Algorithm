N = int(input())
arr = [[0] * N for _ in range(N)]
for c in range(N):
    for r in range(N):
        if c % 2 == 0:
            arr[r][c] = r+1
        else:
            arr[r][c] = N-r

for r in range(N):
    for c in range(N):
        print(arr[r][c], end = '')
    print()