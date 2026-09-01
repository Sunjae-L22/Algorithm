import sys

sys.stdin = open("sample_input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_n, min_n = numbers[0], numbers[0]

    for i in range(len(numbers)):
        if max_n < numbers[i]:
            max_n = numbers[i]
        if min_n > numbers[i]:
            min_n = numbers[i]

    print(f"#{tc} {max_n - min_n}")