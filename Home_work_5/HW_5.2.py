# Создайте пустой словарь, заполните его элементами, удалите часть элементов,
# обратитесь к нескольким элементам и сделайте с ними какое-нибудь действие
months = dict()
print(type(months))
months_2 = {}
print(type(months_2)) # Создаю пустой словарь

months["Dec"] = "winter"
months["Jan"] = "winter"
months["Feb"] = "winter"
months["March"] = "spring"
months["April"] = "spring"
months["May"] = "spring"
months["June"] = "summer"
months["July"] = "summer"
months["Aug"] = "summer"
months["Sep"] = "autumn"
months["Oct"] = "autumn"
months["Nov"] = "autumn"
print(months) # Добавила все месяцы в году

del months["Sep"]
del months["Oct"]
del months["Nov"]
print(months) # Удалила часть элементов

print("jan" in months)
print("jan" in months_2) # Проверка наличия ключа в словаре производится с помощью оператора in.

# Доступ к элементу словаря, осуществляется как же как доступ к элементу списка,
# только в качестве индекса указывается ключ.
print(months["May"])
print(months["April"])

months_3 = months.copy()
print(months_3) # Создала копию словаря

months_3 = months_3.clear()
print(months_3) # Очистила словарь

print(months.keys()) #Вернула ключи словаря

print(months.items()) #Вернула ключи словаря в отформатированном виде

# Если ключ  в словаре -  элемент удаляется из словаря и возвращается значение
# по этому ключу, иначе будет возвращено значение default (Можно указать свое значение).

print(months.pop("Feb"))

# Удаляет и возвращает пару (ключ, значение) из словаря.
# Если словарь пуст, то будет вызвано исключение KeyError.

print(months.popitem("Feb"))

months["Feb"] = months["Feb"].upper() # все буквы в Feb станут заглавными FEB