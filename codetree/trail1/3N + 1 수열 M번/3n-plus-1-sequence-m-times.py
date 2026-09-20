M = int(input())
for tc in range(M):
    N = int(input())
    cnt = 0
    while True:
        if N == 1:
            break
        else:
            cnt += 1
            if N % 2 == 1:
                N = N * 3 + 1
            else:
                N //= 2
    print(cnt)
            