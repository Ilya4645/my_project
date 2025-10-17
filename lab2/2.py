import random
numbers = [random.randint(-50, 50) for _ in range(10)]
print('Все числа в списке:')
print(numbers)
print('Вывод четных элементов')
for i in range(0, len(numbers)):
    if i%2 == 0:
        print(numbers[i])
print('Максимальное и минимальное число')
max = 0
min = 100000
for i in range(0, len(numbers)):
    if numbers[i] < min:
        min = numbers[i]
    if numbers[i] > max:
        max = numbers[i]
print(min, max)
print('Сортировка произвольного списка')
for i in range(1, 6):
    n = int(input('Введите число n ='))
    numbers.append(n)
numbers.sort()
print(numbers)
print('Удаление дубликатов из списка')
i = 0
k = len(numbers)
while i<k:
    j = i+1
    while j<k:
        print(i, j)
        if numbers[i] == numbers[j]:
            print(numbers[j])
            del(numbers[j])
            k -= 1
        j += 1
    i += 1
print(numbers)
print('Замена местами 1 и последнего элемента')
numbers[0], numbers[len(numbers)-1] = numbers[len(numbers)-1], numbers[0]
print(numbers)