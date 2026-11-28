# 2493 탑 [골드 5]

from collections import deque

N = int(input())
heights = list(map(int, input().split()))
answer = [0] * N

# 내 신호를 받아줄 탑을 기다리는 애들
waiting_top = deque()

# 오른쪽에서부터 거꾸로 봐보기
for i in range(N-1, -1, -1):
    while waiting_top and heights[waiting_top[-1]] < heights[i]:
        j = waiting_top.pop()
        answer[j] = i + 1

    waiting_top.append(i)

for n in answer:
    print(n, end = ' ')