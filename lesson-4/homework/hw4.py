# 1. Sort a Dictionary by Value
my_dict = {'a': 3, 'b': 1, 'c': 2}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Сортировка по возрастанию:", ascending)
print("Сортировка по убыванию:", descending)

# 2. Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print("Обновлённый словарь:", d)

# 3.Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {}
for d in (dic1, dic2, dic3):
    merged_dict.update(d)

print("Объединённый словарь:", merged_dict)


# 4. Generate a Dictionary with Squares
n = int(input("Введите число n: "))
squares = {x: x**2 for x in range(1, n+1)}
print("Словарь квадратов:", squares)


# 5. Dictionary of Squares (1 to 15)
squares_15 = {x: x**2 for x in range(1, 16)}
print("Словарь квадратов (1–15):", squares_15)

# Set Exercises
# 1. Create a Set
my_set = {"яблоко", "банан", "киви"}
print("Созданное множество:", my_set)

# 2. Iterate Over a Set
fruits = {"яблоко", "банан", "груша"}
print("Элементы множества:")
for fruit in fruits:
    print(fruit)

# 3. Add Member(s) to a Set
numbers = {1, 2, 3}
numbers.add(4)
numbers.update([5, 6])
print("После добавления:", numbers)

# 4. Remove Item(s) from a Set
colors = {"red", "blue", "green"}
colors.remove("blue")
print("После удаления:", colors)

# 5. Remove an Item if Present in the Set
cities = {"London", "Paris", "Rome"}
cities.discard("Paris")
print("После удаления:", cities)
