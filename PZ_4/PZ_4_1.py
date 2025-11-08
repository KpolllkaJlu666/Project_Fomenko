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
