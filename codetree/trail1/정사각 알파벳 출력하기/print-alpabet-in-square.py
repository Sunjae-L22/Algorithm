N = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
for r in range(N):
    for c in range(N):
        print(alphabet[i], end = '')
        i += 1
    print()