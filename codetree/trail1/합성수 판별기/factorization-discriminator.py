N = int(input())
flag = 'N'

for n in range(2, N):
    if N % n == 0:
        flag = 'C'

print(flag)