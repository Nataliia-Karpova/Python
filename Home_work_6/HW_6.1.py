# Сделайте функцию, принимающую лист и возвращающую выпрямленный лист (исходный не должен был измениться):
flatten = ([1, [1, 2], 3, [[4, 5, [6]]]])



def straightened(flatten):
    import copy
    straightened_sheet = copy.deepcopy(flatten)

