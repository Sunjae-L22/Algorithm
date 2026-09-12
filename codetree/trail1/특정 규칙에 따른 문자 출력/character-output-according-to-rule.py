N = int(input())
for i in range(N-1, 0, -1):
    line = '  ' * i + '@ ' * (N-i)
    print(line)
print('@ ' * N)
for i in range(N-2, -1, -1):
    line = '@ ' * (i+1)
    print(line)