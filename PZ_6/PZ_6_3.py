#Вариант 21
#3. Найти точку из множества A, ближайшую к точке B.

import math

N = int(input("Введите количество точек: "))

# Списки координат
X = []
Y = []

print("Введите координаты точек А:")
for i in range(N):
    x = float(input(f"x{i+1} = "))
    y = float(input(f"y{i+1} = "))
    X.append(x)
    Y.append(y)

# Координаты точки B
Bx = float(input("Введите координату Bx: "))
By = float(input("Введите координату By: "))

min_dist = float('inf')
index_min = 0

for i in range(N):
    R = math.sqrt((X[i] - Bx)**2 + (Y[i] - By)**2)
    if R < min_dist:
        min_dist = R
        index_min = i

print("Ближайшая точка к B:")
print(f"A{index_min+1} = ({X[index_min]}, {Y[index_min]})")
print("Расстояние:", min_dist)