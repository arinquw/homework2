# ====== Задание 1 ======

# Произведение элементов списка
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# пример
lst1 = [2, 3, 4]
print("Задание 1:", multiply_list(lst1))


# ====== Задание 2 ======

# Минимум без функции min()
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

lst2 = [5, 2, 9, -3, 7]
print("Задание 2:", find_min(lst2))


# ====== Задание 3 ======

# Количество простых чисел
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count

lst3 = [2, 3, 4, 5, 10, 11]
print("Задание 3:", count_primes(lst3))


# ====== Задание 4 ======

# Удалить заданное число и посчитать, сколько удалено
def remove_number(numbers, value):
    count = numbers.count(value)
    new_list = []
    for num in numbers:
        if num != value:
            new_list.append(num)
    print("Задание 4: количество удалённых элементов:", count)
    return new_list

lst4 = [1, 2, 3, 2, 4, 2]
lst4 = remove_number(lst4, 2)
print("Задание 4: новый список:", lst4)


# ====== Задание 5 ======

# Объединение двух списков
def merge_lists(list1, list2):
    return list1 + list2

a = [1, 2, 3]
b = [4, 5, 6]
print("Задание 5:", merge_lists(a, b))


# ====== Задание 6 ======

# Возведение элементов списка в степень
def power_list(numbers, power):
    result = []
    for num in numbers:
        result.append(num ** power)
    return result

lst6 = [1, 2, 3, 4]
print("Задание 6:", power_list(lst6, 3))
