1. ZeroDivisionError

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
2. ValueError (неверный ввод)

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: That was not a valid integer.")
3. FileNotFoundError

try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist.")
4. TypeError (если ввод не число)

try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    if not x.isdigit() or not y.isdigit():
        raise TypeError("Inputs must be numerical.")
    print(int(x) + int(y))
except TypeError as e:
    print("Error:", e)
5. PermissionError

try:
    with open("/root/protected.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Error: Permission denied.")
6. IndexError

try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: Index out of range.")
7. KeyboardInterrupt

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nError: Input cancelled by user.")
8. ArithmeticError

try:
    a = 10
    b = 0
    print(a / b)
except ArithmeticError:
    print("Error: Arithmetic operation failed.")
9. UnicodeDecodeError

try:
    with open("file.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Encoding issue while reading file.")
10. AttributeError

try:
    lst = [1, 2, 3]
    lst.push(4)  # неправильный метод
except AttributeError:
    print("Error: Attribute does not exist.")
🔹 File Input/Output Exercises
1. Read entire file

with open("sample.txt", "r") as f:
    print(f.read())
2. Read first n lines

n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline().strip())
3. Append text

with open("sample.txt", "a") as f:
    f.write("\nNew line added.")
with open("sample.txt", "r") as f:
    print(f.read())
4. Read last n lines

n = 2
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))
5. Store lines in list

with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)
6. Store lines in variable

with open("sample.txt", "r") as f:
    data = f.read()
print(data)
7. Store lines in array

import array
with open("sample.txt", "r") as f:
    arr = array.array('u', f.read())
print(arr)
8. Find longest words

with open("sample.txt", "r") as f:
    words = f.read().split()
print(max(words, key=len))
9. Count lines

with open("sample.txt", "r") as f:
    print("Number of lines:", len(f.readlines()))
10. Word frequency

from collections import Counter
with open("sample.txt", "r") as f:
    words = f.read().replace(",", " ").split()
print(Counter(words))
11. File size

import os
print("File size:", os.path.getsize("sample.txt"), "bytes")
12. Write list to file

lst = ["apple", "banana", "cherry"]
with open("list.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")
13. Copy file

with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())
14. Combine lines from two files

with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())
15. Read random line

import random
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines))
16. Check if file closed

f = open("sample.txt", "r")
print("Closed?", f.closed)
f.close()
print("Closed?", f.closed)
17. Remove newlines

with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)
18. Count words in file

with open("sample.txt", "r") as f:
    words = f.read().replace(",", " ").split()
print("Word count:", len(words))
19. Extract characters from files

files = ["file1.txt", "file2.txt"]
chars = []
for fname in files:
    with open(fname, "r") as f:
        chars.extend(list(f.read()))
print(chars)
20. Generate 26 files A–Z

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}")
21. Alphabet file with fixed letters per line

import string
letters = string.ascii_uppercase
n = 5  # letters per line
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write("".join(letters[i:i+n]) + "\n")
