# ==================================== 1 задание ====================================

print("=" * 30)
try:
    number = int(input("введите число от 1 до 100: "))
    if 1 <= number <= 100:
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)
    else:
       print("ошибка: число должно быть в диапазоне от 1 до 100")

       print()


# ==================================== 2 задание ====================================

x = int(input("введите число:"))
for i in range(8):
    print(x,"^" , i ,  "=" , x**i)


# ==================================== 3 задание ====================================
cost = float(input("введите стоимость разговора:"))
print("выберите оператора, с которого звонят:")
print("1 - МТС\n2 - Мегафон\n3 - Билайн")
from_op = int(input("введите номер:"))

if from_op == 1:
    from_name = ("МТС")
elif from_op == 2:
    from_name = ("Мегафон")
elif from_op == 3:
    from_name = ("Билайн")
else:
    print("ошибка: нет такого оператора!")
    exit()

print("выберите оператора , на который звонят:")
print("1 - МТС\n2 - Мегафон\n3 - Билайн")
to_op = int(input("введите номер:"))

if to_op == 1:
    to_name = ("МТС")
elif to_op == 2:
    to_name = ("Мегафон")
elif to_op == 3:
    to_name = ("Билайн")
else:
    print("ошибка:нет такого оператора!")
    exit()

    # результат
print("звонок с" , from_name , "на" , to_name)
print("стоимость разговора:" , cost, "руб.")

# ==================================== 4 задание ====================================
base = 200
sales = []

for i in range(3):
    s = int(input("продажи менеджера" + str(i+1 ) + ": "))
    sales.append(s)

salaries = []

if s <= 500:
    percent = 0.03
elif s <= 1000:
   percent = 0.05
else:
    percent = 0.08
salary = base + s * percent
salaries.append(salary)

best = max(sales)
best_index = sales.index(best)
salaries[best_index] += 200

for i in range(3):
    print("менеджер" , i+1 , "зарплата = ", salaries[i])
    print("лучший менеджер:" , best_index+1)
