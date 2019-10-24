# Проитерируйтесь по заданному вами словарю и выведите его ключи и
# элементы (какой способ кажется вам лучшим?)

# Способ 1 с помощью встроенной функции items

months = {'Dec': 'winter', 'Jan': 'winter', 'Feb': 'winter', 'March': 'spring', 'April': 'spring', 'May': 'spring', 'June': 'summer', 'July': 'summer', 'Aug': 'summer', 'Sep': 'autumn', 'Oct': 'autumn', 'Nov': 'autumn'}
#Создаю новый словарь
print(months.items())

# Минус данного способа - результат в одной строке

# Чуть модифицируем с помощью цикла
months = {'Dec': 'winter', 'Jan': 'winter', 'Feb': 'winter', 'March': 'spring', 'April': 'spring', 'May': 'spring', 'June': 'summer', 'July': 'summer', 'Aug': 'summer', 'Sep': 'autumn', 'Oct': 'autumn', 'Nov': 'autumn'}
for month in months.items():
    print(month)
# Теперь красиво! + доступ к ключам и значениям одновременно. Получили кортежи


# Способ 2 с помощью цикла в котором мы сразу распаковываем кортежи

months = {'Dec': 'winter', 'Jan': 'winter', 'Feb': 'winter', 'March': 'spring', 'April': 'spring', 'May': 'spring', 'June': 'summer', 'July': 'summer', 'Aug': 'summer', 'Sep': 'autumn', 'Oct': 'autumn', 'Nov': 'autumn'}
for month in months:
    print(month, '->', months[month])

# Способ 3 Итерация через .keys()

months = {'Dec': 'winter', 'Jan': 'winter', 'Feb': 'winter', 'March': 'spring', 'April': 'spring', 'May': 'spring', 'June': 'summer', 'July': 'summer', 'Aug': 'summer', 'Sep': 'autumn', 'Oct': 'autumn', 'Nov': 'autumn'}
for month in months.keys():
    print(month, '->', months[month])


