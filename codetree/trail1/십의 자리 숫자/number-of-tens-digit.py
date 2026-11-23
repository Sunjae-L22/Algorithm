nums = map(int, input().split())
ten_digit = [0] * 10
for num in nums:
    if num == 0:
        break
    ten_digit[(num % 100) // 10] += 1

for i in range(1, 10):
    print(f"{i} - {ten_digit[i]}")