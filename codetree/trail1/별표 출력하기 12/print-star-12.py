N = int(input())

M = N if N % 2 == 0 else N - 1
M = max(M, 1)

for r in range(1, M + 1):
    line = [' '] * (2 * N - 1)
    for k in range(1, N + 1):
        if r == 1 or (k % 2 == 0 and r <= k):
            line[2 * (k - 1)] = '*'
    print(''.join(line).rstrip())