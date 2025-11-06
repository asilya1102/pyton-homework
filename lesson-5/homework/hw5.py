# 1. Проверка на високосный год (is_leap)
def is_leap(year):
    """
    Определяет, является ли данный год високосным.

    Год является високосным, если:
    - делится на 4, и
    - не делится на 100, кроме случаев, когда делится на 400.

    Параметры:
        year (int): Год для проверки.

    Возвращает:
        bool: True, если год високосный, иначе False.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Пример использования:
print(is_leap(2000)) # True
print(is_leap(1900)) # False
print(is_leap(2024)) # True

# 2. Условные операторы (Weird / Not Weird)
n = int(input("Введите число: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# Пример:

Ввод: 3 → Вывод: Weird

Ввод: 24 → Вывод: Not Weird

# 3. Найти чётные числа между a и b (включительно) без цикла
# Решение 1 — с использованием if-else
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Определяем начало (первое чётное число)
if a % 2 != 0:
    a += 1

# Создаём список чётных чисел через range (без цикла for)
even_numbers = list(range(a, b + 1, 2))
print("Чётные числа между a и b:", even_numbers)

# Решение 2 — без использования if-else
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Используем тернарный оператор (без if-else блока)
start = a + (a % 2)
even_numbers = list(range(start, b + 1, 2))
print("Чётные числа между a и b:", even_numbers)
