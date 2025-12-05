1. Создание виртуальной среды и установка пакетов
bash
# Создать виртуальную среду
python -m venv venv

# Активировать виртуальную среду
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установить пакеты (пример)
pip install requests numpy
🔹 2. Модуль math_operations.py
python
# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
🔹 3. Модуль string_utils.py
python
# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
🔹 4. Пакет geometry
Структура:

Код
geometry/
    __init__.py
    circle.py
python
# geometry/__init__.py
# можно оставить пустым или импортировать функции
from .circle import calculate_area, calculate_circumference
python
# geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
🔹 5. Пакет file_operations
Структура:

Код
file_operations/
    __init__.py
    file_reader.py
    file_writer.py
python
# file_operations/__init__.py
from .file_reader import read_file
from .file_writer import write_file
python
# file_operations/file_reader.py
def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()
python
# file_operations/file_writer.py
def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
🔹 6. Пример использования
python
from math_operations import add, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

print(add(5, 3))                     # 8
print(divide(10, 2))                 # 5.0
print(reverse_string("hello"))       # olleh
print(count_vowels("assalom"))       # 3
print(calculate_area(5))             # 78.5398...
print(calculate_circumference(5))    # 31.4159...

write_file("test.txt", "Hello World")
print(read_file("test.txt"))
