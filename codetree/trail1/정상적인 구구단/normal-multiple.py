N = int(input())
for r in range(1, N+1):
    for c in range(1, N+1):
        if c == N:
            print(f"{r} * {c} = {r * c}")    
        else:
            print(f"{r} * {c} = {r * c},", end = ' ')