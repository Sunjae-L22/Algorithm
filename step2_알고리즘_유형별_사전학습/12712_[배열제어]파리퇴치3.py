T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pari_array = [[0] * N for i in range(N)]

    for i in range(N):
        pari_array[i] = list(map(int, input().split()))

    answer = 0

    # + -> 상하좌우
    dir_x = [0, 0, -1, 1]
    dir_y = [-1, 1, 0, 0]

    # 중심 : (0, 0) ~ (N-1, N-1)
    for i in range(N):
        for j in range(N):
            start_x = i
            start_y = j
            paris = pari_array[start_x][start_y]
            for k in range(1, M):
                for l in range(4):
                    if 0 <= start_x + dir_x[l]*k < N and 0 <= start_y + dir_y[l]*k < N:
                        paris += pari_array[start_x + dir_x[l]*k][start_y + dir_y[l]*k]

            if paris > answer:
                answer = paris
                print(answer)

    # X -> 1, 2, 3, 4분면
    dir_x = [1, -1, -1, 1]
    dir_y = [-1, -1, 1, 1]

    # 중심 : (0, 0) ~ (N-1, N-1)
    for i in range(N):
        for j in range(N):
            start_x = i
            start_y = j
            paris = pari_array[start_x][start_y]
            for k in range(1, M):
                for l in range(4):
                    if 0 <= start_x + dir_x[l] * k < N and 0 <= start_y + dir_y[l] * k < N:
                        paris += pari_array[start_x + dir_x[l] * k][start_y + dir_y[l] * k]

            if paris > answer:
                answer = paris
                print(answer)

    print(f"#{test_case} {answer}")