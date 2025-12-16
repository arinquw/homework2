# ==================== 1 ===================

import random

lst = [random.randint(-10, 10) for _ in range(20)]
print("исходный список:", lst)

# делим список пополам
mid = len(lst) // 2
left = sorted(lst[:mid])                  # по возрастанию
right = sorted(lst[mid:], reverse=True)   # по убыванию

result = left + right
print("результат:", result)


# ==================== 2 ===================

import random

lst = [random.randint(-20, 20) for _ in range(45)]
print("исходный список:", lst)

size = len(lst) // 3
p1, p2, p3 = lst[:size], lst[size:2*size], lst[2*size:]

max_p2 = max(p2)
min_p2 = min(p2)

middle = []
for i in range(len(p2)):
    middle.append(max_p2 if i % 2 == 0 else min_p2)

result = [x for x in p1 if x % 2 == 0] + middle + [x for x in p3 if x % 2 != 0]

print("результат:", result)
