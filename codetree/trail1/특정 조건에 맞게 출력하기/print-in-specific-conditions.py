nums = map(int, input().split())

for num in nums:
    if num == 0:
        break
    if num % 2 != 0:
        print(num + 3, end = ' ')
    else:
        print(num // 2, end = ' ')