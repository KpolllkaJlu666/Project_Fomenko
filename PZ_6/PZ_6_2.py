#Вариант 21
#2. Проверить, является ли список перестановкой чисел 1..N.

N = int(input("Введите размер списка N: "))

A = []
for i in range(N):
    A.append(int(input(f"A[{i+1}]=")))

print("Исходный список:", A)

is_used = [0] * (N+1)   # отметки встреченных элементов

answer = 0
for i in range(N):
    if 1 <= A[i] <= N and is_used[A[i]] == 0:
        is_used[A[i]] = 1
    else:
        answer = i + 1   # номер первого неправильного элемента (1-индексация)
        break

print("Результат:", answer)