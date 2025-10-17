import random
numbers = [random.randint(-50, 50) for _ in range(20)]
print('Уникальные значения из словаря')
print(numbers)
for numb in numbers:
    if numbers.count(numb) == 1:
        print(numb)
    else:
        pass
print('Словарь')
st = input('Введите строку')
st = st.split()
res = {}
i = 0
for i in range(len(st)):
    if st[i] in res:
        res[st[i]] += 1
    else:
        res[st[i]] = 1
print(res)
print('Словарь из слов длиннее 5 символов')
st = input('Введите строку')
st = st.split()
res = {}
stwr = {word for word in st if len(word) > 5}
print(stwr)
print('Количество вхождений слова в словаре')
st = input('Введите предложение')
st = st.split()
res = {}
i = 0
for i in range(len(st)):
    if st[i] in res:
        res[st[i]] += 1
    else:
        res[st[i]] = 1
print(res)
print('Создание списка чисел, преобразование в множество и обратно без дубликатов')
st = input('Введите числа')
st = st.split()
i = 0
for i in range(len(st)):
    st[i] = int(st[i])
st = set(st)
st = list(st)
print(st)
print('Самый дорогой товар')
tov = {'Апельсин': 40, 'Банан': 20, 'Груша': 60, 'Дыня': 30}
print(tov)
sort_tov = sorted(tov.items(), key=lambda item: item[1], reverse=True)
print('Самый дорогой товар:', sort_tov[0][0])
print('Имена')
st = input('Введите имена')
st = st.split()
res = {}
for i in range(len(st)):
    if st[i] in res:
        res[st[i]] += 1
    else:
        res[st[i]] = 1
sort_st = sorted(res.items(), key=lambda item: item[1], reverse=True)
print('Имена, встречающиеся более 1 раза:')
for i in range(len(sort_st)):
    if sort_st[i][1] > 1:
        print(sort_st[i][0])
print('Имя, встречающееся чаще всего', sort_st[0][0])
print('Словарь с значениями индексов')
st = input('Введите строку')
res = {}
for i in range(len(st)):
    if st[i] not in res:
        res[st[i]] = i
print(res)
