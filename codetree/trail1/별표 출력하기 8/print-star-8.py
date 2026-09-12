N = int(input())
for i in range(1, N+1):
    if i % 2 == 1:
        print('*')
    else:
        print('* ' * i)