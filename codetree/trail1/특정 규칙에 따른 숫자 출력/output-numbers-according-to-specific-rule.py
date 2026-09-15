N = int(input())
cnt = 0
for i in range(N):
    line = '  ' * i
    print(line, end = '')
    for j in range(N-i):
        if cnt == 9:
            cnt = 0
        cnt += 1
        print(cnt, end = ' ')
    print()
        