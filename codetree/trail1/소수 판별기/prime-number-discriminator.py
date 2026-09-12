N = int(input())
prime = 'P'

for i in range(2, N//2):
    if N % i == 0:
        prime = 'C'
        break

print(prime)