remain = 3
while True:
    n = int(input())
    if n % 2:
        continue
    else:
        print(n // 2)
        remain -= 1
        if remain == 0:
            break
