1. Age Calculator

from datetime import datetime

# Ask for user's name
name = input("Enter your name: ")

# Ask for user's year of birth
year_of_birth = int(input("Enter your year of birth: "))

# Get the current year
current_year = datetime.now().year

# Calculate age
age = current_year - year_of_birth

# Display result
print(f"Hello, {name}! You are {age} years old.")


2. Extract Car Names

txt = "LMaasleitbtui"
car_names = ["BMW", "Tesla", "Maserati", "Malibu", "Toyota", "Honda"]

found = [car for car in car_names if all(ch in txt for ch in car.lower())]
print("Extracted car names:", found)

3. Extract Car Names

txt = 'MsaatmiazD'
car_names = ["Mazda", "Tesla", "Maserati", "Malibu", "Toyota", "Honda"]

found = [car for car in car_names if all(ch in txt for ch in car.lower())]
print("Extracted car names:", found)

4.Extract Residence Area

txt = "I'am John. I am from London"

# Разобьём текст на слова
words = txt.split()

# Найдём слово после "from"
if "from" in words:
    index = words.index("from")
    residence = words[index + 1]
    print("Residence area:", residence)

5. Reverse String

# Ask for user input
text = input("Enter a string: ")

# Reverse using slicing
print("Reversed string:", text[::-1])

6. text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)

print("Number of vowels:", count)

7. Find Maximum Value
# Input list of numbers separated by spaces
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

# Find maximum
print("Maximum value:", max(numbers))

8. Check Palindrome
word = input("Enter a word: ")

if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

9. Extract Email Domain
email = input("Enter your email address: ")

# Split at '@' and take the second part
domain = email.split("@")[-1]

print("Email domain:", domain)

10. Generate Random Password

import random
import string

# Define characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password of length 12
password = ''.join(random.choice(characters) for _ in range(12))

print("Random password:", password)
