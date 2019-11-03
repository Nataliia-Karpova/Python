# Функцию, берущую указанный элемент из коллекции
get([1, 2, 15, 36], 2)
15
get((1, 2, 15, 36), -1)
36
get({1: 2, 'kva': 36}, 'kva')
36

num = ([1, 2, 15, 36], 2)
num = ({1: 2, 'kva': 36}, 'kva')
def finding(n):
    list_1 = n[0]
    ind = n[-1]
    if n == dict:
        if ind in list_1:
            print(n.setdefault(int))
    else:
            print(ind)
print(finding(num))



