N = int(input())
for i in range(N):
    line = '  ' * (N-1 - i) + '* ' * (i * 2 + 1)
    print(line)