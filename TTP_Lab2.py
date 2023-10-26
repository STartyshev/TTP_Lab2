from os import system
from number_of_common_numbers import *
from distance_between_points import *
from arithmetic_conversion import *


def main():
    while True:
        task_selection_item = ui_menu(
            'Меню выбора задания.\n'
            '1. Проверка двух массивов на количество общих чисел.\n'
            '2. Расстояние между точками.\n'
            '3. Логическое следствие элементов трех массивов.\n'
            '4. Выход из программы.'
        )

        match task_selection_item:
            case 1:
                ui_number_of_common_numbers()

            case 2:
                ui_distance_between_points()

            case 3:
                ui_arithmetic_conversion()

            case 4:
                system('CLS')
                return

            case _:
                print_error_message('В меню всего 4 пункта. Попробуйте еще раз.')


if __name__ == '__main__':
    main()
