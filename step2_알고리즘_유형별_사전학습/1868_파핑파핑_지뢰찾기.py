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
                    table[row][col] = '0'
                    count += 1
                    for dir in dirs:
                            next_row = row + dir[0]
                            next_col = col + dir[1]
                    
                            if 0 <= next_row < N and 0 <= next_col < N:
                                is_opened_by_other[next_row][next_col] = 1
                               

    q = deque()
    for row in range(N):
        for col in range(N):
            if is_opened_by_other[row][col] == 1:
                q.append((row, col))    

    while q:
        row, col = q.popleft()
        if is_zero(row, col):
            table[row][col] = '0'
            for dir in dirs:
                next_row = row + dir[0]
                next_col = col + dir[1]

                if 0 <= next_row < N and 0 <= next_col < N:
                    is_opened_by_other[next_row][next_col] = 1
                    if is_opened_by_other[next_row][next_col] == 1 and table[next_row][next_col] == '.':
                        q.append((next_row, next_col))
        else:
            table[row][col] = '1'


    for row in range(N):
        for col in range(N):
            if table[row][col] == '.':
                count += 1

    print(f"#{test_case + 1} {count}")




