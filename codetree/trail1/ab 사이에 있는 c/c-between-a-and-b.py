a, b, c = map(int, input().split())
flag = False

for n in range(a, b+1):
    if n % c == 0:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")