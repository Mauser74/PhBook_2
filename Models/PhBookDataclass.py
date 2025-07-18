# Определение класса Contact, представляет один контакт
class Contact:
    def __init__(self, name: str, phone: str, address: str):
        """Инициализация объекта Contact

        :param name: Имя
        :param phone: Номер телефона
        :param address: Адрес
        """
        self.name = name
        self.phone = phone
        self.address = address


    def to_dict(self) -> dict:
        """Преобразует объект Contact в словарь для JSON

        :return: -> None
        """
        return {
            "name": self.name,
            "phone": self.phone,
            "address": self.address
        }


    @classmethod
    def from_dict(cls, data: dict) -> object:
        """Создаёт объект Contact из словаря

        :param data: Словарь с данными контакта
        :return: Объект Contact
        :rtype: Contact
        """
        return cls(
            name=data.get("name"),
            phone=data.get("phone"),
            address=data.get("address")
        )


    def __str__(self) -> str:
        """Возвращает строковое представление контакта

        :return: Строковое представление контакта
        :rtype: str
        """
        if self.address:
            return f"Имя: {self.name}, Телефон: {self.phone}, Адрес: {self.address}"
        else:
            return f"Имя: {self.name}, Телефон: {self.phone}"
