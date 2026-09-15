N = int(input())
cnt = 0
for i in range(1, N+1):
    for j in range(i):
        cnt += 1
        print(cnt, end = ' ')
    print()