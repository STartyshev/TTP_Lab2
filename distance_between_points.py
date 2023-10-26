from os import system
from math import sqrt
import random
from console_ui import *


# Задача №2
def ui_distance_between_points():
    """
    Функция реализующая пользовательский интерфейс в консоли для поиска точек расстояние между,
    которыми больше заданного числа.
    """
    # Массивы с точками
    first_array_of_dots = []
    second_array_of_dots = []
    # Словарь в котором ключи - длины отрезков значения, которых больше заданного числа,
    # а значения - пары точек, которые эти отрезки образуют
    dict_of_segments_and_points = dict()
    # Заданное число с которым нужно сравнивать длину отрезков
    max_length = None
    # Флаг состояния
    algorithm_completed = False
    while True:
        system('CLS')
        main_menu_item = main_menu_for_tasks(
            task_name='Расстояние между точками.'
        )
        match main_menu_item:
            # Условие задачи
            case 1:
                system('CLS')
                print(
                    'Входные данные: два массива с точками и число. '
                    'Требуется вывести точки из первого и второго массивов, '
                    'расстояния между которыми больше заданного числа. '
                    'Расстояния считаются только для соответствующих чисел.'
                )
                system('PAUSE')

            # Ввод исходных данных
            case 2:
                # При вводе новых данных все предыдущие обнуляются
                first_array_of_dots = []
                second_array_of_dots = []
                dict_of_segments_and_points = dict()
                algorithm_completed = False
                system('CLS')
                max_length = input_correct_num(
                    left_value=1,
                    right_value=float('inf'),
                    input_message='Введите значение с которым нужно сравнивать длины отрезков: ',
                    error_message='Значение должно быть положительное. Попробуйте еще раз.',
                    type_of_number=float
                )
                while True:
                    system('CLS')
                    initialization_item = ui_menu(
                        'Способ инициализации массивов точек.\n'
                        '1. Вручную.\n'
                        '2. Автоматически.'
                    )
                    match initialization_item:
                        # Инициализация массивов точек вручную
                        case 1:
                            system('CLS')
                            print('Инициализация первого массива: ')
                            ui_array_of_dots_init(first_array_of_dots)
                            print('Инициализация второго массива: ')
                            ui_array_of_dots_init(second_array_of_dots)
                            break

                        # Инициализация массивов точек случайным образом
                        case 2:
                            system('CLS')
                            print('В каком пространстве будут находиться точки?\n'
                                  '1. На прямой.\n'
                                  '2. На плоскости.\n'
                                  '3. В трехмерном пространстве.')

                            space_selection = input_correct_num(
                                left_value=-float('inf'),
                                right_value=float('inf'),
                                input_message='Выберите пункт меню: ',
                                error_message='В меню всего 3 пункта. Попробуйте еще раз.',
                                type_of_number=int
                            )
                            print('Инициализация первого массива: ')
                            ui_auto_array_of_dots_init(first_array_of_dots, space_selection)
                            print('Инициализация второго массива: ')
                            ui_auto_array_of_dots_init(second_array_of_dots, space_selection)
                            break

                        case _:
                            print_error_message('В меню всего 2 пункта. Попробуйте еще раз.')

                print('Инициализация массивов прошла успешно.')
                system('PAUSE')

            # Выполнение алгоритма
            case 3:
                system('CLS')
                if len(first_array_of_dots) < 1 or len(second_array_of_dots) < 1:
                    print_error_message(
                        'Невозможно выполнить алгоритм, так как один или оба массива пустые. '
                        'Заполните массивы и попробуйте еще раз.'
                    )
                else:
                    dict_of_segments_and_points = distance_between_points(
                        first_array_of_dots,
                        second_array_of_dots,
                        max_length
                    )
                    algorithm_completed = True
                    print('Алгоритм успешно выполнен!')
                    system('PAUSE')

            # Вывод результатов работы алгоритма
            case 4:
                system('CLS')
                if algorithm_completed:
                    if len(dict_of_segments_and_points.keys()) < 1:
                        print(f"Алгоритм не нашел ни одной пары точек, которые образовали бы отрезок "
                              f"длиной больше {max_length}.")
                    else:
                        print(
                            f"Результат работы алгоритма.\n"
                            f"Первый массив точек: {' '.join(map(str, first_array_of_dots))}\n"
                            f"Второй массив точек: {' '.join(map(str, second_array_of_dots))}\n"
                            f"Список точек расстояние между которыми больше {max_length}: "
                        )
                        for key in dict_of_segments_and_points.keys():
                            print(f"Пара точек: {dict_of_segments_and_points[key]}; длина отрезка, "
                                  f"который они образуют: {round(key, 1)}.\n")
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


