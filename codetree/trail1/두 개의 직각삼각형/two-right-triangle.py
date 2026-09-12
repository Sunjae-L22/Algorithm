N = int(input())
for i in range(N):
    line = '*' * (N-i) + ' ' * 2 * i + '*' * (N-i)
    print(line)