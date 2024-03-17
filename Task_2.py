print('Программа вывода таблицы умножения')
n = int(input('Введие число -> '))
for i in range(1, 10):
    print(i, 'x', n, '=', i * n, sep = ' ')