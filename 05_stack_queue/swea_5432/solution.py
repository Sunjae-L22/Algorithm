import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    line = input()
    length = len(line)

    lazers = []
    # 파이프가 되기 위해 준비하는 애들
    pipe_stack = []
    pipes = []
    index = 0
    answer = 0
    
    # input을 돌면서 레이저 위치 넣기
    for i in range(length):
        if line[i] == '(':
            if line[i+1] == ')':
                lazers.append(index)
                index += 1
                # 만들어지고 있는 파이프들이 조각남! 
                answer += len(pipe_stack)
            elif line[i+1] == '(':
                pipe_stack.append(index)
                index += 1
        elif line[i] == ')':
            # 전이 ( 이면 무조건 레이저가 만들어지므로 이미 확인한 경우. 
            if line[i-1] == '(':
                pass
            elif line[i-1] == ')':
                tmp = pipe_stack.pop()
                pipes.append((tmp, index))
                index += 1

    # 기본으로 파이프들은 1조각에서 시작하므로 파이프 개수를 더해줌
    answer += len(pipes)

    
    # 다 만들고 나서 조각 확인하니까 시간초과 남 -> 파이프를 만들 때 스택에 쌓여있는 파이프(만들고있는중) * 레이저를 해주면 되지 않을까...
    # for pipe in pipes:
    #     # 각 파이프 조각
    #     piece = 1
    #     for lazer in lazers:
    #         if pipe[0] < lazer < pipe[1]:
    #             piece += 1
    #         elif lazer > pipe[1]:
    #             break
    #     answer += piece

    print(f"#{test_case} {answer}")