N = int(input())
for i in range(2 * N):
    if i % 2 == 1:
        print('* ' * (N - (i - 1) // 2))
    else:
        print('* ' * (1 + (i // 2)))