import sys

DIRECTIONS = [(0, 1), (1, 0)] # 우 하

sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0 # 조건에 맞는 개수, 최종 답
    for r in range(n):
        for c in range(n): # (r, c) 탐색 시작점
            if puzzle[r][c]: # 1일때 탐색 시작 -> 근데 중간에서 시작하면 안됨
                for dr, dc in DIRECTIONS:
                    # print(dr, dc, " 방향으로 이동")
                    ir, ic = r - dr, r - dc # 지금 점 바로 직전이 상자 밖 or 값이 0
                    if ir == -1 or ic == -1 or not puzzle[ir][ic]: # 인덱스 에러가 나지 않을까,..,..?
                        # print(r, c, " 시작점 확정")

                        len_word = 1 # 단어 길이, 임시 변수
                        nr, nc = r + dr, c + dc
                        while 0 <= nr < n and 0 <= nc < n: # 해당 방향 끝까지 탐색
                            # print(nr, nc, " 탐색중")
                            if not puzzle[nr][nc]: # (r, c)가 0이면 다음 방향 탐색으로 넘어감
                                break
                            len_word += 1 # 위 조건 해당 안하면 단어 길이 + 1
                            # print(len_word)
                            nr += dr
                            nc += dc

                        if len_word == k: # 끝까지 돌고 나왔을 때 단어 길이가 k -> 정답 개수 + 1
                            cnt += 1
                            # print(len_word)

    print(f'#{tc} {cnt}')