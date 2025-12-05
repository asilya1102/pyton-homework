Exercise 1: Threaded Prime Number Checker
python
import threading

# Проверка на простое число
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция для потока
def check_range(start, end, primes):
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)

def main():
    start, end = 1, 100  # диапазон чисел
    num_threads = 4
    step = (end - start) // num_threads

    threads = []
    primes = []

    for i in range(num_threads):
        s = start + i * step
        e = start + (i + 1) * step if i < num_threads - 1 else end
        t = threading.Thread(target=check_range, args=(s, e, primes))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Prime numbers:", sorted(primes))

if __name__ == "__main__":
    main()
📌 В этом примере диапазон [1, 100] делится на 4 части, каждая проверяется отдельным потоком.

 Exercise 2: Threaded File Processing
python
import threading
from collections import Counter

# Функция для обработки части файла
def process_lines(lines, counter):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)

def main():
    filename = "large_text.txt"
    num_threads = 4

    # Читаем все строки
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    step = len(lines) // num_threads
    threads = []
    counters = []

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], counters))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Объединяем результаты
    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    print("Word occurrences:")
    for word, count in total_counter.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
