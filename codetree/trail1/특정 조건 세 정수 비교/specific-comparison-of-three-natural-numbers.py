a, b, c = map(int, input().split())
if a <= b and a <= c:
    ans1 = 1
else:
    ans1 = 0

if a == b and a == c:
    ans2 = 1
else:
    ans2 = 0

print(ans1, ans2)