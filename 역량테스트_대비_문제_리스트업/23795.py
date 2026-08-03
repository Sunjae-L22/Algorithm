test_case = int(input())
for _ in range(test_case):
    N = int(input())
    # area = []
    # 구역 입력 받기(N * N)
    # for i in range(N):
    #     line = list(map(int, input().split()))
    #     area.append(line)

    area=[list(map(int,input().split())) for _ in range(N)]
    # 괴물 위치 찾기

    monster_x = 0
    monster_y = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] == 2:
                monster_y = i
                monster_x = j


    # 빈칸 중 광선이 닿는 곳은 -1로 바꾸기
    for i in range(4):
        wall = False
        x = monster_x
        y = monster_y
        # 상
        if i == 0:
            while (y >= 0 and wall == False):
                if area[y][x] == 1:
                    wall = True
                elif area[y][x] == 0:
                    area[y][x] = -1
                y -= 1

        # 하
        elif i == 1:
            while (y < N and wall == False):
                if area[y][x] == 1:
                    wall = True
                elif area[y][x] == 0:
                    area[y][x] = -1
                y += 1

        # 좌
        elif i == 2:
            while (x >= 0 and wall == False):
                if area[y][x] == 1:
                    wall = True
                elif area[y][x] == 0:
                    area[y][x] = -1
                x -= 1

        # 우
        elif i == 3:
            while (x < N and wall == False):
                if area[y][x] == 1:
                    wall = True
                elif area[y][x] == 0:
                    area[y][x] = -1
                x += 1

    # 0인 곳 세기
    answer = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] == 0:
                answer += 1

    print(f"#{_+1} {answer}")