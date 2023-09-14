def generator(n):
    value = 3
    print(1)
    while value < n:
        yield (value - 1) * (value - 2)
        value += 1


for value in generator(10):
    print(value)
