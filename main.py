"""
smartiqa.ru

"""


class Phone:

    # статические переменные класса
    default_color = "Grey"
    default_model = "C385"

    def turn_on(self):
        pass

    def turn_off(self):
        pass


# список атрибутов класса
# print(dir(Phone))
# print(Phone().__delattr__)

print(Phone.default_color)
Phone.default_color = "Black"
print(Phone.default_color)
