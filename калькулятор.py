print ('Hello my Master')
q1 = int (input('Введите число 1: '))
q2 = int (input('Введите число 2: '))

v = int (input('Че делать будем? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

if v == 1:
    r = q1 + q2
    p = 'сложения'
    t = p
if v == 2:
    r = q1 - q2
    l = 'вычитания'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'деления'
    t = m
if v == 4:
    r = q1 * q2
    n = 'умножения'
    t = n
print ('Во че вышло ',t,' = ',r)