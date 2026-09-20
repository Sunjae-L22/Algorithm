nums = list(map(int, input().split()))
length = len(nums)
new_nums = []
for num in nums:
    if num == 0:
        break
    new_nums.append(num)

for i in range(len(new_nums)-1, -1, -1):
    print(new_nums[i], end = ' ')