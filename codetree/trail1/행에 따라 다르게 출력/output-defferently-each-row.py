cnt = 0
N = int(input())
for r in range(N):
    for c in range(N):
        if r % 2 == 0:
            cnt += 1
        else:
            cnt += 2
        print(cnt, end = ' ')
    print()