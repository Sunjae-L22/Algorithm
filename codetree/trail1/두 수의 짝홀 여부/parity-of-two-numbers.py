a, b = map(int, input().split())

def check(n):
    if n % 2:
        print("odd")
    else:
        print("even")

check(a)
check(b)