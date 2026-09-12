N = int(input())
x = 0
while True:
    N //= 2
    x += 1
    if N == 1:
        break

print(x)