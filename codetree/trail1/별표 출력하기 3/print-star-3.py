N = int(input())

for i in range(N):
    line = '  ' * i +  '* ' * ((N-i) * 2 - 1)
    print(line)