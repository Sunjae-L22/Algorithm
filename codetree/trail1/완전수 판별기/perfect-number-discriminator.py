N = int(input())
sum = 0
for i in range(1, N):
    if N % i == 0:
        sum += i

if N == sum:
    print("P")
else:
    print("N")