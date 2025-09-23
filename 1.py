""" Найдите сумму всех натуральных чисел меньше 1000, которые кратны 3 или 5. """


def task():
    sum([number for number in range(1000) if number % 3 == 0 or number % 5 == 0])

print(task())