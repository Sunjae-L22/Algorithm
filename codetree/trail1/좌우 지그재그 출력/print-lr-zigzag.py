N = int(input())
for r in range(N):
    for c in range(N):
        if r % 2 == 0:
            print(r * N + c + 1, end = ' ')
        else:
            print(N * (r+1) - c, end = ' ')
    print()