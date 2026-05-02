#Вариант 21.
#1. В матрице найти минимальный элемент в предпоследней строке.

matrix = [#создаём матрицу (пример)
    [5, 2, 9],
    [8, 1, 4],
    [7, 3, 6]
]

print("Матрица:")
for row in matrix:
    print(row)

row = matrix[-2]#предпоследняя строка

min_value = row[0]#поиск минимума
for x in row:
    if x < min_value:
        min_value = x

print("\nПредпоследняя строка:", row)
print("Минимальный элемент:", min_value)