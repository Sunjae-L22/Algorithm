nums = list(map(int, input().split()))
sum, cnt = 0, 0

for num in nums:
    if num == 0:
        break
    if num % 2 == 0:
        cnt += 1
        sum += num

print(cnt, sum)