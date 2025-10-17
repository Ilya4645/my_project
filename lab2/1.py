print('Таблица умножения от 1 до 9')
for i in range(1, 10):
    print('Таблица умножения на', i)
    for j in range(1, 11):
        print(i, '*', j, '=', i*j)
print('Сумма нечетных чисел от 1 до 100')
sum = 0
for i in range(1, 101):
    if i%2 > 0:
        sum += i
print(sum)
print('Все делители числа n')
n = int(input('Введите число n ='))
for i in range(1, n+1):
    if n%i == 0:
        print(i)
print('Факториал числа n')
n = int(input('Введите число n ='))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
