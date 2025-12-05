1. Circle Class
python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Test
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
2. Person Class
python
from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob = date(year, month, day)

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

# Test
p = Person("Ali", "Uzbekistan", date(1993, 2, 11))
print("Age:", p.age())
3. Calculator Class
python
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): 
        if b == 0: raise ValueError("Division by zero!")
        return a / b

# Test
calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(10, 2))
4. Shape and Subclasses
python
import math

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
5. Binary Search Tree Class
python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None: node.left = Node(key)
            else: self._insert(node.left, key)
        else:
            if node.right is None: node.right = Node(key)
            else: self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None: return False
        if node.key == key: return True
        elif key < node.key: return self._search(node.left, key)
        else: return self._search(node.right, key)
6. Stack Data Structure
python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
7. Linked List Data Structure
python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
8. Shopping Cart Class
python
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name):
        if name in self.items: del self.items[name]

    def total(self):
        return sum(self.items.values())

# Test
cart = ShoppingCart()
cart.add_item("Book", 10)
cart.add_item("Pen", 2)
print("Total:", cart.total())
9. Stack with Display
python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def display(self): print(self.items)
10. Queue Data Structure
python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None
11. Bank Class
python
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount

    def balance(self, name):
        return self.accounts.get(name, "Account not found")

# Test
bank = Bank()
bank.create_account("Ali", 100)
bank.deposit("Ali", 50)
print("Balance:", bank.balance("Ali"))
