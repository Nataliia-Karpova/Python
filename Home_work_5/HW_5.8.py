# Напишите реверскомплементатор (чем больше способов, тем лучше), на вход подаётся строка ДНК, нужно
# чтобы выводился реверскомплемент заглавными буквами

# Способ 1

DNA = input("Введите строку ДНК: ")
DNA1 = DNA[::-1]
DNA2 = DNA1.upper()
DNA3 = DNA2.replace('A', 'W')
DNA4 = DNA3.replace('G', 'X')
DNA5 = DNA4.replace('T', 'A')
DNA6 = DNA5.replace('C', 'G')
DNA7 = DNA6.replace('X', 'C')
DNA8 = DNA7.replace('W', 'T')
print(DNA8)

# Способ 2
DNA = str(input("Введите строку ДНК: "))
for i in range(n):
    DNA1 = DNA.upper()
    if i == 'A' or i == 'T':
        if i == 'A':
            DNA1 = DNA1.replace('A', 'T')
        else:
            DNA1 = DNA1.replace('T', 'A')
    elif i == 'G' or i == 'C':
        if i == 'G':
            DNA1 = DNA1.replace('G', 'C')
        else:
            DNA1 = DNA1.replace('C', 'G')
print(DNA1)



DNA = str(input("Введите строку ДНК: "))
DNA1 = DNA[::-1]
DNA1 = DNA1.upper()
n = len(DNA1)
for i in range(n):
    if i == 'A' or i == 'T':
        if i == 'A':
            DNA1 = DNA1.replace('A', 'T')
        else:
            DNA1 = DNA1.replace('T', 'A')
    elif i == 'G' or i == 'C':
        if i == 'G':
            DNA1 = DNA1.replace('G', 'C')
        else:
            DNA1 = DNA1.replace('C', 'G')
print(DNA1)





