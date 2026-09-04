import sys
sys.stdin = open("input.txt", "r")

op = ['/', '*', '+', '-']


def calc(i):
    if isinstance(nodes[i], int):
        return nodes[i]
    else:
        l, r = calc(nodes[i][1]), calc(nodes[i][2])
        if nodes[i][0] == '/':
            return l / r
        elif nodes[i][0] == '*':
            return l * r
        elif nodes[i][0] == '+':
            return l + r
        else:
            return l - r


for tc in range(1, 11):
    N = int(input())
    nodes = [0] * (N+1)
    for i in range(1, N+1):
        inputs = input().split()
        if inputs[1] in op:
            nodes[i] = (inputs[1], int(inputs[2]), int(inputs[3]))
        else:
            nodes[i] = int(inputs[1])
    print(f"#{tc} {int(calc(1))}")