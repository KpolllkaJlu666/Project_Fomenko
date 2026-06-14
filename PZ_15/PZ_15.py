#Вариант 21. Приложение "Распределение дополнительных обязанностей".
#Программа работает с однотабличной БД SQLite (таблица "Обязанности"):
#ФИО работника, вид дополнительной работы, сумма оплаты, срок.
#Функционал: ввод данных (10 позиций), поиск, удаление и редактирование
#записей (по три SQL-запроса на каждую операцию).

import sqlite3


DB_NAME = "duties.db"


def create_connection():
    #создаём соединение с БД и вернуть объекты connection и cursor
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    return connection, cursor


def create_table():
    #создаём таблицу "Обязанности", если она ещё не существует
    connection, cursor = create_connection()
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS duties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT NOT NULL,
                work_type TEXT NOT NULL,
                payment REAL NOT NULL,
                deadline TEXT NOT NULL
            )
            """
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Ошибка при создании таблицы: {error}")
    finally:
        connection.close()


def fill_initial_data():
    #заполняем таблицу 10 начальными записями, если она пуста
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT COUNT(*) FROM duties")
        count = cursor.fetchone()[0]
        if count > 0:
            print("Таблица уже содержит данные, заполнение не требуется.")
            return

        records = [
            ("Иванов И.И.", "Дежурство", 1500.0, "2026-06-15"),
            ("Петров П.П.", "Подготовка отчёта", 2000.0, "2026-06-20"),
            ("Сидорова А.А.", "Организация мероприятия", 3000.0, "2026-06-25"),
            ("Кузнецов К.К.", "Дежурство", 1500.0, "2026-06-18"),
            ("Смирнова О.О.", "Замена сотрудника", 2500.0, "2026-06-22"),
            ("Васильев В.В.", "Подготовка презентации", 1800.0, "2026-06-19"),
            ("Никитина Н.Н.", "Дежурство", 1500.0, "2026-06-21"),
            ("Морозов М.М.", "Контроль качества", 2200.0, "2026-06-23"),
            ("Егорова Е.Е.", "Подготовка отчёта", 2000.0, "2026-06-27"),
            ("Семенов С.С.", "Организация мероприятия", 3200.0, "2026-06-30"),
        ]

        cursor.executemany(
            """
            INSERT INTO duties (fio, work_type, payment, deadline)
            VALUES (?, ?, ?, ?)
            """,
            records,
        )
        connection.commit()
        print("Добавлено 10 начальных записей.")
    except sqlite3.Error as error:
        print(f"Ошибка при заполнении таблицы: {error}")
    finally:
        connection.close()


def show_all_records():
    #выводим все записи таблицы
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT * FROM duties")
        rows = cursor.fetchall()
        if not rows:
            print("Таблица пуста.")
            return
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f"Ошибка при выводе записей: {error}")
    finally:
        connection.close()


def search_records():
    
    #Поиск записей по условию.
    #Реализованы три варианта поискового SQL-запроса:
    #1. Поиск по ФИО работника (точное совпадение)
    #2. Поиск по виду дополнительной работы (частичное совпадение)
    #3. Поиск по сумме оплаты больше указанного значения

    print("\nВарианты поиска:")
    print("1 - по ФИО работника")
    print("2 - по виду дополнительной работы (часть названия)")
    print("3 - по сумме оплаты больше указанного значения")
    choice = input("Выберите вариант поиска: ").strip()

    connection, cursor = create_connection()
    try:
        if choice == "1":
            fio = input("Введите ФИО работника: ").strip()
            cursor.execute("SELECT * FROM duties WHERE fio = ?", (fio,))
        elif choice == "2":
            work_type = input("Введите часть названия работы: ").strip()
            cursor.execute(
                "SELECT * FROM duties WHERE work_type LIKE ?",
                (f"%{work_type}%",),
            )
        elif choice == "3":
            payment = input("Введите минимальную сумму оплаты: ").strip()
            payment = float(payment)
            cursor.execute(
                "SELECT * FROM duties WHERE payment > ?", (payment,)
            )
        else:
            print("Некорректный вариант поиска.")
            return

        rows = cursor.fetchall()
        if not rows:
            print("Записи не найдены.")
        else:
            for row in rows:
                print(row)
    except (sqlite3.Error, ValueError) as error:
        print(f"Ошибка при поиске: {error}")
    finally:
        connection.close()


def delete_record():
   
    #Удаление записей по условию.
    #Реализованы три варианта удаляющего SQL-запроса:
    #1. Удаление по идентификатору записи (id)
    #2. Удаление по ФИО работника
    #3. Удаление всех записей с истёкшим сроком (deadline меньше указанной даты)
    
    print("\nВарианты удаления:")
    print("1 - по id записи")
    print("2 - по ФИО работника")
    print("3 - по сроку исполнения (удалить все записи раньше даты)")
    choice = input("Выберите вариант удаления: ").strip()

    connection, cursor = create_connection()
    try:
        if choice == "1":
            record_id = int(input("Введите id записи: ").strip())
            cursor.execute("DELETE FROM duties WHERE id = ?", (record_id,))
        elif choice == "2":
            fio = input("Введите ФИО работника: ").strip()
            cursor.execute("DELETE FROM duties WHERE fio = ?", (fio,))
        elif choice == "3":
            deadline = input("Введите дату в формате ГГГГ-ММ-ДД: ").strip()
            cursor.execute(
                "DELETE FROM duties WHERE deadline < ?", (deadline,)
            )
        else:
            print("Некорректный вариант удаления.")
            return

        connection.commit()
        print(f"Удалено записей: {cursor.rowcount}")
    except (sqlite3.Error, ValueError) as error:
        print(f"Ошибка при удалении: {error}")
    finally:
        connection.close()


def edit_record():
    
    #Редактирование записей по условию
    #Реализованы три варианта обновляющего SQL-запроса:
    #1. Изменение суммы оплаты по id записи
    #2. Изменение срока исполнения по ФИО работника
    #3. Изменение вида дополнительной работы по id записи
   
    print("\nВарианты редактирования:")
    print("1 - изменить сумму оплаты по id")
    print("2 - изменить срок исполнения по ФИО работника")
    print("3 - изменить вид работы по id")
    choice = input("Выберите вариант редактирования: ").strip()

    connection, cursor = create_connection()
    try:
        if choice == "1":
            record_id = int(input("Введите id записи: ").strip())
            payment = float(input("Введите новую сумму оплаты: ").strip())
            cursor.execute(
                "UPDATE duties SET payment = ? WHERE id = ?",
                (payment, record_id),
            )
        elif choice == "2":
            fio = input("Введите ФИО работника: ").strip()
            deadline = input("Введите новый срок (ГГГГ-ММ-ДД): ").strip()
            cursor.execute(
                "UPDATE duties SET deadline = ? WHERE fio = ?",
                (deadline, fio),
            )
        elif choice == "3":
            record_id = int(input("Введите id записи: ").strip())
            work_type = input("Введите новый вид работы: ").strip()
            cursor.execute(
                "UPDATE duties SET work_type = ? WHERE id = ?",
                (work_type, record_id),
            )
        else:
            print("Некорректный вариант редактирования.")
            return

        connection.commit()
        print(f"Изменено записей: {cursor.rowcount}")
    except (sqlite3.Error, ValueError) as error:
        print(f"Ошибка при редактировании: {error}")
    finally:
        connection.close()


def main():
   #Главное меню программы
    create_table()
    fill_initial_data()

    menu = """
========== Распределение дополнительных обязанностей ==========
1 - показать все записи
2 - найти записи
3 - удалить запись
4 - редактировать запись
0 - выход
=================================================================
"""

    while True:
        print(menu)
        action = input("Выберите действие: ").strip()

        if action == "1":
            show_all_records()
        elif action == "2":
            search_records()
        elif action == "3":
            delete_record()
        elif action == "4":
            edit_record()
        elif action == "0":
            print("Завершение программы.")
            break
        else:
            print("Некорректный пункт меню, повторите ввод.")


if __name__ == "__main__":
    main()
