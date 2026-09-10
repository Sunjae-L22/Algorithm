N = int(input())
for i in range(N+1):
    if i % 2 == 0 or i % 10 == 5:
        continue
    if i % 3 == 0 and i % 9 != 0:
        continue
    print(i, end = ' ')