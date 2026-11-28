N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for n in nums:
    if n == M:
        ans += 1

print(ans)