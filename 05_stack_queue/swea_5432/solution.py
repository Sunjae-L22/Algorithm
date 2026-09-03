import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    line = input()

    lazer = []
    
    # input을 돌면서 레이저 위치 넣기
    for _ in line:
