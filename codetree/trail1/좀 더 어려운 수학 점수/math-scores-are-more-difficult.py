Amath, Aeng = map(int, input().split())
Bmath, Beng = map(int, input().split())

if Amath > Bmath:
    print("A")
elif Bmath > Amath:
    print("B")
else:
    if Aeng > Beng:
        print("A")
    else:
        print("B")