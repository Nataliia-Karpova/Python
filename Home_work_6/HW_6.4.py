# Функцию, возвращающую список в обратном порядке
reverse_l = [100, 2, 3, 45, -2, 4]

def reverse_list(n):
    reverse_list_return = n[::-1]
    return(reverse_list_return)
n = reverse_l
print(reverse_list(reverse_l))