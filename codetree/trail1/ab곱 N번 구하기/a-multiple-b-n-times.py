N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    mul = 1
    for j in range(a, b+1):
        mul *= j
    print(mul)