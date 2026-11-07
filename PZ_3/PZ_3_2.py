# Дан номер действия N (целое число в диапазоне 1-4) и вещественные числа A и B (В не равно 0)
# Выполнить над числами указанное действие и вывести результат.
while True:
    n = input("Номер действия (1-сложение, 2-вычитание, 3-умножение, 4-деление):")
    try:
        n = int(n)
        if n < 1 or n > 4:
            print("Некорректное значение")
        else:
            break
    except ValueError:
        print("Неправильное действие")

while True:
    a = input("Введите А:")
    try:
        a = float(a)
        break
    except ValueError:
        print("Неккоректное значение")
while True:
    b = input("Введите В( не равно 0): ")
    try:
        b = float(b)
        if b == 0:
            print("В не должно быть 0")
        else:
            break
    except ValueError:
        print("НЕкорректное значение")

if n == 1:
    print(a + b)
if n == 2:
    print(a - b)
if n == 3:
    print(a * b)
if n == 4:
    print(a / b)