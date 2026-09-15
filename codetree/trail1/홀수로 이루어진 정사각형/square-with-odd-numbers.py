N = int(input())
odds = []
odd = 11
for i in range(100):
    odds.append(odd)
    odd += 2
for r in range(N):
    for c in range(N):
        print(odds[r+c], end = ' ')
    print()
