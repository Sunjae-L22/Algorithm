import sys
from solution import init, oneYearLater

def run():
    n, m, k = map(int, input().split())
    mIceBlock = []
    for i in range(n):
        mIceBlock.append(list(map(int, input().split())))

    mIceGroup = []
    for i in range(m):
        mIceGroup.append(list(map(int, input().split())))

    init(n, m, mIceBlock, mIceGroup)

    okay = True

    for q in range(k):
        user_ans = oneYearLater()
        correctAns = list(map(int, input().split()))
        for y in range(n):
            for x in range(n):
                if user_ans.heights[y][x] != correctAns[y*n+x]:
                    okay = False


    return okay


#sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print("#%d %d" % (tc, score), flush = True)