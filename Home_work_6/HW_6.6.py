# Функцию, находящую самый частый элемент в списке, если их несколько, то все
moda([100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4])
(3, 45)
moda
# Способ 1
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


# Способ 2
import statistics
from statistics import mode


def most_common_number(moda):
    return (mode(moda))


moda = [100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4]
print(most_common_number(n))