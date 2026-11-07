#Даны два целых числа: A, B. Проверить истинность высказывания "Хотябы одно из чисел А и В нечетное"
while True:
    try:
        a = int(input("Введите A: "))
        break
    except ValueError:
        print("Ошибка: введите целое число.")

while True:
    try:
        b = int(input("Введите B: "))
        break
    except ValueError:
        print("Ошибка: введите целое число.")

result = (a % 2 != 0) or (b % 2 !=0)
print("Хотя бы одно из чисел нечетное:", result)