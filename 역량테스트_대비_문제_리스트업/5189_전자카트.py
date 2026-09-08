from itertools import permutations

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    battery = []
    for _ in range(N):
        battery.append(list(map(int, input().split())))

    # 최대 1000이기 떄문에 1001에서 시작
    answer = 1001

    # 순열..? N이 10이라 가능할듯..? (9! = 362,880)
    for perm in permutations(range(2, N+1)):

        # 1번(사무실)에서 첫 번째 관리구역으로 가는거
        spent = battery[0][perm[0]-1]

        # 관리구역끼리 이동
        for i in range(N-2):
            spent += battery[perm[i]-1][perm[i+1]-1]
            # 가지치기?
            if spent > answer:
                break

        # 마지막 관리구역에서 다시 사무실로 돌아가는거
        spent += battery[perm[i+1]-1][0]
        answer = min(answer, spent)

    print(f"#{test_case} {answer}")