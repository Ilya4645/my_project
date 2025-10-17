print('Средний балл студентов')
students = {'Иван': [5, 4, 4, 5], 'Петр': [3, 2, 2, 4], 'Евгений': [5, 4, 3, 4]}
i = 0
sum = 0
kol = 0
for value in students.values():
    for i in range(len(value)):
        sum+=value[i]
        kol+=1
print('Средний балл =', sum/kol)
print('Количество букв в словаре')
str = input('Введите строку')
kol = {}
for el in str:
    if el == ' ':
        el1 = 'Пробел'
    else: el1 = el
    kol[el1] = str.count(el)
print(kol)
print('Создание словаря с квадратами ключей')
giv = {}
for i in range(1, 11):
    giv[i] = i**2
print(giv)
print('Создание словаря из 2-х значений')
keys = ['Имя', 'Возраст', 'Пол']
values = ['Елена', '18', 'Женский']
dictt = dict(zip(keys, values))
print(dictt)