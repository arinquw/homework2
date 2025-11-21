# ====================== 1 задание ==================

import random

class Number:
    def __init__(self):
        # сформировать список случайных чисел
        self.grades = [random.randint(-5, 12) for _ in range(10)]

    def show_grades(self):
        print("Список оценок:", self.grades)

    def sort_grades(self):
        avg = sum(self.grades) / len(self.grades)
        if avg > 0:
            # сортируем первые три элемента списка по возрастанию
            self.grades[:3] = sorted(self.grades[:3])
        else:
            # сортируем только первый элемент
            self.grades[0] = sorted(self.grades[:1])

        # остальные элементы в обратном порядке
        self.grades[3:] = sorted(self.grades[3:], reverse=True)
        print("отсортированный список оценок:", self.grades)


# пример использования
number = Number()
number.show_grades()  # показываем исходный список оценок
number.sort_grades()  # сортируем и показываем отсортированный список


# ====================== 2 задание ==================
#
# class Number:
#     def __init__(self, grades):
#         self.grades = grades
#
#     def show_grades(self):
#         print("cписок оценок:", self.grades)
#
#     def retake_exam(self, index, new_grade):
#         self.grades[index] = new_grade
#
#     def check_scholarship(self):
#         avg = sum(self.grades) / len(self.grades)
#         if avg >= 10.7:
#             print("ура, стипендия.")
#         else:
#             print("лох, без стипендии остался.")
#
#     def sort_grades(self):
#         avg = sum(self.grades) / len(self.grades)
#         if avg > 0:
#             self.grades[:3] = sorted(self.grades[:3])
#         else:
#             self.grades[0] = sorted(self.grades[:1])
#         self.grades[3:] = sorted(self.grades[3:], reverse=True)
#         print("отсортированный список:", self.grades)
#
# # Пример данных
# grades = [8, 9, 6, 7, 11, 5, 12]
# number = Number(grades)
#
# while True:
#     print("\n1. показать оценки")
#     print("2. пересдать экзамен")
#     print("3. проверить стипендию")
#     print("4. выйти и отсортировать оценки")
#
#     choice = input("выберите действие: ")
#
#     if choice == '1':
#         number.show_grades()
#     elif choice == '2':
#         index = int(input("введите номер экзамена: "))
#         new_grade = int(input("введите новую оценку: "))
#         number.retake_exam(index, new_grade)
#     elif choice == '3':
#         number.check_scholarship()
#     elif choice == '4':
#         number.sort_grades()
#         break
#     else:
#         print("неверный выбор!")
#
#
#
# # ====================== 3 задание ==================
#
# # def bubble_sort(arr):
# #     for i in range(len(arr)):
# #         swapped = False
# #         for j in range(len(arr) - 1 - i):
# #             if arr[j] > arr[j + 1]:
# #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# #                 swapped = True
# #         if not swapped:
# #             break
# #     return arr
# #
# # # пример
# # arr = [64, 34, 25, 12, 22, 11, 90]
# # print(bubble_sort(arr))
