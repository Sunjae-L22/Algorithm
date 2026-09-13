N = int(input())
for i in range(2*N + 1):
    if i % 2 == 0:
        line = '* ' * (2*N + 1)
    else:
        line = '*   ' * (N + 1)
    print(line)