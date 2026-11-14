#Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N
while True:
    try:
        n = float(input("Введите целое число N (N>0): "))
        if n > 0:
            break
        print("Число должно быть больше 0!")
    except ValueError:
        print("Неправильно ввели!")

#Вычисление суммы
s = 0
i = 1
while i <= n:
    s += 1 / i
    i += 1

print("s =", i)
print("Сумма равна:", s)