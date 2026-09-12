N = int(input())
mul = 1
multiplying = 1

while True:
    mul *= multiplying
    if mul >= N:
        break
    multiplying += 1

print(multiplying)