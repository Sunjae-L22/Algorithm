scores = map(int, input().split())
group = [0] * 11
for score in scores:
    if score == 0:
        break
    group[(109 - score) // 10] += 1

for i in range(10):
    print(f"{100 - i * 10} - {group[i]}")
