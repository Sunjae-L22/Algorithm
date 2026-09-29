nums = list(map(int, input().split()))

for i, num in enumerate(nums):
    if num % 3 == 0:
        print(nums[i-1])
        break