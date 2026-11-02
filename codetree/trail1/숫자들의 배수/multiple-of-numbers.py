N = int(input())
cnt = 0
mul = 1

while True:
    print(N * mul, end = ' ')
    if (N * mul) % 5 == 0:
        cnt += 1
    if cnt == 2:
        break
    mul += 1
