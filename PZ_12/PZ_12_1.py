#Вариант 21.
#1. В матрице найти минимальный элемент в предпоследней строке.

from random import randint

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = list(
    map(
        lambda _: list(map(lambda _: randint(1, 20), range(m))),
        range(n)
    )
)

print("\nМатрица:")
list(map(print, matrix))

pre_last_row = matrix[-2]

min_element = min(pre_last_row)

print("\nПредпоследняя строка:", pre_last_row)
print("Минимальный элемент:", min_element)