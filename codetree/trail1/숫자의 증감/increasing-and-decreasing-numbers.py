C, N = input().split()
if C == 'A':
    for i in range(1, int(N)+1):
        print(i, end = ' ')
elif C == 'D':
    for i in range(int(N), 0, -1):
        print(i, end = ' ')