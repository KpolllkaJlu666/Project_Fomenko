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