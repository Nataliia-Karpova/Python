# Напишите по 5 преобразований из целых чисел в дробные,
# из дробных в целые, из каждого из этих типов в строку и
# наоборот (5 баллов)
# Из целого числа в дробь
n = 0
while n < 5:
    number1 = float(int(input('Введите целое число ')))
    print(number1)
    n += 1
# Из дроби в целое число
n = 0
while n < 5:
    number1 = int(float(input('Введите дробное число')))
    print(number1)
    n += 1
# Целое число в строку
n = 0
while n < 5:
    number1 = str(int(input('Введите целое число ')))
    print(number1)
    n += 1
# Дробное число в строку
n = 0
while n < 5:
    number1 = str(float(input('Введите дробное число ')))
    print(number1)
    n += 1
# Строку в целое число
n = 0
while n < 5:
    number1 = int(str(input('Введите строку для преобразования в целое число ')))
    print(number1)
    n += 1
# Строку в дробное число
n = 0
while n < 5:
    number1 = float(str(input('Введите строку для преобразования в дробное число ')))
    print(number1)
    n += 1
# Выберите 3 формулы (математические/физические, какие угодно) и имлементируйте их,
# приведите 3 примера вычисления с их помощью
# # Уравнение для расчета константы Михаэлиса - Ментен (3 подсчета)
n = 0
while n < 3:
    k = int(input('Константа скорости реакции распада фермент-субстратного комплекса на фермент и исходный субстрат '))
    k1 = int(input('Константа скорости реакции образования фермент-субстратного комплекса '))
    k2 = int(input('Константа скорости реакции распада фермент-субстратного комплекса на фермент и продукт '))
    km = (k + k2)/k1
    n += 1
    print(km)
# Подсчет средней оценки за 5 тестов
# Для 3-х посчетов нужно добавить цикл while как в предидущем коде
test1 = int(input('Оценка за тест 1 '))
test2 = int(input('Оценка за тест 2 '))
test3 = int(input('Оценка за тест 3 '))
test4 = int(input('Оценка за тест 4 '))
test5 = int(input('Оценка за тест 5 '))
mean = (test1 + test2 + test3 + test4 + test5) / 5
print(mean)
# Подсчет средней оценки за 5 тестов - причешем код
n = 0
summ = 0
while n < 5:
    test = int(input('Оценка за тест '))
    summ += test
    n += 1
mean = (summ / 5)
print(mean)
# Подсчет средней оценки за 5 тестов - причешем код исключив возможность неправильного ввода значения
n = 0
summ = 0
while n < 5:
    test = int(input('Введите оценку за тест от 1 до 5 '))
    if 0 < test <= 5:
        summ += test
        n += 1
    else:
        print('Некорректное число ')
mean = (summ / 5)
print('Средняя оценка', mean)
# Подсчет кол-ва деталей, выпускаемых на заводе за единицу времени на х станках
n = 0
while n < 3:
    x = int(input('Кол-во работающих станков '))
    t = int(input('Время работы станков (в часах) '))
    i = int(input('Производительность станков (кол-во деталей в час) '))
    details = t * i * x
    print(details)
    n +=1
# Выведите таблицы истинности для:
#Выводим таблицу истинности для a and b
a = int(input('Введите 0: '))
b = int(input('Введите 1: '))
print('a','b',' ', 'a and b')
print(a,a,'   ',a and a)
print(a,b,'   ',a and b)
print(b,a,'   ',b and a)
print(b,b,'   ',b and b)
#Выводим таблицу истинности для a or b
a = 0
b = 1
print('a','b',' ', 'a or b')
print(a,a,'   ',a or a)
print(a,b,'   ',a or b)
print(b,a,'   ',b or a)
print(b,b,'   ',b or b)
#Выводим таблицу истинности для 1 / 0
a = 0
b = 1
print('a',' ', 'not a/b')
print(a,'   ',int(not a))
print(b,'   ',int(not b))
#Выводим таблицу истинности для not
a = 0
b = 1
print('a',' ', 'not a/b')
print(a,'   ',not a)
print(b,'   ',not b)
#Выводим таблицу истинности для a nor b
a = 0
b = 1
print('a','b',' ', 'a nor b')
print(a,a,'   ',int(not(a or a)))
print(a,b,'   ',int(not(a or b)))
print(b,a,'   ',int(not(b or a)))
print(b,b,'   ',int(not(b or b)))
#Выводим таблицу истинности для a xor b
a = 0
b = 1
import operator
print('a','b',' ', 'a xor b')
print(a,a,'   ', operator.xor(a, a))
print(a,b,'   ', operator.xor(a, b))
print(b,a,'   ', operator.xor(b, a))
print(b,b,'   ', operator.xor(b, b))
#Выводим таблицу истинности для a nand b
a = 0
b = 1
print('a','b',' ', 'a nand b')
print(a,a,'   ',int(not(a and b)))
print(a,b,'   ',int(not(a and b)))
print(b,a,'   ',int(not(a and b)))
print(b,b,'   ',a and b)
# fizzbuzz - сделайте программу, на вход которой поступает целое число, если это число делится на 3 выводится fizz,
# Если на 5 - buzz, а если на 15 - fizzbuzz.
# Если не делится нацело ни на одно из них, выведите это же число
number = int(input('Введите целое число '))
if number % 15 == 0:
    print('fizzbuzz')
elif number % 3 == 0:
    print('fizz')
elif number % 5 == 0:
    print('buzz')
else:
    print(number)