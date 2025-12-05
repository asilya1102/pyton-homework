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




