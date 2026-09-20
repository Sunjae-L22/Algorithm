N = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
for r in range(1, N+1):
    for c in range(r):
        print(alphabet[i], end = '')
        i += 1
        if i == 26:
            i = 0
    print()