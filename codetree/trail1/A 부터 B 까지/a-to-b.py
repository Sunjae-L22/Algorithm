A, B = map(int, input().split())
while A <= B:
    print(A, end = ' ')
    if A % 2 == 0:
        A += 3
    else:
        A *= 2

