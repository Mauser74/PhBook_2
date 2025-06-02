from Models import PhoneBook


def save_ph_book() -> None:
    """Сохраняем телефонную книгу в формате json"""
    cls()
    print_caption(save_ph_book)
    ph_book.save()
    print(f'{text.save_complete}')
    input(f'{text.press_enter}')


def save_as_ph_book() -> None:
    """Сохраняем телефонную книгу под другим именем"""
    cls()
    print_caption(save_as_ph_book)
    new_filename = input(f'{text.save_as_filename}')

    if len(new_filename):
        # Имя не пустое
        if new_filename[-5:] != '.json':
            # Пользователь забыл указать расширение, добавим
            ph_book.set_filename(new_filename + '.json')
        else:
            # С расширением всё нормально
            ph_book.set_filename(new_filename)

        ph_book.save()


# Печать всех контактов
def print_all_contacts() -> None:
    cls()
    print_caption(print_all_contacts)
    for idx in range(ph_book.get_size()):
        print_contact(idx)
        print('-' * 20)
    input(f'{text.press_enter}')


def print_contact(idx: int) -> None:
    """Печать одного контакта

    :param idx: ID контакта в телефонной книге
    :type idx: int
    """
    contact = ph_book.get_contact(idx)
    print(f'ID: {idx}\n{text.name}:\t\t\t{contact['name']}\n{text.phone}:\t{contact['phone']}\n{text.address}:\t\t\t{contact['address']}')


def add_contact() -> None:
    """Ввод нового контакта"""
    cls()
    print_caption(add_contact)

    while True:
        new_name = input(f'{text.enter_name}')

        if len(new_name):
            break
        else:
            cls()
            print(text.need_correct_data)

    phone = input(f'{text.enter_phone}')
    address = input(f'{text.enter_address}')
    ph_book.add({'name': new_name, 'phone': phone, 'address': address})


def search_contact() -> None:
    """Запрос строки поиска и поиск по всем контактам с выводом результата"""
    cls()
    print_caption(search_contact)

    # Запрос строки для поиска
    substr = input(f'{text.enter_substr}: ')

    if len(substr):
        contacts = ph_book.search(substr)

        if len(contacts):
            for contact_idx in contacts:
                print('-' * 20)
                print_contact(contact_idx)
            print('-' * 20)
        else:
            print(f'{text.contact_not_found}')

    input(f'{text.press_enter}')


def change_contact() -> None:
    """Редактирование записи"""
    cls()
    print_caption(change_contact)
    contact_id = input(f'{text.enter_contact_id_edit}: ')

    if not len(contact_id):
        # Отказ редактировать запись
        return

    if contact_id.isdigit():
        contact_id = int(contact_id)
        if  0 <= contact_id < ph_book.get_size():
            edited_contact = ph_book.get_contact(contact_id)
            print(edited_contact['name'])
            name_of_contact = input(f'{text.enter_new_name}')

            if not len(name_of_contact):
                # Новое имя контакта пустое, это отказ редактировать запись
                return

            print(edited_contact['phone'])
            phone = input(f'{text.enter_new_phone}')
            print(edited_contact['address'])
            address = input(f'{text.enter_new_address}')
            ph_book.set_contact(contact_id, {'name': name_of_contact, 'phone': phone, 'address': address})


# Удалить контакт
def delete_contact() -> None:
    """Удаление контакта из телефонной книги"""
    cls()
    print_caption(delete_contact)
    contact_id = input(f'{text.enter_contact_id_delete}: ')

    if not len(contact_id):
        # Отказ удалять запись
        return

    if contact_id.isdigit():
        contact_id = int(contact_id)
        if 0 <= contact_id < ph_book.get_size():
            ph_book.del_contact(contact_id)


# Структура главного меню
main_menu = ("Телефонная книга", None,
             "Открыть телефонную книгу", open_ph_book,
             "Сохранить телефонную книгу", save_ph_book,
             "Сохранить телефонную книгу с новым именем", save_as_ph_book,
             "Показать все контакты", print_all_contacts,
             "Добавить контакт", add_contact,
             "Найти контакт", search_contact,
             "Изменить контакт", change_contact,
             "Удалить контакт", delete_contact,
             "Завершить работу", None
             )


# Функция печати и выбора пунктов меню
def print_menu(menu) -> None:
    while True:
        cls()
        for i in range(0, len(menu), 2):
            if i:
                # Выводим пункты меню и нумеруем их
                print(f'{i//2}. {menu[i]}')
            else:
                # Выводим название меню и текущей телефонной книги
                print(f'{menu[0]} {ph_book.get_filename()}\n')
        # Ожидаем выбора пользователя
        select_function = select_menu(menu)
        if select_function:
            select_function()
        else:
            return


# Выбор пункта меню пользователем
def select_menu(menu):
    while True:
        menu_choice = input(text.input_menu)
        if menu_choice.isdigit() and 0 < int(menu_choice) < (len(menu) // 2):
            return menu[int(menu_choice) * 2 + 1]


# Объект - телефонная книга
ph_book = PhoneBook('../PhBook.json')


# Начало программы
def run_program() -> None:
    print_menu(main_menu)