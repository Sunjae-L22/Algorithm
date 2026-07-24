T = int(input())

def classify_fruits(weight_list, k1, k2):
    n_good = 0
    n_normal = 0
    n_bad = 0

    for weight in weight_list:
        if weight <= k1:
            n_bad += 1
        elif k1 < weight <= k2:
            n_normal += 1
        else:
            n_good += 1

    return n_good, n_normal, n_bad, max(n_good, n_normal, n_bad) - min(n_good, n_normal, n_bad)

for _ in range(T):
    # n : 과일의 개수, weight_list : 과일의 무게 리스트, low : 세 등급에 속한 과일의 최소 개수, high : 세 등급에 속한 과일의 최대 개수
    n , low, high = map(int, input().split())
    weight_list = list(map(int, input().split()))
    possible = False
    diff_answer = 9999999

    for k1 in range(low, high + 1):
        for k2 in range(low, high + 1):
            n_good, n_normal, n_bad, diff = classify_fruits(weight_list, k1, k2)
            if n_good >= low and n_normal >= low and n_bad >= low and n_good <= high and n_normal <= high and n_bad <= high:
                possible = True
                diff_answer = min(diff_answer, diff)

    if possible:
        print(f"#{_+1} {diff_answer}")
    else:
        print(f'#{_+1} -1')