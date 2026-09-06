A, B = map(int, input().split())
a = min(A, B)
b = max(A, B)
sum = 0

for n in range(a, b+1):
    if n % 5 == 0:
        sum += n

print(sum)