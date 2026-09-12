a, b, c = map(int, input().split())
flag = "YES"

for div in range(a, b+1):
    if div % c == 0:
        flag = "NO"
        break

print(flag)