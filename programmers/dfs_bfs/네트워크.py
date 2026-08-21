from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        q = deque([i])
        visited[i] = True
        while q:
            now = q.popleft()
            for col in range(n):
                if computers[now][col] == 1 and not visited[col]:
                    visited[col] = True
                    q.append(col)
        answer += 1
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))