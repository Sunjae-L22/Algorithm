from collections import defaultdict, Counter

# clothes = [["yellow_hat", "headgear"], 
#            ["blue_sunglasses", "eyewear"], 
#            ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    count = []
    for cloth in clothes:
        count.append(cloth[1])
    counts = Counter(count)
    answer = 1

    # 모든 조합 - (하나도 안 입는 경우 1가지)
    for n in counts.values():
        answer *= (n+1)

    return answer - 1


print(solution(clothes))