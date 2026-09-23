nums = list(map(int, input().split()))
odd_s, even_s = 0, 0

for i in range(len(nums)):
    if i % 2 == 0:
        odd_s += nums[i]
    else:
        even_s += nums[i]

print(abs(odd_s - even_s))