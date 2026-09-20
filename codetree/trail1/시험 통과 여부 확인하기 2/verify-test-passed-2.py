N = int(input())
cnt = 0
for i in range(N):
    scores = list(map(int, input().split()))
    mean = sum(scores) / 4
    if mean >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)