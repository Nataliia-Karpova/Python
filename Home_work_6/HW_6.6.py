# Функцию, находящую самый частый элемент в списке, если их несколько, то все
from statistics import mode

moda = [100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4]
def most_frequent(moda):
    counter = 0
    most_freq = []
    for i in moda:
        number_frequency = moda.count(i)
        if number_frequency > counter:
            counter = number_frequency
            most_freq = most_freq.insert(i)
    return most_freq
print(most_frequent(moda))


