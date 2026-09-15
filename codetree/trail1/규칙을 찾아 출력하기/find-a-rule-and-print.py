N = int(input())
for i in range(N):
    if i == 0 or i == N:
        line = '* ' * N
    else:
        line = '* ' * i + '  ' * (N-1-i) + '*'
    print(line)