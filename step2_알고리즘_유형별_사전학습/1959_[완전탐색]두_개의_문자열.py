T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # N이 더 클 경우 -> 순서를 바꿔버림
    if M < N:
        tmp = M
        M = N
        N = tmp
        tmp_2 = Bj
        Bj = Aj
        Aj = tmp_2

    # Aj와 Bj의 곱을 저장한 행렬(N X M)
    prod_arr = [[0] * M for i in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            prod_arr[i][j] = Aj[i] * Bj[j]

    # 대각선으로 합을 구해서 큰 걸 답으로 업데이트
    for k in range(M-N+1):
        tmp_sum = 0
        for l in range(N):
            tmp_sum += prod_arr[l][k+l]
        if tmp_sum > answer:
            answer = tmp_sum

    print(f"#{test_case} {answer}")