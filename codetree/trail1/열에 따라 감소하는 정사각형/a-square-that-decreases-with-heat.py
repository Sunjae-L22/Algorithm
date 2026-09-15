N = int(input())
for i in range(N):
    line = ''
    for j in range(N, 0, -1):
        line += f'{j} '
    print(line)