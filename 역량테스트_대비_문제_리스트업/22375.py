T = int(input())
 
def toggle(switch, start):
    for i in range(start, len(switch)):
        if switch[i] == 0:
            switch[i] = 1
        else:
            switch[i] = 0
             
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
     
    answer = 0
     
    for i in range(N):
        if Ai[i] != Bi[i]:
            toggle(Ai, i)
            answer += 1
        if Ai == Bi:
            break
    print(f"#{test_case} {answer}")