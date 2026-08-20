from itertools import product

def solution(numbers, target):
    answer = 0
    arr = [-1, 1]
    m = len(numbers)
    perms = list(product(arr, repeat = m))

    for perm in perms:
        tmp_sum = 0
        for i in range(m):
            tmp_sum += perm[i] * numbers[i]
        if tmp_sum == target:
            answer += 1

    return answer

print(solution([4, 1, 2, 1], 2))