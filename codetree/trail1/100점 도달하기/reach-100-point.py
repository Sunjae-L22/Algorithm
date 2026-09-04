N = int(input())
def grade(n):
    if n >= 90:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 70:
        return 'C'
    elif n >= 60:
        return 'D'
    else:
        return 'F'

for i in range(N, 101):
    print(grade(i), end = ' ')