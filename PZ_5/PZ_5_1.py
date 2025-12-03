# Вариант 21
# 1. Составить функцию, которая выполнит суммирования числового ряда.
def sum_range(N):
    s = 0
    for i in range(1, N + 1):
        s += i
    return s

# Проверка корректности ввода
N = input("Введите целое число N: ")

while type(N) != int: #пока не целое число
    try:
        N = int(N)
    except ValueError:
        print("Некорректный ввод!")
        N = input("Введите целое число N: ")

print("Сумма ряда от 1 до", N, "=", sum_range(N))
