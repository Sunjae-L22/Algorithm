A, B = map(int, input().split())
sum = 0
cnt = 0
for n in range(A, B+1):
    if n % 5 == 0 or n % 7 == 0:
        sum += n
        cnt += 1
print(f"{sum} {sum / cnt :.1f}")