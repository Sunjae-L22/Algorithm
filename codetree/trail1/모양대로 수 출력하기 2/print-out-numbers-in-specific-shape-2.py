N = int(input())
cnt = 2
for i in range(N):
    for j in range(N):
        print(cnt, end = ' ')
        if cnt == 8:
            cnt = 2
        else:
            cnt += 2
    print()