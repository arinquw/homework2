# ================================ 1 задание =========================
#
# ids = [103, 15, 17, 24]
# phones = [79028029311, 79124956827, 79223000257, 79197058606]
#
# while True:
#     print("\nменю:")
#     print("1. отсортировать по идентификационным кодам")
#     print("2. отсортировать по номерам телефона")
#     print("3. показать список пользователей")
#     print("4. выход")
#
#     choice = input("выберите пункт: ")
#
#     if choice == "1":
#         # сортировка по ids
#         for i in range(len(ids) - 1):
#             for j in range(i + 1, len(ids)):
#                 if ids[i] > ids[j]:
#                     ids[i], ids[j] = ids[j], ids[i]
#                     phones[i], phones[j] = phones[j], phones[i]
#         print("список отсортирован по ID.")
#
#     elif choice == "2":
#         # сортировка по телефону
#         for i in range(len(phones) - 1):
#             for j in range(i + 1, len(phones)):
#                 if phones[i] > phones[j]:
#                     phones[i], phones[j] = phones[j], phones[i]
#                     ids[i], ids[j] = ids[j], ids[i]
#         print("список отсортирован по телефонам")
#
#     elif choice == "3":
#         print("\nпользователи:")
#         for i in range(len(ids)):
#             print(ids[i], phones[i])
#
#     elif choice == "4":
#         print("выход")
#         break
#
#     else:
#         print("неверный выбор")

# ================================ 2 задание =========================

# Списки: названия книг и годы выпуска
titles = ["872 дня блокадного Ленинграда", "9 негритят", "Кладбище домашних животных", "Гарри Поттер и Тайная комната"]
years = [2000, 2022, 1977, 1967]

while True:
    print("\nменю:")
    print("1. отсортировать по названиям книг")
    print("2. отсортировать по годам выпуска")
    print("3. вывести список книг")
    print("4. выход")

    choice = input("выберите пункт: ")

    if choice == "1":
        # сортировка по названиям
        for i in range(len(titles) - 1):
            for j in range(i + 1, len(titles)):
                if titles[i] > titles[j]:
                    titles[i], titles[j] = titles[j], titles[i]
                    years[i], years[j] = years[j], years[i]
        print("Отсортировано по названиям книг.")

    elif choice == "2":
        # сортировка по годам выпуска
        for i in range(len(years) - 1):
            for j in range(i + 1, len(years)):
                if years[i] > years[j]:
                    years[i], years[j] = years[j], years[i]
                    titles[i], titles[j] = titles[j], titles[i]
        print("отсортировано по годам выпуска")

    elif choice == "3":
        print("\nсписок книг:")
        for i in range(len(titles)):
            print(titles[i], "-", years[i])

    elif choice == "4":
        print("выход из программы")
        break

    else:
        print("неверный пункт меню")
