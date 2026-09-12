N = int(input())
for i in range(N):
    line = '  ' * i + '* ' * ((N-i) * 2 - 1)
    print(line)
for i in range(N-2, -1, -1):
    line = '  ' * i + '* ' * ((N-i) * 2 - 1)
    print(line)