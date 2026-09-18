N = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0

for r in range(N, 0, -1):
    blank = ' ' * (2 * (N - r))
    print(blank, end = '')
    for  c in range(r):
        print(alphabet[i], end = ' ')
        i += 1
        if i == 26:
            i = 0
    print()