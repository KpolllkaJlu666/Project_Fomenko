#Вариант 21.
#2. В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
# квадратная матрица

from random import randint

n = int(input("Введите размерность квадратной матрицы: "))

matrix = list(
    map(
        lambda _: list(map(lambda _: randint(1, 20), range(n))),
        range(n)
    )
)

print("\nИсходная матрица:")
list(map(print, matrix))

matrix = list(
    map(
        lambda i:
        list(
            map(
                lambda j:
                matrix[i][j] * 2 if i == j else matrix[i][j],
                range(n)
            )
        ),
        range(n)
    )
)

print("\nМатрица после изменения:")
list(map(print, matrix))