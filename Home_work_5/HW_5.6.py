# Сконвертируйте список, кортеж, сэт и строку друг в друга всеми возможными способами
# (строка -> лист, строка -> кортеж, ...)

# Из строки в лист, кортеж и set

For_convertation = input("Введите строку для преобразования в лист: ")
print(list(For_convertation))

For_convertation = input("Введите строку для преобразования в кортеж: ")
print(tuple(For_convertation))

For_convertation = input("Введите строку для преобразования в set: ")
print(set(For_convertation))

# Из листа в строку, кортеж и set

For_convertation = list(input("Введите лист для преобразования в строку: "))
print(str(For_convertation))

For_convertation = list(input("Введите лист для преобразования в кортеж:"))
print(tuple(For_convertation))

For_convertation = list(input("Введите лист для преобразования в set:"))
print(set(For_convertation))

# Из кортежа в строку, лист и set

For_convertation = tuple(input("Введите кортеж для преобразования в строку:"))
print(str(For_convertation))

For_convertation = tuple(input("Введите кортеж для преобразования в лист:"))
print(list(For_convertation))

For_convertation = tuple(input("Введите кортеж для преобразования в set:"))
print(set(For_convertation))

# Из set в строку, лист и кортеж

For_convertation = set(input("Введите set для преобразования в строку:"))
print(str(For_convertation))

For_convertation = set(input("Введите set для преобразования в лист:"))
print(list(For_convertation))

For_convertation = set(input("Введите set для преобразования в кортеж:"))
print(tuple(For_convertation))
