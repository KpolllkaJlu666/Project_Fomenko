#Вариант 21.
#2. В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
# квадратная матрица
matrix = [
    [5, 2, 9],
    [8, 1, 4],
    [7, 3, 6]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(len(matrix)):#изменяем диагональ
    matrix[i][i] = matrix[i][i] * 2

print("\nМатрица после изменения:")
for row in matrix:
    print(row)