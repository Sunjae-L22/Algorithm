action, temp = [], []
for i in range(3):
    a, b = input().split()
    action.append(a)
    temp.append(int(b))

# A, B, C, D grade array
grade = [0] * 4

for i in range(3):
    if action[i] == 'Y':
        if temp[i] >= 37:
            grade[0] += 1
        else:
            grade[2] += 1
    else:
        if temp[i] >= 37:
            grade[1] += 1
        else:
            grade[3] += 1
            
flag = "normal"
if grade[0] >= 2:
    flag = "emergency"

for cnt in grade:
    print(cnt, end = ' ')

if flag == "emergency":
    print("E")