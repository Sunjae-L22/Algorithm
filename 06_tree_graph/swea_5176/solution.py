import sys
sys.stdin = open("input.txt", "r")


def inorder(node):
    global cnt
    if node > N:
        return
    inorder(node * 2)        # 왼쪽
    cnt += 1
    tree[node] = cnt         # 현재 노드에 다음 숫자
    inorder(node * 2 + 1)    # 오른쪽


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 0
    inorder(1)
    print(f"#{tc} {tree[1]} {tree[N // 2]}")