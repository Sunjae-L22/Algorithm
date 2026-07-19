from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    height_array = list(map(int, input().split()))
    answer = sum(height_array) - B
    comb = []
    for i in range(N):
        comb += list(combinations(height_array, i+1))
    
    
    for heights in comb:
        if sum(heights) >= B:
            answer = min(answer, sum(heights) - B)
    
    print(f"#{test_case} {answer}")