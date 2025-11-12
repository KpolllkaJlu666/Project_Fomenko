#
x = float(input())
n = int(input())

s = 0.0
k = 1
p = x        # x^k
sgn = 1      # (-1)^(k-1)

while k <= n:
    s += sgn * p / k
    p *= x
    sgn = -sgn
    k += 1

print(s)