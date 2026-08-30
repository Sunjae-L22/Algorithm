from collections import Counter

def solution(nums):
    answer = 0
    poketmon_count = Counter(nums)
    N = len(nums)

    if len(poketmon_count) >= N//2:
        answer = N//2
    else:
        answer = len(poketmon_count)

    return answer

nums = [3, 3, 3, 2, 2, 4]
print(solution(nums))