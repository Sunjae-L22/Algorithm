A, B = map(int, input().split())
for i in range(1, 10):
    for n in range(B, A-1, -2):
        if n == A:
            print(f"{n} * {i} = {n * i}")
        else:
            print(f"{n} * {i} = {n * i} /", end = ' ')