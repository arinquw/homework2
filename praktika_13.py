# ================================ 1 задание =========================
# 
# def linear_search(arr, target):
#     for i, value in enumerate(arr):
#         if value == target:
#             return i
#     return -1
# 
# 
# def main_task1():
#     list1 = [5, 2, 8, 1, 9]
#     list2 = [4, 7, 2, 6, 4]
#     list3 = [10, 15, 12, 11]
#     list4 = [22, 18, 16, 14, 13]
# 
#     print("список 1:", list1)
#     print("список 2:", list2)
#     print("список 3:", list3)
#     print("список 4:", list4)
# 
# 
#     combined_list = list1 + list2 + list3 + list4
#     print("\nобъединенный список:", combined_list)
# 
# 
#     while True:
#         order = input("\nвыберите сортировку 1) по возрастанию, 2) по убыванию: ")
#         if order in ['1', '2']:
#             break
#         print("выберете 1 или 2")
# 
# 
#     if order == '1':
#         combined_list.sort()
#         print("отсортировано по возрастанию:", combined_list)
#     else:
#         combined_list.sort(reverse=True)
#         print("отсортировано по убыванию:", combined_list)
# 
# 
#     try:
#         search_value = int(input("\nвведите значение для поиска: "))
#         index = linear_search(combined_list, search_value)
# 
#         if index != -1:
#             print(f"значение {search_value} найдено на позиции {index + 1}")
#         else:
#             print(f"значение {search_value} не найдено в списке")
#     except ValueError:
#         print("ошибка")
# 
# 
# 
# main_task1()


#================================= 2 задание =========================
# 
# def binary_search(arr, target):
# 
#     left, right = 0, len(arr) - 1
# 
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# 
# 
# def get_unique_elements(*lists):
# 
#     all_elements = []
#     for lst in lists:
#         all_elements.extend(lst)
# 
# 
#     unique_elements = []
#     for element in all_elements:
#         if all_elements.count(element) == 1:
#             unique_elements.append(element)
# 
#     return unique_elements
# 
# 
# def main_task2():
# 
#     list1 = [5, 2, 8, 1, 9, 100]
#     list2 = [3, 7, 2, 6, 4, 100]
#     list3 = [10, 15, 12, 11, 200]
#     list4 = [20, 18, 16, 14, 13, 300]
# 
#     print("список 1:", list1)
#     print("список 2:", list2)
#     print("список 3:", list3)
#     print("список 4:", list4)
# 
# 
#     unique_list = get_unique_elements(list1, list2, list3, list4)
#     print("\nуникальные элементы:", unique_list)
# 
#     if not unique_list:
#         print("нет уникальных элементов!")
#         return
# 
# 
#     while True:
#         order = input("\nвыберите сортировку 1) по возрастанию, 2) по убыванию: ")
#         if order in ['1', '2']:
#             break
#         print("введите 1 или 2")
# 
# 
#     if order == '1':
#         unique_list.sort()
#         print("отсортировано по возрастанию:", unique_list)
#     else:
#         unique_list.sort(reverse=True)
#         print("отсортировано по убыванию:", unique_list)
# 
# 
#     try:
#         search_value = int(input("\nвведите значение для поиска: "))
# 
#         search_list = unique_list.copy()
#         if order == '2':
#             search_list.sort()
# 
#         index = binary_search(search_list, search_value)
# 
#         if index != -1:
# 
#             if order == '1':
#                 actual_index = index
#             else:
#                 actual_index = len(unique_list) - 1 - index
# 
#             print(f"значение {search_value} найдено на позиции {actual_index + 1}")
#             print(f"cписок: {unique_list}")
#         else:
#             print(f"значение {search_value} не найдено в списке")
#     except ValueError:
#         print("ошибка, введите целое число")
# 
# main_task2()
