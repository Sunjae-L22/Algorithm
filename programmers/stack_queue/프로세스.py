from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))   # (원래 위치, 우선순위)
    count = 0
    while q:
        cur = q.popleft()
        if any(cur[1] < p for _, p in q):
            q.append(cur)              # 더 높은 놈 있으면 뒤로
        else:
            count += 1                 # 실행
            if cur[0] == location:
                return count