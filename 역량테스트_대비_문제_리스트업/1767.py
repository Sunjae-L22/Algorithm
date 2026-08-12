T = int(input())


# core_locations 리스트를 받아서 각 코어가 전선을 뻗을 수 있는 방향 반환하는 함수
def core_to_line(N, maxinos, core_locations):
    line_dirs = []

    for core_location in core_locations:
        row = core_location[0]
        col = core_location[1]
        tmp_dir = []

        for i in range(4):
            # 상 방향에 1이나 -1이 없는지 확인
            flag = False
            if i == 0:
                for r in range(0, row):
                    if maxinos[r][col] in (1, -1):
                        flag = True
            elif i == 1:
                for r in range(row+1, N):
                    if maxinos[r][col] in (1, -1):
                        flag = True
            elif i == 2:
                for c in range(0, col):
                    if maxinos[row][c] in (1, -1):
                        flag = True
            else:
                for c in range(col+1, N):
                    if maxinos[row][c] in (1, -1):
                        flag = True

            if flag == False:
                tmp_dir.append(i)

        line_dirs.append(tmp_dir)
    return line_dirs


def line_to_comb(line_dirs):
    l = len(line_dirs)
    total = 1
    for i in range(l):
        total *= len(line_dirs[i])

    iters = [total] * l
    tmp_total = total
    for i in range(l):
        tmp_total = int(tmp_total / len(line_dirs[i]))
        iters[i] = tmp_total

    possible_lines = [[] for _ in range(total)]
    for idx in range(total):
        for i in range(l):
            d = (idx // iters[i]) % len(line_dirs[i])
            possible_lines[idx].append(line_dirs[i][d])

    return possible_lines



for test_case in range(1, T+1):
    N = int(input())
    maxinos = []

    for i in range(N):
        maxinos.append(list(map(int, input().split())))

    # 가장자리에 붙어있는 코어는 벽(2로 작성)으로 취급해버리기
    for row in range(N):
        for col in range(N):
            if (maxinos[row][col] == 1) and (row == 0 or row == N-1 or col == 0 or col == N-1):
                maxinos[row][col] = -1

    # 코어 위치 기록(벽으로 변환한거 빼고)
    core_locations = []
    for row in range(N):
        for col in range(N):
            if maxinos[row][col] == 1:
                core_locations.append([row, col])

    line_dirs = core_to_line(N, maxinos, core_locations)
    possible_lines = line_to_comb(line_dirs)

    # possible lines를 돌면서, 선을 다 그었을 때 겹치는 부분(2 or bigger)이 생기면 -해주자. 
    