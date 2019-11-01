# Функцию, вычисляющую среднее списка
meaning_mean([100, 2, 3, 45, -2, 4])

def meaning_mean(n):
    summ_numbers = 0
    counter = 0
    for i in n:
        summ_numbers += i
        counter +=1
    final_mean = summ_numbers / counter
    return(final_mean)

print(meaning_mean([100, 2, 3, 45, -2, 4]))


