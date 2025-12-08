# ============== 1 задание ====================

# базовый класс
# class animal:
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     def __str__(self):
#         return self.nickname
#
# класс кошки
# class cat(animal):
#     def __init__(self, nickname):
#         super().__init__(nickname)
#
#     def voice(self):
#         print("мяуууу")
#
#     def run(self):
#         print("бегу")

# класс попугая
# class parrot(animal):
#     def __init__(self, nickname):
#         super().__init__(nickname)
#
#     def voice(self):
#         print("карррр")
#
#     def fly(self):
#         print("лечу")


# ================ 2 задание ===================

class сообщение:
    def __init__(self, отправитель, получатель):
        self.отправитель = отправитель
        self.получатель = получатель

    def покажизаголовок(self):
        print(f"от {self.отправитель} к {self.получатель}:")

class текстовое_сообщение(сообщение):
    def __init__(self, отправитель, получатель, текст):
        super().__init__(отправитель, получатель)
        self.текст = текст

    def отправь(self):
        self.покажи_заголовок()
        print(self.текст)

class стикер_сообщение(сообщение):
    def __init__(self, отправитель, получатель, стикер):
        super().__init__(отправитель, получатель)
        self.стикер = стикер
        self.счетчик = 1

    def отправь(self):
        self.покажи_заголовок()
        print(f"{self.стикер} {self.счетчик}")
        self.счетчик += 1


# ================== 3 задание ================

# import random
#
# class msdice:
#     def __init__(self, грани):
#         self.facets = грани
#
#     def кинуть(self):
#         return random.randint(1, self.facets)
#
# d10 = msdice(10)
# print("бросок d10:", d10.кинуть())
# print("ещё раз d10:", d10.кинуть())
#
# d20 = msdice(20)
# print("бросок d20:", d20.кинуть())
# print("ещё разу d20:", d20.кинуть())


# ============== 4 задание ================

# class player:
#     # конструктор класса
#     def __init__(self, nickname):
#         self.nickname = nickname
#         self.exp_points = 0
#         self.inventory = []
#
#     # переопределяет строковое представление
#     def __str__(self):
#         return f"player {self.nickname} with {self.exp_points} exp and inventory {self.inventory}"
#
#     # добавляет указанное количество очков опыта.
#     def addexp(self, exp):
#         self.exp_points += exp
#
#     # добавляет предмет в инвентарь
#     def additem(self, item):
#         self.inventory.append(item)
#
#     # удаляет предмет из инвентаря, если он есть
#     def removeitem(self, item):
#         if item in self.inventory:
#             self.inventory.remove(item)


# ============== 5 заданиие ===================

# def parallel(r1, r2): return r1 * r2 / (r1 + r2)
# def consec(resistances): return sum(resistances)
