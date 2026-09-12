N = int(input())
for i in range(N):
    if i % 2 == 0:
        print('* ' * (N - (i // 2)))
    else:
        print('* ' * (i // 2 + 1))
for i in range(N-1, -1, -1):
    if i % 2 == 0:
        print('* ' * (N - (i // 2)))
    else:
        print('* ' * (i // 2 + 1))