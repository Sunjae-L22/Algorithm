T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    counted = [False] * 10
    turn = 1

    while True:
        sheep_n = turn * N
        for num in str(sheep_n):
            counted[int(num)] = True
        if sum(counted) == 10:
            break
        else:
            turn += 1

    print(f"#{test_case} {turn*N}")