def solution(arr):
    answer = [arr[0]]
    last = arr[0]
    for num in arr:
        if num == last:
            continue
        last = num
        answer.append(num)
    return answer