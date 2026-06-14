#Вариант 21
#Даны две последовательности.Найти элементы, различные для двух 
# последовательностей,и их среднее арифметическое.

from random import randint
from functools import reduce

# Ввод размерности
n = int(input("Введите количество видов рыб в озере: "))

# Генерация видов рыб (номера видов)
lake = set(map(lambda _: randint(1, 20), range(n)))

# Каждый рыбак ловит случайные виды рыб из озера
fisherman1 = set(filter(lambda x: randint(0, 1), lake))
fisherman2 = set(filter(lambda x: randint(0, 1), lake))
fisherman3 = set(filter(lambda x: randint(0, 1), lake))

# Виды рыб, которые никто не поймал
caught = reduce(lambda a, b: a | b,
                [fisherman1, fisherman2, fisherman3])

not_caught = lake - caught

print("\nВиды рыб в озере:", lake)
print("1 рыбак поймал:", fisherman1)
print("2 рыбак поймал:", fisherman2)
print("3 рыбак поймал:", fisherman3)
print("Не поймал никто:", not_caught)