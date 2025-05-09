"""
6. (МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
"""

def get_list():
    while True:
        try:
            # Запрашиваем у пользователя ввод через один из разрешенных разделителей
            user_input = input("Введите элементы списка через запятую: ")

            # Разделяем строку на элементы по выбранному разделителю
            elements = user_input.split(',')

            # Преобразуем элементы в числа и сохраняем в список
            numbers = [int(element.strip()) for element in elements]
            break
        except ValueError:
            print("Ошибка ввода")

    return numbers

list1 = get_list()
list2 = get_list()

# Удаляем из первого списка элементы, которые есть во втором
result = [num for num in list1 if num not in list2]

# Выводим результат
print("Результат:", ", ".join(map(str, result)))