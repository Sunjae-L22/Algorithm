N = int(input())
for i in range(N):
    line = ' ' * (N-1 - i) + '*' * ((i+1) * 2 - 1)
    print(line)
for i in range(N-2, -1, -1):
    line = ' ' * (N-1 - i) + '*' * ((i+1) * 2 - 1)
    print(line)