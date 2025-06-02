# Телефонная книга. Домашнее задание 1
# Семенов Владимир

import glob
import json

from View import text


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


    def del_contact(self, idx: int) -> None:
        """Удаляет запись из телефонной книги

        :param idx: индекс удаляемой записи в телефонной книге
        :type idx: int
        """
        if 0 <= idx <= len(self._ph_book):
            del self._ph_book[idx]


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
