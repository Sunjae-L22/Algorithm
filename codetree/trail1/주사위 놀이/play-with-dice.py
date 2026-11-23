nums = map(int, input().split())
dice = [0] * 7

for num in nums:
    dice[num] += 1

for i in range(1, 7):
    print(f"{i} - {dice[i]}")