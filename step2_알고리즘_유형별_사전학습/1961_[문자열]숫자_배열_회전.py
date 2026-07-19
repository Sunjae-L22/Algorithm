T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    original = [[0] * N for i in range(N)]

    for i in range(N):
        original[i] = list(map(int, input().split()))

    rotate_90 = [[0] * N for i in range(N)]
    rotate_180 = [[0] * N for i in range(N)]
    rotate_270 = [[0] * N for i in range(N)]

    # 90도 돌릴 경우
    for i in range(N):
        for j in range(N):
            rotate_90[i][j] = original[N-1-j][i]

    # 180도 돌릴 경우
    for i in range(N):
        for j in range(N):
            rotate_180[i][j] = original[N-1-i][N-1-j]

    # 270도 돌릴 경우
    for i in range(N):
        for j in range(N):
            rotate_270[i][j] = original[j][N-1-i]

    print(f"#{test_case}")
    for i in range(N):
        for num in rotate_90[i]:
            print(num, end = "")
        print(" ", end = "")
        for num in rotate_180[i]:
            print(num, end = "")
        print(" ", end = "")
        for num in rotate_270[i]:
            print(num, end = "")
        print("")