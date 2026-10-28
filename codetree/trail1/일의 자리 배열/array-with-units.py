a, b = map(int, input().split())
print(a, b, end = ' ')
for i in range(8):
    sum = a + b
    a = b
    b = sum % 10
    print(sum % 10, end = ' ')