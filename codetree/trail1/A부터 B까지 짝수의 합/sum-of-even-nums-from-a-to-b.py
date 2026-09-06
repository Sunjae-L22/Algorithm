A, B = map(int, input().split())
sum = 0
for n in range(A, B+1):
    if n % 2 == 0:
        sum += n
print(sum)