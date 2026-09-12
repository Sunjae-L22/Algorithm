students = {1 : "John", 2 : "Tom", 3 : "Paul", 4 : "Sam"}

while True:
    n = int(input())
    if 1 <= n <= 4:
        print(students[n])
    else:
        print("Vacancy")
        break