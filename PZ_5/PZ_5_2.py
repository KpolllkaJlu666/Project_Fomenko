# Вариант 21
#2. Описать функцию Power1(A, B) вещественного типа, 
# находящую величину AB по формуле AB = exp(B*ln(A)) 
# (параметры A и B — вещественные). В случае нулевого
# ы или отрицательного параметра A функция возвращает 0. С помощью этой функции найти степени AP

import math
# Функция вычисления A^B через exp(B * ln(A))
def Power1(A, B):
    if A <= 0:
        return 0
    return math.exp(B * math.log(A)) #формула AB = exp(B*ln(A))


# Ввод данных с проверкой
def input_float(msg):
    x = input(msg)
    while True:
        try:
            x = float(x) #если можно преобразить, возвращаем число
            return x
        except ValueError:
            print("Неверный ввод!")
            x = input(msg)


# Ввод значений
P = input_float("Введите P: ")
A = input_float("Введите A: ")
B = input_float("Введите B: ")
C = input_float("Введите C: ")

# Вывод результатов
print("A^P =", Power1(A, P))
print("B^P =", Power1(B, P))
print("C^P =", Power1(C, P))