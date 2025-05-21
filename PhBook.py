# Телефонная книга. Домашнее задание 1
# Семенов Владимир

import text                             # Модуль со строками
import glob
from os import system, name
import json


#Глобальные переменные
filename_of_book = 'PhBook.json'        # Файл телефонной книги
ph_book = []


# Очистка экрана в консольном окне
def cls():
    if name == 'nt':                    # Для windows
        _ = system('cls')
    else:                               # Для mac и linux
        _ = system('clear')


# Печатаем заголовок меню выбранной функции
def print_caption(f_pointer):
    caption = main_menu[main_menu.index(f_pointer) - 1]
    print(f'{caption}\n' + '-' * len(caption))


# Открытие файла телефонной книги
def open_ph_book():
    cls()
    print_caption(open_ph_book)
    global ph_book, filename_of_book
    # Получаем список файлов
    files_list = glob.glob('*.json')

    if len(files_list) == 0:
        # Список файлов телефонной книги пуст
        print(f'{text.no_files}')
        input(f'{text.press_enter}')
        return

    for i in range(0, len(files_list)):
        # Выводим список файлов
        print(f'{i+1} {files_list[i]}')

    # Запрос номера файла
    while True:
        file_num = input(f'\n{text.input_file} (1 - {len(files_list)}): ')

        if len(file_num):
            # Номер файла выбран
            if file_num.isdigit() and 0 <= (int(file_num) - 1) < (len(files_list)):
                # Номер файла корректный
                file_num = int(file_num) - 1
                filename_of_book = files_list[file_num]
                # Открываем файл
                with open(filename_of_book, 'r', encoding='utf-8') as ph_book_file:
                    ph_book = json.load(ph_book_file)
                return
        else:
            # Отказ от открытия файла
            return


# Сохраняем телефонную книгу в формате json
def save_ph_book():
    cls()
    print_caption(save_ph_book)
    save_file(filename_of_book)
    print(f'{text.save_complete}')
    input(f'{text.press_enter}')


# Сохранить телефонную книгу под другим именем
def save_as_ph_book():
    cls()
    print_caption(save_as_ph_book)
    global filename_of_book
    new_filename = input(f'{text.save_as_filename}')

    if len(new_filename):
        # Имя не пустое
        if new_filename[-5:] != '.json':
            # Пользователь забыл указать расширение, добавим
            filename_of_book = new_filename + '.json'
        else:
            # С расширением всё нормально
            filename_of_book = new_filename
        save_file(filename_of_book)


# Сохраняет файл телефонной книги под именем filename
def save_file(filename):
    with open(filename, 'w', encoding = 'utf-8') as ph_book_file:
        json.dump(ph_book, ph_book_file, indent = 4, ensure_ascii = False)


# Печать всех контактов
def print_all_contacts():
    cls()
    print_caption(print_all_contacts)
    for idx, contact in enumerate(ph_book):
        print_contact(idx)
        print('-' * 20)
    input(f'{text.press_enter}')


# Печать одного контакта
def print_contact(idx):
    cnt = ph_book[idx]
    print(f'ID: {idx}\n{text.name}:\t\t\t{cnt['name']}\n{text.phone}:\t{cnt['phone']}\n{text.address}:\t\t\t{cnt['address']}')


# Ввод нового контакта
def add_contact():
    cls()
    print_caption(add_contact)
    global ph_book

    while True:
        new_name = input(f'{text.enter_name}')

        if len(new_name):
            break
        else:
            cls()
            print(text.need_correct_data)

    phone = input(f'{text.enter_phone}')
    address = input(f'{text.enter_address}')
    ph_book.append({'name': new_name, 'phone': phone, 'address': address})


# Поиск контактов
def find_contact():
    cls()
    print_caption(find_contact)

    while True:
        # Запрос строки для поиска
        substr = input(f'{text.enter_substr}: ')

        if len(substr):
            for idx, contact in enumerate(ph_book):
                for i, element in enumerate(list(contact.values())):
                    if element.find(substr) >= 0:
                        print('-' * 20)
                        print_contact(idx)
                        break
            print('-' * 20)
        else:
            break


# Редактирование записи
def change_contact():
    cls()
    print_caption(change_contact)
    global ph_book
    contact_id = input(f'{text.enter_contact_id_edit}: ')

    if not len(contact_id):
        # Отказ редактировать запись
        return

    if contact_id.isdigit() and 0 <= int(contact_id) < (len(ph_book)):
        contact_id = int(contact_id)
        print(ph_book[contact_id]['name'])
        name_of_contact = input(f'{text.enter_new_name}')

        if not len(name_of_contact):
            # Новое имя контакта пустое, это отказ редактировать запись
            return

        print(ph_book[contact_id]['phone'])
        phone = input(f'{text.enter_new_phone}')
        print(ph_book[contact_id]['address'])
        address = input(f'{text.enter_new_address}')
        ph_book[contact_id] = ({'name': name_of_contact, 'phone': phone, 'address': address})


# Удалить контакт
def delete_contact():
    cls()
    print_caption(delete_contact)
    global ph_book
    contact_id = input(f'{text.enter_contact_id_delete}: ')

    if not len(contact_id):
        # Отказ удалять запись
        return

    if contact_id.isdigit() and 0 <= int(contact_id) < (len(ph_book)):
        contact_id = int(contact_id)
        del ph_book[contact_id]
        print(ph_book)


# Структура главного меню
main_menu = ("Телефонная книга",                                None,
             "Открыть телефонную книгу",                        open_ph_book,
             "Сохранить телефонную книгу",                      save_ph_book,
             "Сохранить телефонную книгу с новым именем",       save_as_ph_book,
             "Показать все контакты",                           print_all_contacts,
             "Добавить контакт",                                add_contact,
             "Найти контакт",                                   find_contact,
             "Изменить контакт",                                change_contact,
             "Удалить контакт",                                 delete_contact,
             "Завершить работу",                                None
             )


# Функция печати и выбора пунктов меню
def print_menu(menu):
    while True:
        cls()
        for i in range(0, len(menu), 2):
            if i:
                # Выводим пункты меню и нумеруем их
                print(f'{i//2}. {menu[i]}')
            else:
                # Выводим название меню и текущей телефонной книги
                print(f'{menu[0]} {filename_of_book}\n')
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


# Начало программы
def run_program():
    print_menu(main_menu)
