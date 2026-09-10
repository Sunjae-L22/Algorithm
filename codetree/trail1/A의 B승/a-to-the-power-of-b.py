A, B = map(int, input().split())
result = 1
for i in range(B):
    result *= A
print(result)