def ui_array_of_dots_init(array_of_dots):
    """
    Функция реализующая пользовательский интерфейс в консоли для инициализации массива точек вручную.
    :param array_of_dots: Массив точек для инициализации.
    """
    print('В каком пространстве будут находиться точки?\n'
          '1. На прямой.\n'
          '2. На плоскости.\n'
          '3. В трехмерном пространстве.')

    space_selection = input_correct_num(
        left_value=-float('inf'),
        right_value=float('inf'),
        input_message='Выберите пункт меню: ',
        error_message='В меню всего 3 пункта. Попробуйте еще раз.',
        type_of_number=int
    )
    while True:
        point_coordinates = []
        for i in range(space_selection):
            point_coordinates.append(
                input_correct_num(
                    left_value=-float('inf'),
                    right_value=float('inf'),
                    input_message=f"Введите {i + 1}-ю координату {len(array_of_dots) + 1}-й точки: ",
                    error_message='Координата должна быть числом. Попробуйте еще раз.',
                    type_of_number=float
                )
            )
        array_of_dots.append(tuple(point_coordinates))
        add_or_exit = input('Хотите добавить еще одну точку? Да / Нет: ')
        add_or_exit = add_or_exit.upper()
        while add_or_exit != 'ДА' and add_or_exit != 'НЕТ':
            print_error_message('Есть только два варианта ответа. '
                                'Попробуйте еще раз.')
            add_or_exit = input('Хотите добавить еще одну точку? Да / Нет: ')
            add_or_exit = add_or_exit.upper()

        if add_or_exit == 'НЕТ':
            return


def ui_auto_array_of_dots_init(array_of_dots, space_selection):
    """
    Функция реализующая пользовательский интерфейс в консоли для автоматической инициализации массива точек.
    :param array_of_dots: Массив точек для инициализации;
    :param space_selection: размерность пространства в котором будут находиться точки.
    """
    size_of_array = input_correct_num(
        left_value=1,
        right_value=50,
        input_message='Введите размер массива точек, который хотите заполнить автоматически: ',
        error_message='Размер массива должен быть больше 0 и меньше или равен 50. '
                      'Попробуйте еще раз.',
        type_of_number=int
    )

    for i in range(size_of_array):
        array_of_dots.append(
            tuple(
                round(random.random() * 10 * ((-1) ** random.randint(1, 2)), 1) for j in range(space_selection)
            )
        )


def distance_between_points(first_array_of_dots, second_array_of_dots, distance):
    """
    Функция поиска точек расстояние между которыми больше заданного.
    :param first_array_of_dots: Первый массив точек;
    :param second_array_of_dots: второй массив точек;
    :param distance: заданное расстояние с которым будут сравниваться длины отрезков двух точек взятых
    из первого и второго массивов.
    :return: Возвращает словарь где ключи - длины отрезков которые больше заданного числа, а значения - пара точек,
    которые эти отрезки образуют.
    """
    return {
        segment_length(dot1, dot2): [dot1, dot2]
        for dot1, dot2 in zip(first_array_of_dots, second_array_of_dots)
        if segment_length(dot1, dot2) > distance
    }


def segment_length(dot1, dot2):
    """
    :param dot1: Первая точка;
    :param dot2: вторая точка.
    :return: Возвращает длину отрезка образованного двумя точками.
    """
    return sqrt(
        sum(
            (c1 - c2) ** 2 for c1, c2 in zip(dot1, dot2)
        )
    )


def print_error_message(message):
    system('CLS')
    print(message)
    system('PAUSE')
    system('CLS')


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