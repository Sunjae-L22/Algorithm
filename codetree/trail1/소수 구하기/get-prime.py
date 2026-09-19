N = int(input())

def is_prime(n):
    flag = True

    for div in range(2, n//2 + 1):
        if n % div == 0:
            flag = False
    
    if flag:
        return True
    return False

for i in range(2, N+1):
    if is_prime(i):
        print(i, end = ' ')