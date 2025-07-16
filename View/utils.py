from os import system, name


# Очистка экрана в консольном окне
def cls() -> None:
    """Очистка экрана в консоли в зависимости от операционной системы

    :return: -> None
    """
    if name == 'nt':                    # Для windows
        _ = system('cls')
    else:                               # Для mac и linux
        _ = system('clear')


# Печатаем заголовок меню выбранной функции
def print_caption(menu: (), f_pointer) -> None:
    """Получив указатель на функцию и список с пунктами меню печатает название меню относящегося к этой функции как заголовок

    :param menu:
    :param f_pointer: указатель на функцию
    :return: -> None
    """
    caption = menu[menu.index(f_pointer) - 1]
    print(f'{caption}\n' + '-' * len(caption))