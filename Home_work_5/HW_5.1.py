# Создайте пустой сэт, добавьте к нему несколько элементов разных типов, а также проведите сэтовые операции над парой сэтов:
# объединение
# пересечение
# вычитание
# симметричное вычитание
# проверку на вхождение одного сэта в другой

my_set_1 = set()
my_set_2 = set() #Создаю пустые сеты
my_set_1.add("Sun")
my_set_1.add(2)
my_set_1.add(9.1)
my_set_2.add("moon")
my_set_2.add(8)
my_set_2.add(True) #Добавляю элементы в словари
print(my_set_1)
print(my_set_2)
summ_set = my_set_1.union(my_set_2) # объединение
print(summ_set)
crossing = my_set_1.intersection(my_set_2)
print(crossing) # пересечение
print(my_set_1 & my_set_2) # А можно так!
# Нет общих элементов - добавим, чтобы проверить как работает пересечение
my_set_1.add(4)
my_set_2.add(4)
print(my_set_1 & my_set_2)
diff_set = my_set_1.difference((my_set_2))
print(diff_set) # вычитание
both_diff_set = my_set_1.symmetric_difference(my_set_2)
print(both_diff_set) # симметричное вычитание
daughter_sub_set = my_set_1.issubset(my_set_2)
print(daughter_sub_set)
daughter_super_set = my_set_1.issuperset(my_set_2)
print(daughter_super_set) # проверка на вхождение одного сэта в другой

