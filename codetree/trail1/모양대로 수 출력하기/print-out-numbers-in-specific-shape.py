N = int(input())
for i in range(N):
    line = '  ' * i
    print(line, end = '')
    for j in range(N-i, 0, -1):
        print(j, end = ' ')
    print()