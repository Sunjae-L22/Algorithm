N = int(input())
dividing = 1

while True:
    N //= dividing
    if N <= 1:
        break
    dividing += 1

print(dividing)