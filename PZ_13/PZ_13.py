# 21. В исходном текстовом файле hotline.txt после фразы «Горячая линия»
# добавить фразу «Министерства образования Ростовской области»,
# посчитать количество произведённых добавлений.
# Сколько номеров телефонов заканчивается на «03», «50».
# Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re

with open("hotline.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern_insert = r"Горячая линия"#добавление фразы после "Горячая линия"
text_new, count_insert = re.subn(
    pattern_insert,
    "Горячая линия Министерства образования Ростовской области",
    text
)

count_03 = len(re.findall(r"\d*03\b", text_new))#подсчёт номеров, заканчивающихся на 03 и 50
count_50 = len(re.findall(r"\d*50\b", text_new))

matches = re.findall(r"(ЕГЭ|ГИА).*(\+?\d[\d\s\-\(\)]{5,})", text_new)#номера, связанные с ЕГЭ/ГИА
ege_gia_phones = [m[1] for m in matches]

print("Количество добавлений фразы:", count_insert)#вывод результатов
print("Номера, заканчивающиеся на 03:", count_03)
print("Номера, заканчивающиеся на 50:", count_50)

print("\nТелефоны ЕГЭ/ГИА:")
for phone in ege_gia_phones:
    print(phone)

with open("hotline_new.txt", "w", encoding="utf-8") as f:#(опционально) запись результата в новый файл
    f.write(text_new)