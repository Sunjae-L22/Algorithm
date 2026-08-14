from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = "No"
    question = list(map(int, input().split()))
    perm_list = list(permutations(range(1, N+1), len(question)))

    if tuple(question) in perm_list:
        answer = "Yes"

    print(f"#{tc} {answer}")