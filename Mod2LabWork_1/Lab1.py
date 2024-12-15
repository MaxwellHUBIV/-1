import doctest
from typing import Union

class Milk:
    def __init__(self, milk_name: str, fat_percent: Union[int, float], milk_volume: Union[int, float], milk_left: Union[int, float]):
        """
            Создание и подготовка к работе объекта "Молоко"

            :param milk_name: Название молока
            :param fat_percent: Жирность молока
            :param milk_volume: Объем молока в литрах
            :param milk_left: Остаток молока в литрах

            Примеры:
            >>> milk1 = Milk("Бабушкина крынка",3, 1, 1)  # инициализация экземпляра класса
        """
        if not isinstance(milk_name, str):
            raise TypeError("Название молока должно быть типа Str")
        if len(milk_name) == 0:
            raise ValueError("У молока должно быть название")
        self.milk_name = milk_name

        if not isinstance(fat_percent, (int, float)):
            raise TypeError("Жирность молока должна быть типа int или float")
        if 0.5 < fat_percent > 9.5:
            raise ValueError("Такой жирности молока не существует")
        self.fat_percent = fat_percent

        if not isinstance(milk_volume, (int, float)):
            raise TypeError("Объем пакета молока должен быть типа int или float")
        if milk_volume < 0:
            raise ValueError("Объем пакета молока должен быть больше нуля")
        self.milk_volume = milk_volume

        if not isinstance(milk_left, (int, float)):
            raise TypeError("Оcтаток молока должен быть типа int или float")
        if milk_left <= 0:
            raise ValueError("Остаток молока должен не должен быть меньше нуля")
        self.milk_left = milk_left

    def is_empty_milk(self) -> bool:
        """
            Функция которая проверяет кончилось ли молоко

            :return: Молоко если или нет?

            Примеры:
            >>> milk1 = Milk("Весёлый молочник",0.5, 1, 0)
            >>> milk1.is_empty_milk()
        """
        ...

    def add_new_milk(self, addmilk_volume: float) -> None:
        """
            Мы купили молоко в пакете и доливаем в бутылку.

            :param addmilk_volume: Объем нового молока

            :raise ValueError: Если количество добавляемого молока превышает свободное место в бутылке, то вызываем ошибку

            Примеры:

            >>> milk1 = Milk("Весёлый молочник",0.5, 1.5, 0.9)
            >>> milk1.add_new_milk(1)
        """
        if not isinstance(addmilk_volume, (int, float)):
            raise TypeError("Объем нового пакета молока должен быть типа int или float")
        if addmilk_volume < 0:
            raise ValueError("Объем нового пакета молока должен быть больше нуля")
        ...

class Soda:
    def __init__(self, soda_name: str, soda_volume: Union[int, float], soda_left: Union[int, float]):
        """
            Создание и подготовка к работе объекта "Газировка"

            :param soda_name: Название газировки
            :param soda_volume: Объем бутылки газировки
            :param soda_left: Остаток газировки

            Примеры:
            >>> soda1 = Soda("Добрый-Cola",2, 2)  # инициализация экземпляра класса
        """
        if not isinstance(soda_name, str):
            raise TypeError("Название газировки должно быть типа Str")
        if len(soda_name) == 0:
            raise ValueError("У газировки должно быть название")
        self.soda_name = soda_name

        if not isinstance(soda_volume, (int, float)):
            raise TypeError("Объём газировки должен быть типа int или float")
        if soda_volume < 0:
            raise ValueError("Объем газировки должен быть больше нуля")
        self.soda_volume = soda_volume

        if not isinstance(soda_left, (int, float)):
            raise TypeError("Остаток газировки должен быть типа int или float")
        if soda_left < 0:
            raise ValueError("Количество газировки не может быть отрицательным числом")
        self.soda_left = soda_left

    def is_empty_bottle(self) -> bool:
        """
            Функция которая проверяет является ли бутылка пустой

            :return: Является ли бутылка с Байкалом из Черноголовки пустой (пейте без остановки)

            Примеры:
            >>> soda1 = Soda("Байкал",2, 0)
            >>> soda1.is_empty_bottle()
        """
        ...

    def remove_soda_from_bottle(self, estimate_soda: float) -> None:
        """
            Извлечение газировки из бутылки.

            :param estimate_soda: Объем извлекаемой жидкости

            :raise ValueError: Если количество извлекаемой жидкости превышает количество газировки в бутылке,
            то возвращается ошибка.

            :return: Объем реально извлеченной газировки

            Примеры:
            >>> soda1 = Soda("Shh... Lemon",2, 2)
            >>> soda1.remove_soda_from_bottle(0.5)
        """
        ...

class Candy:
    def __init__(self, candy_name: str, manufacturer: str,):
        """
            Создание и подготовка к работе объекта "Конфета"

            :param candy_name: Название конфеты
            :param manufacturer: Производитель

            Примеры:
            >>> candy1 = Candy("Ирис Кис-Кис", "Красный Октябрь")  # инициализация экземпляра класса
        """
        if not isinstance(candy_name, str):
            raise TypeError("Название конфеты должно быть типа Str")
        if len(candy_name) == 0:
            raise ValueError("У конфеты должно быть название")
        self.candy_name = candy_name

        if not isinstance(manufacturer, str):
            raise TypeError("Название производителя должно быть типа Str")
        if len(manufacturer) == 0:
            raise ValueError("Производитель должен быть указан")
        self.manufacturer = manufacturer

    def is_manufacturer_correct(self, manufacturer_check: str) -> bool:
        """
            Функция которая проверяет откуда конфета

            :return: Изготовлена ли конфета на заводе "Красный пищевик" (Республика Беларусь)

            Примеры:
            >>> candy1 = Candy("Зефир Бобруйский", "Красный пищевик")
            >>> candy1.is_manufacturer_correct("Красный пищевик")
        """
        if not isinstance(manufacturer_check, str):
            raise TypeError("Название производителя должно быть типа Str")
        if len(manufacturer_check) == 0:
            raise ValueError("Производитель должен быть указан")

        ...

if __name__ == "__main__":
    doctest.testmod()
