#21. В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить 
#фразу «Министерства образования Ростовской области», посчитать количество 
#произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,«50».
#Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re

f = open('hotline.txt', encoding='UTF-8')#открываем файл
text = f.read()
f.close()



new_text = re.sub(#добавление фразы
    r'Горячая линия',
    'Горячая линия Министерства образования Ростовской области',
    text
)

count_replace = len(re.findall(r'Горячая линия', text))#считаем сколько замен сделали

phones = re.findall(r'\d{11}', text)#поиск номеров

end_03 = [p for p in phones if p.endswith('03')]
end_50 = [p for p in phones if p.endswith('50')]

ege = re.findall(r'.*(ЕГЭ|ГИА).*\d{11}', text)#номера ЕГЭ/ГИА

f2 = open('result.txt', 'w', encoding='UTF-8')#запись в новый файл
f2.write(new_text)
f2.close()

print("Количество добавлений:", count_replace)
print("Номера на 03:", end_03)
print("Номера на 50:", end_50)
print("Номера ЕГЭ/ГИА:", ege)
