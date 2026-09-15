A, B = map(int, input().split())
for i in range(2, 9, 2):
    for n in range(B, A-1, -1):
        if n == A:
            print(f"{n} * {i} = {n * i}")
        else:
            print(f"{n} * {i} = {n * i} /", end = ' ')