def total_age(**ages):
    sum = 0
    for age in ages:
        sum += ages[age]
    print(ages)
    print(sum)


total_age(age1=1, age2=20, age3=30)
