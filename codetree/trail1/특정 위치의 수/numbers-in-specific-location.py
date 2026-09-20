nums = list(map(int, input().split()))
sum = 0
for i in range(10):
    if i == 2 or i == 4 or i == 9:
        sum += nums[i]
    
print(sum)