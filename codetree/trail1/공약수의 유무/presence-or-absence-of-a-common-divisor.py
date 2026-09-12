A, B = map(int, input().split())
flag = 0

for div in range(A, B+1):
    if 1920 % div == 0 and 2880 % div == 0:
        flag = 1
        break

print(flag)