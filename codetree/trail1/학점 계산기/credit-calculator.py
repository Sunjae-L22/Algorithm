N = int(input())
grades = map(float, input().split())
mean = sum(grades) / N
print(f"{mean :.1f}")
if mean >= 4:
    print("Perfect")
elif mean >= 3:
    print("Good")
else:
    print("Poor")