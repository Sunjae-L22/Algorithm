# 0930 ~ 09:32

def solution(s):
    answer = True
    open = []
    for _ in s:
        if _ == '(':
            open.append(_)
        else:
            if len(open) == 0:
                answer = False
            else:
                open.pop()
    if len(open) > 0:
        answer = False

    return answer