nums = list(map(int, input().split()))
sum, cnt = 0, 0

for num in nums:
    if num == 0:
        break
    sum += num
    cnt += 1

print(f"{sum} {(sum / cnt) :.1f}")