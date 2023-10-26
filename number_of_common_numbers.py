from os import system
import random
from console_ui import *


def ui_array_init(array: list):
    """
    Функция для инициализации массива числами вручную.
    :param array: Массив для инициализации.
    """
    while True:
        elem_or_exit = input('Введите число, которое хотите добавить в массив (для выхода введите - выход): ')
        if elem_or_exit.upper() == 'ВЫХОД':
            return
        else:
            try:
                elem_or_exit = float(elem_or_exit)
                array.append(elem_or_exit)
            except ValueError:
                print_error_message('Введенное значение не является числом или ключевым словом "выход". '
                                    'Попробуйте еще раз.')


def auto_array_init(array):
    """
    Функция для инициализации массива числами автоматически.
    :param array: Массив для инициализации.
    """
    n = input_correct_num(
        left_value=1,
        right_value=50,
        input_message='Введите размер массива: ',
        error_message='Размер массива должен принимать целочисленное значение и быть больше нуля '
                      'и меньше или равен 50. Попробуйте еще раз.',
        type_of_number=int
    )
    for i in range(n):
        array.append(round(random.random() * 10 * ((-1) ** random.randint(1, 2)), 1))


# Задача №1
def ui_number_of_common_numbers():
    """
    Функция реализующая пользовательский интерфейс в консоли для поиска кол-ва общих чисел в двух массивах.
    """
    # Два массива в которых будет осуществляться поиск общих чисел
    first_array = []
    second_array = []
    # Количество общих чисел двух массивов
    num_of_common_numbers = None
    while True:
        system('CLS')
        main_menu_item = main_menu_for_tasks(
            task_name='Проверка двух массивов на количество общих чисел.'
        )

        match main_menu_item:
            # Условие задачи
            case 1:
                system('CLS')
                print(
                    'Входные данные: два массива с числами. Требуется проверить сколько у массивов общих чисел. '
                    'Также число будет считаться общим если оно входит в один массив, а в другом массиве находится '
                    'его перевернутая версия.'
                )
                system('PAUSE')

            # Ввод исходных данных
            case 2:
                first_array = []
                second_array = []
                system('CLS')
                while True:
                    initialization_item = ui_menu(
                        'Способ инициализации.\n'
                        '1. Вручную.\n'
                        '2. Автоматически.'
                    )
                    match initialization_item:
                        # Инициализация массивов вручную
                        case 1:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            ui_array_init(first_array)
                            print('Инициализация второго массива: ')
                            ui_array_init(second_array)
                            break

                        # Инициализация массивов случайным образом
                        case 2:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            auto_array_init(first_array)
                            print('Инициализация второго массива: ')
                            auto_array_init(second_array)
                            break

                        case _:
                            print_error_message('В меню всего 2 пункта. Попробуйте еще раз.')

                print('Инициализация массивов прошла успешно.')
                system('PAUSE')

            # Выполнение алгоритма
            case 3:
                system('CLS')
                if len(first_array) < 1 or len(second_array) < 1:
                    print_error_message(
                        'Невозможно выполнить алгоритм, так как один или оба массива пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    num_of_common_numbers = number_of_common_numbers(first_array, second_array)
                    print('Алгоритм успешно выполнен!')
                    system('PAUSE')

            # Вывод результатов работы алгоритма
            case 4:
                system('CLS')
                if num_of_common_numbers is not None:
                    print(
                        f"Результат работы алгоритма.\n"
                        f"Первый массива: {' '.join(map(str, first_array))}\n"
                        f"Второй массив: {' '.join(map(str, second_array))}\n"
                        f"Количество общих чисел в обоих массивах: {num_of_common_numbers}"
                    )
                    system('PAUSE')
                else:
                    print_error_message(
                        'Невозможно вывести результат работы алгоритма, так как алгоритм не был выполнен. '
                        'Запустите работу алгоритма и попробуйте еще раз.'
                    )

            # Выход в главное меню
            case 5:
                break

            case _:
                print_error_message('В меню всего 5 пунктов. Попробуйте еще раз.')


def number_of_common_numbers(first_array, second_array):
    """
    Функция находит количество общих чисел в двух массивах.
    Также, число считается общим если оно входит в один массив, а в другом
    находится его перевернутая версия.
    :param first_array: Первый массив чисел;
    :param second_array: второй массив чисел.
    :return: Возвращает количество общих чисел двух массивов.
    """
    num_of_common_numbers = 0
    list_of_common_numbers = []
    for elem in first_array:
        if ((str(elem) in list(map(str, second_array)) or str(elem)[::-1] in list(map(str, second_array))) and
                elem not in list_of_common_numbers):
            num_of_common_numbers += 1
            list_of_common_numbers.append(elem)
    return num_of_common_numbers


def input_correct_num(left_value, right_value, input_message, error_message, type_of_number):
    """
    Функция реализующая ввод пользователем корректного числа входящего в заданный диапазон.
    :param left_value: Левая граница диапазона;
    :param right_value: правая граница диапазона;
    :param input_message: сообщение-приглашение на ввод числа;
    :param error_message: сообщение о том, что число не входит в диапазон и нужно ввести новое;
    :param type_of_number: тип числа, которое нужно вводить пользователю.
    :return: Возвращает корректное число введенное пользователем.
    """
    while True:
        while True:
            try:
                num = type_of_number(input(input_message))
                break
            except ValueError:
                print('Введенное значение должно являться числом! '
                      'Попробуйте еще раз.')

        if num < left_value or num > right_value:
            print(error_message)
        else:
            return num


def print_error_message(message):
    system('CLS')
    print(message)
    system('PAUSE')
    system('CLS')