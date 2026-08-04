T = int(input())


# 뒤집어진 이진수 만드는 함수
def num_to_binary(num):
    res = []
    while num > 0:
        tmp = num % 2
        res.append(tmp)
        num = num // 2
    return res


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    num_binary = num_to_binary(M)
    switch = "ON"
    if len(num_binary) < N:
        switch = "OFF"

    else:
        for i in range(0, N):
            if num_binary[i] == 0:
                switch = "OFF"

    print(f"#{test_case} {switch}")