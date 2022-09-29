class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # метод возращает служебную информацию о переменной класса
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"

    def __len__(self):
        return self.name


cat = Cat("Васька")
print(cat)


class Point:
    "класс координат точек"

    def __init__(self, *args):  # инициализатор нескольких переменных
        self.__coords = args

    def __len__(self):  # метод возращает длину списка переменных
        return len(self.__coords)

    def __abs__(self):  # метод возращает абсолютные значения списка переменных
        return list(map(abs, self.__coords))

    def __str__(self):  # метод возращает список переменных
        return f"{self.__coords}"


p = Point(-1, 2, -3, -5, 7, 0, -6)
print(p)
print(len(p))
print(abs(p))


class Clock:
    __DAY = 86400  # Число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)


c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(8400)
print(c1.get_time())
c1 = c1 + 100
c3 = c1 + c2 + c3
print(c1.get_time())
print(c2.get_time())
print(c3.get_time())
