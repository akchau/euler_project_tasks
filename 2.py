"""
Каждый новый член последовательности Фибоначчи получается путём сложения двух предыдущих членов. Начиная с 1 и 2, первые 10 членов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Рассмотрев члены последовательности Фибоначчи, значения которых не превышают четыре миллиона, найдите сумму чётных членов.

"""

def task():
    fib_num_sum = 0
    last_fib_num = 1
    fib_num = 1
    while fib_num < 4000000:
        temp_stor = fib_num
        fib_num = fib_num + last_fib_num
        last_fib_num = temp_stor
        if fib_num % 2 == 0:
            fib_num_sum += fib_num
    return fib_num_sum


print(task())