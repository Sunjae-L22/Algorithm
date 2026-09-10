A, B = map(int, input().split())
result = 1
for i in range(1, B+1):
    if i % A == 0:
        result *= i
print(result)