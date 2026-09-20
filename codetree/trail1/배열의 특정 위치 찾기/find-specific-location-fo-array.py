nums = list(map(int, input().split()))
sum1, sum2 = 0, 0
cnt2 = 0
for i in range(10):
    if i % 2 == 1:
        sum1 += nums[i]
    if i % 3 == 2:
        sum2 += nums[i]
        cnt2 += 1

print(f"{sum1} {sum2 / cnt2 :.1f}")