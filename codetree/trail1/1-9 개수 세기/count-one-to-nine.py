N = int(input())
nums = map(int, input().split())

count_num = [0] * 10
for num in nums:
    count_num[num] += 1

for i in range(1, 10):
    print(count_num[i])