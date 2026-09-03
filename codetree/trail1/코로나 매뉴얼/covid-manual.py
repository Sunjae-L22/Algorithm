count = 0
for i in range(3):
    gamgi, temp = input().split()
    if gamgi == 'Y' and int(temp) >= 37:
        count +=1 

if count >= 2:
    print('E')
else:
    print('N')