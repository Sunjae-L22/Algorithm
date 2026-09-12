sum = 0
n = 0

while True:
    age = int(input())
    if 20 <= age < 30:
        sum += age
        n += 1
    else:
        break
print(f"{sum / n :.2f}")