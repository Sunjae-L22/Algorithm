A, B = map(int, input().split())
if A < B:
    ans1 = 1
    ans2 = 0
elif A == B:
    ans1 = 0
    ans2 = 1
else:
    ans1 = 0
    ans2 = 0

print(ans1, ans2)