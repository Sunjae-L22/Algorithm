N = int(input())
for r in range(N):
    for c in range(1, N+1):
        print(r * N + c, end = ' ')
    print()