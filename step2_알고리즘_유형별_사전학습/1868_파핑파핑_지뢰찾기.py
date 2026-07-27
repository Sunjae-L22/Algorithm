T = int(input())
dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
from collections import deque


def is_zero(row, col):
    flag = True
    for dir in dirs:
        next_row = row + dir[0]
        next_col = col + dir[1]

        if 0 <= next_row < N and 0 <= next_col < N:
            if table[next_row][next_col] == '*':
                flag = False
                break
    return flag


for test_case in range(T):
    N = int(input())
    table = [[] for i in range(N)]
    is_opened_by_other = [[0] * N for i in range(N)]
    count = 0

    for i in range(N):
        table[i] = list(input())

    for row in range(N):
        for col in range(N):
            if table[row][col] == '.':
                if is_zero(row, col) and is_opened_by_other[row][col] == 0:
                    count += 1
                    is_opened_by_other[row][col] = 1

                    q = deque([(row, col)])          
                    while q:
                        r, c = q.popleft()
                        if not is_zero(r, c):        
                            continue
                        for dir in dirs:
                            next_row = r + dir[0]
                            next_col = c + dir[1]

                            if 0 <= next_row < N and 0 <= next_col < N:
                                if table[next_row][next_col] == '.' and is_opened_by_other[next_row][next_col] == 0:
                                    is_opened_by_other[next_row][next_col] = 1
                                    q.append((next_row, next_col))

    for row in range(N):
        for col in range(N):
            if table[row][col] == '.' and is_opened_by_other[row][col] == 0:
                count += 1                          

    print(f"#{test_case + 1} {count}")