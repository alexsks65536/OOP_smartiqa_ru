"""
Операторы перегрузки
Предположим, что вы создали класс Vector для представления двумерных векторов. Что произойдет, когда вы добавите
оператор «плюс»? Скорее всего, Python будет кричать на вас.
Однако вы можете определить метод __add__ в вашем классе для выполнения сложения векторов, и тогда оператор плюс
будет вести себя так, как ожидалось:
"""


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Возвращает строковое представление объекта.
    def __str__(self):
        return f"Vector {self.a, self.b}"

    # Перегрузка арифметических операторов
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Vector(self.a * other.a, self.b * other.b)

    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

    def __truediv__(self, other):
        return Vector(self.a / other.a, self.b / other.b)


class Numbers:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f"{self.n}"

    def __add__(self, other):
        return f"Сумма: {Numbers(self.n + other.n)}"

    def __sub__(self, other):
        return f"Разность: {Numbers(self.n - other.n)}"

    def __mul__(self, other):
        return f"Произведение: {Numbers(self.n * other.n)}"

    def __truediv__(self, other):
        return f"Частное: {Numbers(self.n / other.n)}"

    def __floordiv__(self, other):  # целочисленное деление (x // y).
        return f"целочисленное деление :{Numbers(self.n // other.n)}"

    def __mod__(self, other):  # остаток от деления (x % y).
        return f"остаток от деления: {Numbers(self.n % other.n)}"

    def __pow__(self, power, modulo=None):
        return f"Возведение в степень: {Numbers(self.n ** power.n)}"


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print(v1 * v2)
print(v1 - v2)
print(v1 / v2)
""""-------------------------"""
n = Numbers(65536)
m = Numbers(1024)
x = 2
y = 10
print(n)
print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)
print(n % m)
print(x**y)
