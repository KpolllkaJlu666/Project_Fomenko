

try:
    N = int(input("Введите количество чисел N (>0): ")) #вводим количкство N
    if N <= 0:
        raise ValueError

    # ввод первого числа и установка min или max. то есть он распределяет куда это число отнести 
    x = float(input("Введите число: "))
    minimum = x
    maximum = x

    # оставшиеся N-1 чисел
    for i in range(N - 1):
        x = float(input("Введите число: "))
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
#выводим результаты
    print("Минимальное значение:", minimum)
    print("Максимальное значение:", maximum)

except ValueError:
    print("Неверный ввод: нужно число N > 0 и корректные значения.")