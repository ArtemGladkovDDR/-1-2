from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, brand: str, max_speed: float):
        """
        Инициализация транспортного средства.

        :param brand: Бренд транспортного средства (например, "Toyota").
        :param max_speed: Максимальная скорость в км/ч (должна быть положительным числом).

        :raises ValueError: Если max_speed не положительное число.

        >>> car = Transport("Toyota", 180)
        >>> car.brand
        'Toyota'
        >>> car.max_speed
        180
        """
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")
        self.brand = brand
        self.max_speed = max_speed

    @abstractmethod
    def accelerate(self, increment: float) -> float:
        """
        Увеличивает скорость транспортного средства.

        :param increment: Увеличение скорости в км/ч.
        :return: Новая скорость.

        >>> car = Transport("Toyota", 180)
        >>> car.accelerate(20)
        200
        """
        ...

    @abstractmethod
    def brake(self, decrement: float) -> float:
        """
        Уменьшает скорость транспортного средства.

        :param decrement: Уменьшение скорости в км/ч.
        :return: Новая скорость.

        >>> car = Transport("Toyota", 180)
        >>> car.brake(30)
        150
        """
        ...


class Book(ABC):
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц (должно быть положительным числом).

        :raises ValueError: Если pages не положительное число.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.title
        '1984'
        >>> book.pages
        328
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self, pages_to_read: int) -> str:
        """
        Читает указанное количество страниц.

        :param pages_to_read: Количество страниц для чтения.
        :return: Сообщение о прочитанных страницах.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(50)
        'Вы прочитали 50 страниц.'
        """
        ...

    @abstractmethod
    def bookmark(self, page: int) -> str:
        """
        Устанавливает закладку на указанной странице.

        :param page: Номер страницы для закладки.
        :return: Сообщение о том, что закладка установлена.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.bookmark(100)
        'Закладка установлена на странице 100.'
        """
        ...


class ElectronicDevice(ABC):
    def __init__(self, brand: str, battery_life: int):
        """
        Инициализация электронного устройства.

        :param brand: Бренд устройства.
        :param battery_life: Время работы от батареи в часах (должно быть положительным числом).

        :raises ValueError: Если battery_life не положительное число.

        >>> device = ElectronicDevice("Apple", 10)
        >>> device.brand
        'Apple'
        >>> device.battery_life
        10
        """
        if battery_life <= 0:
            raise ValueError("Время работы от батареи должно быть положительным числом.")
        self.brand = brand
        self.battery_life = battery_life

    @abstractmethod
    def power_on(self) -> str:
        """
        Включает устройство.

        :return: Сообщение об успешном включении.

        >>> device = ElectronicDevice("Apple", 10)
        >>> device.power_on()
        'Устройство включено.'
        """
        ...

    @abstractmethod
    def charge(self, hours: int) -> str:
        """
        Заряжает устройство.

    :param hours: Количество часов для




