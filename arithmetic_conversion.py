from os import system
import random
from console_ui import *
from correct_initialization import *


# Задача №3
def ui_arithmetic_conversion():
    """
    Функция реализующая пользовательский интерфейс в консоли для решения следующей задачи:
    Требуется проверить можно ли получить число из 3-го массива, арифметическими преобразованиями
    с числами двух других массивов. Числа проверяются последовательно.
    """
    # Массивы с числами
    first_array = []
    second_array = []
    third_array = []
    # Список результатов
    list_of_results = []
    while True:
        system('CLS')
        main_menu_item = main_menu_for_tasks(
            task_name='Логическое следствие элементов трех массивов.'
        )
        match main_menu_item:
            # Условие задачи
            case 1:
                system('CLS')
                print(
                    'Входные данные: три массива с числами. '
                    'Требуется проверить можно ли получить число из 3-го массива, '
                    'арифметическими преобразованиями с числами из двух других массивов. '
                    'Числа проверяются последовательно.'
                )
                system('PAUSE')

            # Ввод исходных данных
            case 2:
                # При вводе новых данных все предыдущие обнуляются
                first_array = []
                second_array = []
                third_array = []
                list_of_results = []
                system('CLS')
                while True:
                    initialization_item = ui_menu(
                        'Способ инициализации.\n'
                        '1. Вручную.\n'
                        '2. Автоматически.'
                    )
                    match initialization_item:
                        # Инициализация массивов точек вручную
                        case 1:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            ui_array_init(first_array)
                            print('Инициализация второго массива: ')
                            ui_array_init(second_array)
                            print('Инициализация третьего массива: ')
                            ui_array_init(third_array)
                            break

                        # Инициализация массивов точек случайным образом
                        case 2:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            auto_array_init(first_array)
                            print('Инициализация второго массива: ')
                            auto_array_init(second_array)
                            print('Инициализация третьего массива: ')
                            auto_array_init(third_array)
                            break

                        case _:
                            print_error_message('В меню всего 2 пункта. Попробуйте еще раз.')

                print('Инициализация массивов прошла успешно.')
                system('PAUSE')

            # Выполнение алгоритма
            case 3:
                system('CLS')
                if len(first_array) < 1 or len(second_array) < 1 or len(third_array) < 1:
                    print_error_message(
                        'Невозможно выполнить алгоритм, так как один или несколько массивов пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    list_of_results = arithmetic_conversion(first_array, second_array, third_array)
                    print('Алгоритм успешно выполнен!')
                    system('PAUSE')

            # Вывод результатов работы алгоритма
            case 4:
                system('CLS')
                if len(list_of_results) > 0:
                    print(
                        f"Результат работы алгоритма.\n"
                        f"Первый массив чисел: {' '.join(map(str, first_array))}\n"
                        f"Второй массив чисел: {' '.join(map(str, second_array))}\n"
                        f"Третий массив чисел: {' '.join(map(str, third_array))}\n"
                        f"Результат проверки: {' '.join(map(str, list_of_results))}"
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


def arithmetic_conversion(first_array, second_array, third_array):
    """
    Функция реализующая решение следующей задачи:
    Требуется проверить можно ли получить число из 3-го массива, арифметическими преобразованиями
    с числами двух других массивов. Числа проверяются последовательно.
    :param first_array: Первый массив чисел;
    :param second_array: второй массив чисел;
    :param third_array: третий массив чисел, который будет проверяться.
    :return: Список со строками в которых будет содержаться описание результатов проверки
    (можно или нельзя преобразовать).
    """
    list_of_results = ['' for i in range(len(third_array))]
    triples_of_numbers = enumerate(zip(first_array, second_array, third_array))
    for index, triple in triples_of_numbers:
        try:
            arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 % elem2, '%'
            )
            arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 / elem2, '/'
            )
            arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 ** elem2, '**'
            )
            arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 * elem2, '*'
            )
            arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 - elem2, '-'
            )
            arithmetic_operation(
                index, triple[0], triple[1], triple[2], list_of_results,
                lambda elem1, elem2: elem1 + elem2, '+'
            )
        except ZeroDivisionError:
            pass

    for i in range(len(list_of_results)):
        if list_of_results[i] == '':
            list_of_results[i] = f"Нет способов получить {i + 1}-й элемент."

    return list_of_results


def arithmetic_operation(index, elem1, elem2, elem3, list_of_results, func, function_symbol):
    if func(elem1, elem2) == elem3:
        if list_of_results[index] == '':
            list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                      f"{elem1} {function_symbol} {elem2} = {elem3};")
        else:
            list_of_results[index] += f"\n{elem1} {function_symbol} {elem2} = {elem3};"
    elif func(elem2, elem1) == elem3:
        if list_of_results[index] == '':
            list_of_results[index] = (f"Способы получить {index + 1}-й элемент: "
                                      f"{elem2} {function_symbol} {elem1} = {elem3};")
        else:
            list_of_results[index] += f"\n{elem2} {function_symbol} {elem1} = {elem3};"


def print_error_message(message):
    system('CLS')
    print(message)
    system('PAUSE')
    system('CLS')