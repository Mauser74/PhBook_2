from Models import PhoneBook
from View import cls, print_caption, text
import glob


class Menu:
    """Класс работы с меню"""
    def __init__(self, ph_book):
        # Структура главного меню
        self.main_menu = (
            "Телефонная книга", None,
            "Открыть телефонную книгу", self.__open_ph_book,
            "Сохранить телефонную книгу", self.__save_ph_book,
            "Сохранить телефонную книгу с новым именем", self.__save_as_ph_book,
            "Показать все контакты", self.__print_all_contacts,
            "Добавить контакт", self.__add_contact,
            "Найти контакт", self.__search_contact,
            "Изменить контакт", self.__change_contact,
            "Удалить контакт", self.__delete_contact,
            "Завершить работу", None
            )

        self.__ph_book = ph_book


    def __print_caption(self, f_pointer):
        print_caption(self.main_menu, f_pointer)


    def __open_ph_book(self) -> None:
        """Открытие файла телефонной книги"""
        cls()
        self.__print_caption(self.__open_ph_book)
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
                    self.__ph_book.set_filename(files_list[file_num])
                    # Открываем файл
                    self.__ph_book.open()
            return

    def __save_ph_book(self) -> None:
        """Сохраняем телефонную книгу в формате json"""
        cls()
        self.__print_caption(self.__save_ph_book)
        self.__ph_book.save()
        print(f'{text.save_complete}')
        input(f'{text.press_enter}')


    def __save_as_ph_book(self) -> None:
        """Сохраняем телефонную книгу под другим именем"""
        cls()
        self.__print_caption(self.__save_as_ph_book)
        new_filename = input(f'{text.save_as_filename}')

        if len(new_filename):
            # Имя не пустое
            if new_filename[-5:] != '.json':
                # Пользователь забыл указать расширение, добавим
                self.__ph_book.set_filename(new_filename + '.json')
            else:
                # С расширением всё нормально
                self.__ph_book.set_filename(new_filename)

            self.__ph_book.save()


    # Печать всех контактов
    def __print_all_contacts(self) -> None:
        cls()
        self.__print_caption(self.__print_all_contacts)
        for idx in range(self.__ph_book.get_size()):
            self.__print_contact(idx)
            print('-' * 20)
        input(f'{text.press_enter}')


    def __print_contact(self, idx: int) -> None:
        """Печать одного контакта

        :param idx: ID контакта в телефонной книге
        :type idx: int
        """
        contact = self.__ph_book.get_contact(idx)
        print(f'ID: {idx}\n{text.name}:\t\t\t{contact['name']}\n{text.phone}:\t{contact['phone']}\n{text.address}:\t\t\t{contact['address']}')


    def __add_contact(self) -> None:
        """Ввод нового контакта"""
        cls()
        self.__print_caption(self.__add_contact)

        while True:
            new_name = input(f'{text.enter_name}')

            if len(new_name):
                break
            else:
                cls()
                print(text.need_correct_data)

        phone = input(f'{text.enter_phone}')
        address = input(f'{text.enter_address}')
        self.__ph_book.add({'name': new_name, 'phone': phone, 'address': address})


    def __search_contact(self) -> None:
        """Запрос строки поиска и поиск по всем контактам с выводом результата"""
        cls()
        self.__print_caption(self.__search_contact)

        # Запрос строки для поиска
        substr = input(f'{text.enter_substr}: ')

        if len(substr):
            contacts = self.__ph_book.search(substr)

            if len(contacts):
                for contact_idx in contacts:
                    print('-' * 20)
                    self.__print_contact(contact_idx)
                print('-' * 20)
            else:
                print(f'{text.contact_not_found}')

        input(f'{text.press_enter}')


    def __change_contact(self) -> None:
        """Редактирование записи"""
        cls()
        self.__print_caption(self.__change_contact)
        contact_id = input(f'{text.enter_contact_id_edit}: ')

        if not len(contact_id):
            # Отказ редактировать запись
            return

        if contact_id.isdigit():
            contact_id = int(contact_id)
            if  0 <= contact_id < self.__ph_book.get_size():
                edited_contact = self.__ph_book.get_contact(contact_id)
                print(edited_contact['name'])
                name_of_contact = input(f'{text.enter_new_name}')

                if not len(name_of_contact):
                    # Новое имя контакта пустое, это отказ редактировать запись
                    return

                print(edited_contact['phone'])
                phone = input(f'{text.enter_new_phone}')
                print(edited_contact['address'])
                address = input(f'{text.enter_new_address}')
                self.__ph_book.set_contact(contact_id, {'name': name_of_contact, 'phone': phone, 'address': address})


    def __delete_contact(self) -> None:
        """Удаление контакта из телефонной книги"""
        cls()
        self.__print_caption(self.__delete_contact)
        contact_id = input(f'{text.enter_contact_id_delete}: ')

        if not len(contact_id):
            # Отказ удалять запись
            return

        if contact_id.isdigit():
            contact_id = int(contact_id)
            if 0 <= contact_id < self.__ph_book.get_size():
                self.__ph_book.del_contact(contact_id)


    def print_menu(self) -> None:
        """Печать и выбор пунктов меню"""
        while True:
            cls()
            for i in range(0, len(self.main_menu), 2):
                if i:
                    # Выводим пункты меню и нумеруем их
                    print(f'{i//2}. {self.main_menu[i]}')
                else:
                    # Выводим название меню и текущей телефонной книги
                    print(f'{self.main_menu[0]} {self.__ph_book.get_filename()}\n')
            # Ожидаем выбора пользователя
            select_function = self.__select_menu()
            if select_function:
                select_function()
            else:
                return


    def __select_menu(self):
        """Выбор пункта меню пользователем"""
        while True:
            menu_choice = input(text.input_menu)
            if menu_choice.isdigit() and 0 < int(menu_choice) < (len(self.main_menu) // 2):
                return self.main_menu[int(menu_choice) * 2 + 1]


# Объект - телефонная книга
book = PhoneBook('../PhBook.json')
# Объект - главное меню
main_menu = Menu(book)


# Начало программы
def run_program() -> None:
    main_menu.print_menu()