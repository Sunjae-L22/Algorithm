start, end = map(int, input().split())

# Please write your code here.
def division_n(n):
    cnt = 0
    for div in range(1, n+1):
        if n % div == 0:
            cnt += 1
    if cnt == 3:
        return True
    return False

ans = 0

for i in range(start, end+1):
    if division_n(i):
        ans += 1

print(ans)