# Сделайте функцию, принимающую лист и возвращающую выпрямленный лист (исходный не должен был измениться):
flatten = ([1, [1, 2], 3, [[4, 5, [6]]]])
def straightened(flatten):
    return str(flatten).replace('[','').replace(']','')
print(straightened(([1, [1, 2], 3, [[4, 5, [6]]]])))


