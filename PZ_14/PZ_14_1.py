#Вариант 21
#https://lh5.googleusercontent.com/- 
#wG_YHAIbVZU/Ud696wJg0FI/AAAAAAAACP4/eaIzPTZRixE/w596-h642-no/4_3.png
import tkinter as tk
from tkinter import ttk, messagebox


def submit():
    messagebox.showinfo("Данные подтверждаю", "Форма отправлена!")


root = tk.Tk()
root.title("Обработка формы")
root.geometry("596x642")
root.resizable(False, False)

title = tk.Label(root, text="Форма регистрации пользователя",
                 font=("Arial", 14, "bold"))
title.pack(pady=18)

frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
frame.pack()

labels = [
    "Ваше имя:", "Пароль:", "Возраст:", "Пол:",
    "Ваши увлечения:", "Ваша страна:", "Ваш город:",
    "Кратко о себе:"
]

for i, text in enumerate(labels):
    tk.Label(frame, text=text, font=("Arial", 10), anchor="w").grid(
        row=i, column=0, sticky="w", pady=7
    )

entry_name = tk.Entry(frame, width=38, bg="#cfcfcf", relief="flat")
entry_name.grid(row=0, column=1, columnspan=4, pady=7)

entry_pass = tk.Entry(frame, width=38, bg="#cfcfcf", relief="flat", show="*")
entry_pass.grid(row=1, column=1, columnspan=4, pady=7)

entry_age = tk.Entry(frame, width=38, bg="#cfcfcf", relief="flat")
entry_age.grid(row=2, column=1, columnspan=4, pady=7)

gender = tk.StringVar(value="Мужской")
tk.Radiobutton(frame, text="Мужской", variable=gender,
               value="Мужской").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame, text="Женский", variable=gender,
               value="Женский").grid(row=3, column=4, sticky="e")

music = tk.BooleanVar()
video = tk.BooleanVar()
draw = tk.BooleanVar()

tk.Checkbutton(frame, text="Музыка", variable=music).grid(row=4, column=1)
tk.Checkbutton(frame, text="Видео", variable=video).grid(row=4, column=2)
tk.Checkbutton(frame, text="Рисование", variable=draw).grid(row=4, column=3)

country = ttk.Combobox(frame, width=35, values=["Россия", "Беларусь", "Казахстан"])
country.grid(row=5, column=1, columnspan=4, pady=7)

city = ttk.Combobox(frame, width=35, values=["Москва", "Санкт-Петербург", "Казань"])
city.grid(row=6, column=1, columnspan=4, pady=7)

about = tk.Text(frame, width=38, height=3, bg="#cfcfcf", relief="flat")
about.insert("1.0", "краткая информация о ваших увлечениях")
about.grid(row=7, column=1, columnspan=4, pady=7)

tk.Label(frame, text="Решите пример, запишите результат в поле ниже:",
         font=("Arial", 10)).grid(row=8, column=0, columnspan=5, sticky="w", pady=12)

answer = tk.Entry(frame, width=38, bg="#cfcfcf", relief="flat")
answer.grid(row=9, column=1, columnspan=4, pady=7)

tk.Button(frame, text="Отменить ввод", command=lambda: answer.delete(0, tk.END)).grid(
    row=10, column=1, pady=7
)
tk.Button(frame, text="Данные подтверждаю", command=submit).grid(
    row=10, column=3, pady=7
)

root.mainloop()
