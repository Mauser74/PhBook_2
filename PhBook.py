# Телефонная книга. Домашнее задание 1
# Семенов Владимир
from typing import Callable, Tuple

import text                             # Модуль со строками
import glob
from os import system, name
import json


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



class PhoneBook:
    """Класс телефонной книги формата .json"""

    # Телефонная книга в виде списка
    _ph_book = []


    def __init__(self, filename: str) -> None:
        """Инициализация класса

        :param filename: Имя файла телефонной книги задаваемой по-умолчанию
        :type filename: str
        """
        self._filename = filename


    def set_filename(self, filename: str) -> None:
        """Сеттер имени файла телефонной книги

        :param filename: Имя файла телефонной книги задаваемой по-умолчанию
        :type filename: str
        """
        self._filename = filename


    def get_filename(self) -> str:
        """Геттер имени файла телефонной книги с которой работаем

        :return: имя файла телефонной книги с которой работаем
        :rtype: str
        """
        return self._filename


    def get_size(self) -> int:
        """Геттер числа контактов в телефонной книге

        :return: число контактов в телефонной книге
        :rtype: int
        """
        return len(self._ph_book)


    def get_contact(self, idx: int) -> {}:
        """Геттер записи из телефонной книги

        :param idx: индекс записи в телефонной книге
        :type idx: int

        :return: словарь с записью
        :rtype: {}
        """
        if 0 <= idx <= len(self._ph_book):
            return self._ph_book[idx]
        else:
            return None


    def set_contact(self, idx: int, contact: {}) -> None:
        """Записывает по существующему ID данные контакта

        :param idx:
        :type idx: int
        :param contact:
        :type contact: {}
        """
        if idx < self.get_size():
            self._ph_book[idx] = contact


    def open(self) -> None:
        """Открываем файл телефонной книги и читаем его"""
        with open(self._filename, 'r', encoding='utf-8') as ph_book_file:
            self._ph_book = json.load(ph_book_file)


    def save(self) -> None:
        """Сохраняем телефонную книгу в формате json"""
        with open(self._filename, 'w', encoding='utf-8') as ph_book_file:
            json.dump(self._ph_book, ph_book_file, indent=4, ensure_ascii=False)


    def add(self, contact: {}) -> None:
        """Добавление нового контакта в телефонную книгу

        :param contact: словарь с новым контактом
        :type contact: {}
        """
        self._ph_book.append(contact)


    def search(self, search_str: str)->[int]:
        """Поиск в записях по строке по всем полям телефонной книги

        :param search_str: строка для поиска
        :type search_str: str

        :return: список индексов контактов, где найдено совпадение
        :rtype: [int]
        """
        # Список индексов записи с результатами поиска
        contacts = []

        if len(search_str):
            # Строка для поиска не пустая
            for idx, contact in enumerate(self._ph_book):
                # Перебираем все контакты в телефонной книге
                for i, element in enumerate(list(contact.values())):
                    # Ищем совпадение строки поиска во всех элементах записи
                    if element.find(search_str) >= 0:
                        # Найдено совпадение, добавим в список индекс
                        contacts.append(idx)
                        break

        return contacts


def open_ph_book() -> None:
    """Открытие файла телефонной книги"""
    cls()
    print_caption(open_ph_book)
    global ph_book
    # Получаем список файлов
    files_list = glob.glob('*.json')

    if len(files_list) == 0:
        # Список файлов телефонной книги пуст
        print(f'{text.files_not_found}')
        input(f'{text.press_enter}')
        return

    for i in range(0, len(files_list)):     # !!! Заменить на enumerate
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
                # Имя файла открываемой телефонной книги
                ph_book.set_filename(files_list[file_num])
                # Открываем файл
                ph_book.open()
        return


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
    global ph_book
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
ph_book = PhoneBook('PhBook.json')


# Начало программы
def run_program():
    print_menu(main_menu)
