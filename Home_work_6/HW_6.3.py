# Напишите функцию, возвращающую максимум, который есть в списке чисел
maximum = ([100, 2, 3, 45, -2, 4])


def max_number(n):
    sorted_for_max = n.sort()
    return n[-1]


maximum_number = max_number(maximum)
print(maximum_number)
