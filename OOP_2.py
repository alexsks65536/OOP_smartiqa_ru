"""
Динамические поля
self - это ссылка на текущий экземпляр класса
"""


class Phone:

    # статические переменные класса
    default_color = "Grey"
    default_model = "C385"

    def __init__(self, color, model):
        # Динамические поля
        self.color = color
        self.model = model


# Создадим экземпляр класса Phone
my_phone_red = Phone("Red", "I495")
print(dir(my_phone_red))
# Получим статические поля объекта
print(my_phone_red)
print(my_phone_red.default_model)
print(my_phone_red.default_color)
# Получим динамические поля объекта
print(my_phone_red.color)
print(my_phone_red.model)
my_phone_blue = Phone("Blue", "I495")
print(my_phone_blue)
print(my_phone_blue.color)
print(my_phone_blue.model)


class Apple:

    # Создаем объект с общим кол-вом яблок 12
    def __init__(self):
        self.whole_amount = 12

    # Съедаем часть яблок для текущего объекта
    def eat(self, number):
        self.whole_amount -= number


my_apple = Apple
