is3, is5 = 0, 0
for i in range(10):
    n = int(input())
    if n % 3 == 0:
        is3 += 1
    if n % 5 == 0:
        is5 += 1
print(is3, is5)