#эксперимент монте-карло
import datetime
from random import randint

def getbirthday(numberOfBirthdays):
    birthdays = [] # список дней рождений
    for i in range(numberOfBirthdays):
        # год в нашей имитации роли не играет,
        # лишь бы в объектах дней рождения он был одинаков
        start0Year = datetime.date(2000, 1, 1)
        # случайный день года
        randomNumberOfDays = datetime.timedelta(randint(0, 364))
        birthday = start0Year + randomNumberOfDays
        birthdays.append(birthday) # добавляем в список
    return birthdays

'''
принимает список дней рождений. обрабатывает его и возвращает совпадения в 
датах, которые встречаются несколько раз
'''
def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # даты не совпадают, выходим из программы
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA # даты совпали

# MAIN
def main():
    # кортеж месяцев в году
    Months = ('Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , "Jun" ,
              "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec")
    print("Добро пожаловать в приложение для симуляции совпадения "
          "дат рождения")
    while True: # апрашвает данные, пока пользователь
        # не введет допустимые значения
        print("сколько симуляций вы хотите сделать \n P.S. max = 100")
        response = input("--->")
        if response.isdecimal() and 0 < int(response) <= 100:
            numBDdays = int(response)
            break
    print()
    # генерируем и отображаем дни рождения
    birthdays = getbirthday(numBDdays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(", ", end="")
        months = Months[birthday.month - 1]
        dateText = "{} {}".format(months, birthday.day)
        print(dateText, end="")
    print()
    print()
    print(f"генерация {numBDdays} случайных симуляций")
    input("для продолжения введите Enter...")
    print("запуск 100000 симуляций")
    simMatch = 0
    for i in range(100000):
        if i % 10000 == 0 and i != 0:
            print(i, "запущена симуляция...")
        birthdays = getbirthday(numBDdays)
        if getMatch(birthdays) != None:
            simMatch += 1
    print("было выполнено 100000 симуляций.")
    probability = round(simMatch / 100000 * 100, 2)
    print("процент попадения", probability, "%")
    print("количество дат для исследования:", numBDdays)
    print("количество циклов симуляции:", simMatch)

if __name__ == '__main__':
    main()

#1 вопрос
# др пооказаны как объекты datetime.date где фиксируется год
# а меняются только месяц и день
#
# 2вопрос
# надо изменить или в крайнем случае удалить часть условия
# f response.isdecimal() and 0 < int(response) <= 100:
# на
# if response.isdecimal() and int(response) > 0:
# теперь можно ввести любое количество
#
# 3 вопрос
# прога выдаст ошибку тк переменная используется хотя ее нет
# NameError: name 'numBDdays' is not defined
#
# 4 вопрос
# Months = ('January', 'February', 'March', 'April', 'May', 'June',
#           'July', 'August', 'September', 'October', 'November', 'December')
#
# 5 вопрос
# было if i % 100 == 0:
# стало if i % 1000 == 0:
