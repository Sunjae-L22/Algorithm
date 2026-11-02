N = int(input())
nums = map(int, input().split())
for num in nums:
    if num % 2 == 0:
        print(num, end = ' ')