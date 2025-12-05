1. is_prime(n) funksiyasi
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Misollar
print(is_prime(4))  # False
print(is_prime(7))  # True

# filter bilan: berilgan ro‘yxatdan faqat tub sonlarni olish
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)  # [2, 3, 5, 7]

2.digit_sum(k) funksiyasi
def digit_sum(k):
    return sum(map(int, str(k)))

# Misollar
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

# map bilan: bir nechta sonlarning raqam yig‘indisini hisoblash
nums = [24, 502, 123]
sums = list(map(lambda x: digit_sum(x), nums))
print(sums)  # [6, 7, 6]

3. Ikki sonning darajalari (2 ning darajalari)
def powers_of_two(N):
    result = []
    k = 1
    while 2**k <= N:
        result.append(2**k)
        k += 1
    return result

# Misol
print(powers_of_two(10))  # [2, 4, 8]

# map bilan: darajalarni string ko‘rinishda chiqarish
print(" ".join(map(str, powers_of_two(10))))  # 2 4 8
