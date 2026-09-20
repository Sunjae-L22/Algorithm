N = int(input())
nums = list(map(int, input().split()))
for i in range(len(nums)-1, -1, -1):
    if nums[i] % 2 == 0:
        print(nums[i], end = ' ')