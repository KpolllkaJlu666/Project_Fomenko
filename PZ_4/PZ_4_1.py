<<<<<<< HEAD
#№1 Сумма ряда: X - X^2/2 + X^3/3 - ... + (-1)^(N-1) * X^N / N
# (приближение ln(1+X), |X| < 1, N > 0)

try:
    x = float(input("Введите X (|X| < 1): ").strip())
    n = int(input("Введите N (целое > 0): ").strip())
    if not (-1 < x < 1) or n <= 0:
        raise ValueError

    k = 1
    term = x            # первый член: x
    s = 0.0

    while k <= n:
        s += term
        # готовим следующий член через рекуррентное соотношение:
        # term_k -> term_{k+1} = term_k * (-(x)) * (k/(k+1))
        k_plus_1 = k + 1
        if k_plus_1 <= n:
            term = term * (-x) * (k / k_plus_1)
        k = k_plus_1

    print("Сумма первых N членов:", s)

except ValueError:
    print("Неверный ввод: требуется |X| < 1 и целое N > 0.")
=======
# 1 

try:
    x = float(input())
    n = int(input())
    if not (-1 < x < 1) or n <= 0:
        raise ValueError
    s = 0
    k = 1
    term = x
    while k <= n:
        s += term
        k1 = k + 1
        if k1 <= n:
            term = term * (-x) * (k / k1)
        k = k1
    print(s)
except:
    print("error")

try:
    m = int(input())
    if m <= 0:
        raise ValueError
    t = m
    while t % 3 == 0:
        t //= 3
    if t == 1:
        print("TRUE")
    else:
        print("FALSE")
except:
    print("error")
>>>>>>> f51874772bbe6a86d7f6d60b28db20b9c6b4c64f
