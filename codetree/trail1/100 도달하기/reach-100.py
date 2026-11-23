N = int(input())
num_1, num_2 = 1, N
print(num_1, num_2, end = ' ')
while num_2 <= 100:
    num_1, num_2 = num_2, num_2 + num_1
    print(num_2, end = ' ')