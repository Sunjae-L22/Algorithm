import sys
sys.stdin = open("input.txt", "r")

# 상, 좌, 우
dr, dc = [-1, 0, 0], [0, -1, 1]

for test_case in range(1, 11):
    tc = int(input())
    ladder = []
    for i in range(100):
        line = list(map(int, input().split()))
        ladder.append(line)
        # 도착지점 찾기
        if i == 99:
            end = (99, line.index(2))

    # 도착지점부터 올라갈건데, 처음 한번은 무조건 올라가고 시작
    row, col = end[0], end[1]
    # 이전 이동방향 -> 좌/우로 이동중이었다면 좌/우 그대로 가거나 길이 없을 때 위로 꺾어야함(1/2/3)
    prev_dir = 1
    while row > 0:
        if prev_dir == 1:
            # 위로 이동중이었다면, 왼쪽/오른쪽에 길이 있나 확인부터 합시다.
            if 0 <= (col - 1) and ladder[row][col-1] == 1:
                col -= 1
                prev_dir = 2
                continue
            elif (col + 1) < 100 and ladder[row][col+1] == 1:
                col += 1
                prev_dir = 3
                continue
            else: # 왼쪽 / 오른쪽에 길이 없다면 위로 한칸 올라가
                row -= 1
                continue
        elif prev_dir == 2: # 좌로 이동중이였다면
            if 0 <= (col - 1) and ladder[row][col-1] == 1:
                col -= 1
                prev_dir = 2
                continue
            else:
                row -= 1
                prev_dir = 1
                continue
        else: # 우로 이동중이였다면
            if (col + 1) < 100 and ladder[row][col+1] == 1:
                col += 1
                prev_dir = 3
                continue
            else:
                row -= 1
                prev_dir = 1
                continue

    print(f"#{test_case} {col}")