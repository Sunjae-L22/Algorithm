n = int(input())
class_clean, aile_clean, bathroom_clean = 0, 0, 0
for i in range(1, n+1):
    if i % 12 == 0:
        bathroom_clean += 1
    elif i % 3 == 0:
        aile_clean += 1
    elif i % 2 == 0:
        class_clean += 1

print(class_clean, aile_clean, bathroom_clean)