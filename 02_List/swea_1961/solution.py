import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())


def prettyprint(nlist):
    for n in nlist:
        print(n, end='')


for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    nums_90, nums_180, nums_270 = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            nums_90[row][col] = nums[N - 1 - col][row]
            nums_180[row][col] = nums[N - 1 - row][N - 1- col]
            nums_270[row][col] = nums[col][N-1-row]

    print(f"#{tc}")
    for row in range(N):
        prettyprint(nums_90[row])
        print(' ', end='')
        prettyprint(nums_180[row])
        print(' ', end='')
        prettyprint(nums_270[row])
        print()