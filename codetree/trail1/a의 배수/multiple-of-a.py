N, a = map(int, input().split())
for i in range(1, N+1):
    if i % a == 0:
        print(1)
    else:
        print(0)