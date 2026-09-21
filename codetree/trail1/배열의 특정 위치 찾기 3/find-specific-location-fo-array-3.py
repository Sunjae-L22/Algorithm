nums = list(map(int, input().split()))
index_0 = 0
for i in range(len(nums)):
    if nums[i] == 0:
        index_0 = i
        break
print(nums[i-1] + nums[i-2] + nums[i-3])