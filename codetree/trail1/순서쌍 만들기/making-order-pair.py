N = int(input())
for i in range(N, 0, -1):
    line = ''
    for j in range(N, 0, -1):
        line += f'({i},{j}) '
    print(line)