T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))

    # 누적 당근 개수 합 리스트
    agg_carrot = [carrot_list[0]]
    for i in range(1, N):
        agg_carrot.append(agg_carrot[i-1] + carrot_list[i])

    # 차이가 최대로 나려면 첫번째 일꾼이 0개, 두번째 일군이 다!
    diff = agg_carrot[-1]
    area = 0

    for i in range(N):
        a = agg_carrot[i]
        b = agg_carrot[-1] - a
        if abs(a - b) < diff:
            area = i
            diff = abs(a - b)

    print(f"#{test_case} {area+1} {diff}")