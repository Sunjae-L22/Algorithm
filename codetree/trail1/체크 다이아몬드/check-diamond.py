N = int(input())

for i in range(N-1, -1, -1):
    line = ' ' * i + '* ' * (N-i)
    print(line)
for i in range(1, N):
    line = ' ' * i + '* ' * (N-i)
    print(line)