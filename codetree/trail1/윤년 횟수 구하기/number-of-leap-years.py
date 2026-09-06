N = int(input())

def yoon(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

cnt = 0
for i in range(1, N+1):
    if yoon(i):
        cnt += 1
print(cnt)