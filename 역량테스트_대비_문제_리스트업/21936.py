T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    target = input()
    answer = "NONE"
     
    for i in range(N-M+1):
        if target[i] == target[i+M-1]:
            answer = target[i : i+M]
    print(f"#{test_case} {answer}")
                                    