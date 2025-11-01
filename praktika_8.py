# =============================== 1 задание ==============================

points_to_letters = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'С', 'Т'],
    2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
    3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
    4: ['F', 'H', 'V', 'W', 'Y', 'Й', 'Р', 'Ы'],
    5: ['K', 'Ж', 'З', 'Ч', 'Ц'],
    8: ['J', 'X', 'Ш', 'Э', 'Ю', 'Х'],
    10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
}


dictionnary = points_to_letters

gamers = {}  # словарь игрока

count_user = int(input("сколько человек будет играть?:"))
for i in range(count_user):
    name = input("введите имя игрока:").strip()
    if not name:
        name = f"Игрок_{i+1}"
    gamers[name] = 0

print(f"список игроков: \n{gamers}")

# 10 раундов
for raund in range(10):
    for gamer in gamers.keys():
        print("*"*11)
        print(f"ходит игрок {gamer}")
        answer = input("введите слово:").strip().upper()
        for i in answer:
            for key, value in dictionnary.items():
                if i in value:
                    gamers[gamer] += key
                    break  # чтобы не начислять очки дважды

print("игра окончена! \n таблица игроков:")
for key, value in gamers.items():
    print(f"{key} -> {value} баллов")

result_user = ''
result_value = -1
for key, value in gamers.items():
    if result_value < value:
        result_value = value
        result_user = key

print(f"победитель: {result_user}")


# =============================== 2 задание ==============================

backpack = {'зажигалка':20, 'компас':100, 'фрукты':500, 'рубашка':300,
            'термос':1000, 'аптечка':200, 'куртка':600, 'бинокль':400,
            'удочка':1300, 'салфетки':40, 'бутерброды':800, 'палатка':5500,
            'спальный мешок':2500, 'изолента':250, 'котел':3000
}

max_mass = int(input("введите максимальный вес для похода: "))
curr_mass = 0  # одна переменная

while curr_mass < max_mass:
    print(backpack)
    answer = input("что вы хотите взять с собой: ").strip().lower()
    if answer in backpack:              # проверяем, что предмет существует
        curr_mass += backpack[answer]   # добавляем вес
    else:
        print("такого предмета нет")

print(f"рюкзак заполнен, текущая масса: {curr_mass}")


# =============================== 3 задание ==============================

contacts = {
    "Иван": {
        "телефон": "+48 600 000 001",
        "ютюб": "https://youtube.com/@ivan",
        "вк": "https://vk.com/ivan",
        "телеграм": "https://t.me/ivan"
    },
    "Мария": {
        "телефон": "+48 600 000 002",
        "ютюб": "https://youtube.com/@maria",
        "вк": "https://vk.com/maria",
        "телеграм": "https://t.me/maria"
    }
}

name = input("Введите имя контакта: ")

if name in contacts:
    info = contacts[name]
    print("Телефон:", info["телефон"])
    print("YouTube:", info["ютюб"])
    print("VK:", info["вк"])
    print("Telegram:", info["телеграм"])
else:
    print("Контакт не найден.")
