# Телефонная книга. Домашнее задание 1
# Семенов Владимир

import json

from Models import Contact
from View import text, press_enter


class PhoneBook:
    """Класс телефонной книги формата .json"""
    def __init__(self) -> None:
        """Инициализация класса

        :return: -> None
        """
        self._filename = ""
        # Телефонная книга в виде списка
        self._ph_book = []


    def clear_all(self) -> None:
        """Удаление всех записей из телефонной книги

        :return: None
        """
        self._ph_book.clear()


    def set_filename(self, filename: str) -> None:
        """Сеттер имени файла телефонной книги

        :param filename: Имя файла телефонной книги задаваемой по-умолчанию
        :type filename: str
        :return: -> None
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


    def get_contact(self, idx: int) -> (dict, None):
        """Геттер записи из телефонной книги

        :param idx: индекс записи в телефонной книге
        :type idx: int

        :return: словарь с записью
        :rtype: (dict, None)
        """
        if 0 <= idx <= len(self._ph_book):
            return self._ph_book[idx]
        else:
            return None


    def del_contact(self, idx: int) -> None:
        """Удаляет запись из телефонной книги

        :param idx: индекс удаляемой записи в телефонной книге
        :type idx: int
        :return: -> None
        """
        if 0 <= idx <= len(self._ph_book):
            del self._ph_book[idx]


    def set_contact(self, idx: int, contact: {}) -> None:
        """Записывает по существующему ID данные контакта

        :param idx:
        :type idx: int
        :param contact:
        :type contact: {}
        :return: -> None
        """
        if idx < self.get_size():
            self._ph_book[idx] = contact


    def open(self) -> None:
        """Открываем файл телефонной книги и читаем его

        :return: -> None
        """
        try:
            with open(self._filename, 'r', encoding='utf-8') as ph_book_file:
                # self._ph_book = json.load(ph_book_file)
                data = json.load(ph_book_file)
                self._ph_book = [Contact.from_dict(contact_data) for contact_data in data]
        except OSError:
            print(f"{text.file_open_error}")
            press_enter()


    def save(self) -> None:
        """Сохраняем телефонную книгу в формате json

        :return: -> None
        """
        try:
            data = [contact.to_dict() for contact in self._ph_book]
            with open(self._filename, 'w', encoding='utf-8') as ph_book_file:
                json.dump(self._ph_book, ph_book_file, indent=4, ensure_ascii=False)
        except OSError:
            print(f"{text.file_save_error}")
            press_enter()


    def add(self, contact: Contact) -> None:
        """Добавление нового контакта в телефонную книгу

        :param contact: словарь с новым контактом
        :type contact: Contact
        :return: -> None
        """
        self._ph_book.append(contact)


    def search(self, search_str: str) -> [int]:
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
