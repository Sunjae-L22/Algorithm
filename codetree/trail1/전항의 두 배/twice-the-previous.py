a, b = map(int, input().split())
print(a, b, end = ' ')
for i in range(8):
    a, b = b, b + 2 * a
    print(b, end = ' ')