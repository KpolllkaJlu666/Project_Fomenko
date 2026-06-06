import tkinter as tk
from tkinter import messagebox


def calculate():
    lake = set(entry_lake.get().replace(" ", "").split(","))
    fisherman1 = set(entry_f1.get().replace(" ", "").split(","))
    fisherman2 = set(entry_f2.get().replace(" ", "").split(","))
    fisherman3 = set(entry_f3.get().replace(" ", "").split(","))

    not_caught = lake - (fisherman1 | fisherman2 | fisherman3)

    result_text = (
        f"1 рыбак поймал: {', '.join(fisherman1)}\n"
        f"2 рыбак поймал: {', '.join(fisherman2)}\n"
        f"3 рыбак поймал: {', '.join(fisherman3)}\n\n"
        f"Никто не выловил: {', '.join(not_caught) if not_caught else 'таких видов нет'}"
    )

    messagebox.showinfo("Результат", result_text)


root = tk.Tk()
root.title("Рыбаки и виды рыб")
root.geometry("520x330")
root.resizable(False, False)

tk.Label(root, text="Введите виды рыб через запятую",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Все виды рыб в озере:").pack()
entry_lake = tk.Entry(root, width=60)
entry_lake.pack(pady=3)

tk.Label(root, text="Виды рыб, пойманные 1 рыбаком:").pack()
entry_f1 = tk.Entry(root, width=60)
entry_f1.pack(pady=3)

tk.Label(root, text="Виды рыб, пойманные 2 рыбаком:").pack()
entry_f2 = tk.Entry(root, width=60)
entry_f2.pack(pady=3)

tk.Label(root, text="Виды рыб, пойманные 3 рыбаком:").pack()
entry_f3 = tk.Entry(root, width=60)
entry_f3.pack(pady=3)

tk.Button(root, text="Определить результат", command=calculate).pack(pady=15)

root.mainloop()