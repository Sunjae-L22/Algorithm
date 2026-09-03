age_1, sex_1 = input().split()
age_2, sex_2 = input().split()

if int(age_1) >= 19 and sex_1 == 'M':
    print(1)
elif int(age_2 ) >= 19 and sex_2 == 'M':
    print(1)
else:
    print(0)