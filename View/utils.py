from os import system, name


# Очистка экрана в консольном окне
def cls() -> None:
    if name == 'nt':                    # Для windows
        _ = system('cls')
    else:                               # Для mac и linux
        _ = system('clear')


# Печатаем заголовок меню выбранной функции
def print_caption(f_pointer) -> None:
    caption = main_menu[main_menu.index(f_pointer) - 1]
    print(f'{caption}\n' + '-' * len(caption))