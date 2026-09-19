start, end = map(int, input().split())

# Please write your code here.
def is_perfect(n):
    res = 0
    for div in range(1, n//2 + 1):
        if n % div == 0:
            res += div
    if res == n:
        return True
    return False

perfect_cnt = 0
for i in range(start, end+1):
    if is_perfect(i):
        perfect_cnt += 1

print(perfect_cnt)