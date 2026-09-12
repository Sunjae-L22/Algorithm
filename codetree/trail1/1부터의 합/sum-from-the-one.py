N = int(input())
adding = 1
sum = 0

while True:
    sum += adding
    if sum >= N:
        break
    adding += 1

print(adding)