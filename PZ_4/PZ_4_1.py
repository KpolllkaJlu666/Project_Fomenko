#№1 Сумма ряда: X - X^2/2 + X^3/3 - ... + (-1)^(N-1) * X^N / N (приближение ln(1+X), |X| < 1, N > 0)

try:
    x = float(input("Введите X (|X| < 1): "))
    n = int(input("Введите N (целое > 0): "))

    if (-1 < x < 1) and (n > 0):
        s = 0.0
        term = x  # первый член: x
        for k in range(1, n + 1):
            s += term
            term *= (-x) * (k / (k + 1))  # term_k -> term_{k+1}
        print("Сумма первых N членов:", s)
    else:
        print("Неверный ввод: требуется |X| < 1 и целое N > 0.")

except ValueError:
    print("Неверный ввод: требуется |X| < 1 и целое N > 0.")