"""
Палиндромное число читается одинаково слева направо и справа налево. Наибольшее палиндромное число, полученное как произведение двух двузначных чисел, — это 9009 = 91 × 99.

Найдите наибольшее палиндромное число, полученное как произведение двух трёхзначных чисел.
"""

def is_number_polyndrom(number):
    signs = list(str(number))
    for index in range(len(signs) // 2 + 1):
        if signs[index-1] != signs[-index]:
            return False
    return True

def max_polyndrom():
    first = 999
    second = first
    current = 1
    max_pol = 1
    while second > 1:
        current = first * second
        if is_number_polyndrom(current):
            if current > max_pol:
                max_pol = current
        if first > 1:
            first -= 1
        else:
            second -= 1
            first = second
    return max_pol

print(max_polyndrom())