#Вариант 21
#Блок заданий 1, задача 21: класс "Календарь" с атрибутами год, месяц, день.
#Методы: определение дня недели, проверка на високосный год, определение количества дней в месяце.
#Блок заданий 2, задача 21: базовый класс "Животное" со свойствами вид,
#количество лап, цвет шерсти. Класс "Собака" наследуется от "Животное" и добавляет свойства кличка и порода.

import calendar
import datetime


class Calendar:
    #класс "Календарь" для работы с датой (год, месяц, день)

    DAY_NAMES = (
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье",
    )

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def day_of_week(self):
        #вернуть название дня недели для текущей даты
        date = datetime.date(self.year, self.month, self.day)
        return self.DAY_NAMES[date.weekday()]

    def is_leap_year(self):
        #проверить, является ли год високосным
        return calendar.isleap(self.year)

    def days_in_month(self):
        #вернуть количество дней в текущем месяце
        return calendar.monthrange(self.year, self.month)[1]


class Animal:
    #базовый класс "Животное"

    def __init__(self, species, legs_count, fur_color):
        self.species = species
        self.legs_count = legs_count
        self.fur_color = fur_color

    def info(self):
        #вернуть строку с информацией о животном
        return (
            f"Вид: {self.species}, "
            f"Количество лап: {self.legs_count}, "
            f"Цвет шерсти: {self.fur_color}"
        )


class Dog(Animal):
    #класс "Собака", наследуется от "Животное"

    def __init__(self, species, legs_count, fur_color, nickname, breed):
        super().__init__(species, legs_count, fur_color)
        self.nickname = nickname
        self.breed = breed

    def info(self):
        #вернуть строку с информацией о собаке, дополняя данные родителя
        base_info = super().info()
        return f"{base_info}, Кличка: {self.nickname}, Порода: {self.breed}"


def main():
    #тестовые запуски реализованных классов
    print("=== Блок заданий 1, задача 21: класс Calendar ===")
    today = Calendar(2026, 6, 13)
    print(f"Дата: {today.year}-{today.month:02d}-{today.day:02d}")
    print(f"День недели: {today.day_of_week()}")
    print(f"Високосный год: {today.is_leap_year()}")
    print(f"Дней в месяце: {today.days_in_month()}")

    leap_date = Calendar(2024, 2, 29)
    print(f"\nДата: {leap_date.year}-{leap_date.month:02d}-{leap_date.day:02d}")
    print(f"День недели: {leap_date.day_of_week()}")
    print(f"Високосный год: {leap_date.is_leap_year()}")
    print(f"Дней в месяце: {leap_date.days_in_month()}")

    print("\n=== Блок заданий 2, задача 21: классы Animal и Dog ===")
    cat = Animal("Кошка", 4, "рыжий")
    print(cat.info())

    dog = Dog("Собака", 4, "чёрный", "Бобик", "овчарка")
    print(dog.info())


if __name__ == "__main__":
    main()
