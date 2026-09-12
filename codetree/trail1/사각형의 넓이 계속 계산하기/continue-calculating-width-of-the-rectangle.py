while True:
    w, h, str = input().split()
    w, h = int(w), int(h)
    print(w * h)
    if str == 'C':
        break