#1. Создание списка и доступ к элементу
fruits = ["яблоко", "банан", "киви", "апельсин", "груша"]
print("Третий фрукт:", fruits[2])

# 2. Конкатенация двух списков
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Объединённый список:", combined)

# 3. Извлечение элементов
numbers = [10, 20, 30, 40, 50]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print("Новый список:", new_list)

# 4. Преобразование списка в кортеж
movies = ["Матрица", "Интерстеллар", "Начало", "Титаник", "Аватар"]
movies_tuple = tuple(movies)
print("Кортеж фильмов:", movies_tuple)

# 5. Проверка элемента
cities = ["London", "Paris", "Rome", "Berlin"]
if "Paris" in cities:
    print("Париж есть в списке!")
else:
    print("Парижа нет в списке.")

# 6. Дублирование списка
nums = [1, 2, 3]
duplicate = nums * 2
print("Дублированный список:", duplicate)

# 7. Обмен элементов
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("После обмена:", nums)

# 8. Срез кортежа
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Срез с 3 по 7 индекс:", t[3:8])

# 9. Подсчёт количества элементов
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print("Количество 'blue':", count_blue)

# 10. Индекс элемента
animals = ("cat", "dog", "lion", "tiger")
index_lion = animals.index("lion")
print("Индекс 'lion':", index_lion)

# 11. Объединение кортежей
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print("Объединённый кортеж:", merged)

# 12. Длина списка и кортежа
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7)
print("Длина списка:", len(my_list))
print("Длина кортежа:", len(my_tuple))

# 13. Кортеж → список
nums_tuple = (10, 20, 30, 40, 50)
nums_list = list(nums_tuple)
print("Преобразованный список:", nums_list)

# 14. Максимум и минимум
numbers = (5, 10, 2, 8, 3)
print("Максимум:", max(numbers))
print("Минимум:", min(numbers))

# 15. Разворот кортежа
words = ("один", "два", "три", "четыре")
reversed_tuple = words[::-1]
print("Кортеж в обратном порядке:", reversed_tuple)
