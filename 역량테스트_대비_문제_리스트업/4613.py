# a개에서 W, B, R의 경계 두개를 뽑는 경우의 리스트를 반환하는 콤비네이션 함수
def combination(a):
    res = []

    for i in range(a):
        for j in range(i+1, a):
            res.append((i, j))

    return res

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    flag = []
    
    for i in range(N):
        flag.append(list(input()))

    # paint = 0
    # # 첫 줄은 하얀색으로 칠하기
    # for col in range(M):
    #     if flag[0][col] != 'W':
    #         paint += 1

    # # 마지막 줄은 빨간색으로 칠하기
    # for col in range(M):
    #     if flag[N-1][col] != 'R':
    #         paint += 1

    # 중간 줄 -> W, B, R가 순서대로 나오므로 가능한 조합(49 combination 2) 찾기
    W_B_boarder, B_R_boarder = 0, 0
    possible_boarder = combination(N-1)
    paints = []

    for boarders in possible_boarder:
        paint = 0
        W_B_boarder = boarders[0]
        B_R_boarder = boarders[1]

        for i in range(0, 1+W_B_boarder):
            for col in range(M):
                if flag[i][col] != 'W':
                    paint += 1

        for i in range(1+W_B_boarder, 1+B_R_boarder):
            for col in range(M):
                if flag[i][col] != 'B':
                    paint += 1

        for i in range(1+B_R_boarder, N):
            for col in range(M):
                if flag[i][col] != 'R':
                    paint += 1

        paints.append(paint)
    answer = min(paints)

    print(f"#{test_case} {answer}")