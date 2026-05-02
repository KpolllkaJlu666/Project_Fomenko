# Вариант 21
# Из заданной строки отобразить только цифры. Использовать библиотеку string.

import string

text = (
    "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, "
    "755 feet (230metres) longand 481 feet (147 metres) high."
)

digits = [ch for ch in text if ch in string.digits]#проверяет каждый символ строки и оставляет только цифры

print("Исходная строка:")
print(text)

print("Цифры из строки:")
print(digits)

print("Цифры строкой:")
print("".join(digits))