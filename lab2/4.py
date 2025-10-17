print('Пересечение и объединение множеств')
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 5, 7, 9}
print('Объединение: ', set1 | set2)
print('Пересечение: ', set1 & set2)
print('Уникальные слова')
str = input('Введите текст')
words = str.split()
for word in words:
    if str.count(word) == 1:
        print(word)
    else:
        pass
print('Поиск общих элементов')
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 8, 'а']
sa = set(a)
sb = set(b)
print('Общие элементы', sa & sb)
print('Проверка подмножеств')
print(set1.issubset(set2))
print('Удаление элементов из множества, которые меньше заданного числа')
set3 = {1, 23, 54, 3, 2, 1, 53, 8, 9}
n = int(input('Введите число'))
for i in range(1, n):
    set3.discard(i)
print(set3)