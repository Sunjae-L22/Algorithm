import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    num_count = [0] * 10
    numbers = input()
    for number in numbers:
        num_count[int(number)] += 1

    max_n = 0
    max_number = -1
    for i in range(10):
        if num_count[i] >= max_n:
            max_n = num_count[i]
            max_number = i
    print(f"#{tc} {max_number} {max_n}")