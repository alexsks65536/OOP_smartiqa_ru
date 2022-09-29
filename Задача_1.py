"""
Есть Человек, характеристиками которого являются:
Имя
Возраст
Наличие денег
Наличие собственного жилья
"""


class Human:

    # Статические поля
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Money: {self.__money}\n"
            f"House: {self.__house}"
        )

    # Статический метод
    @staticmethod
    def default_info():
        print(
            f"default_name: {Human.default_name}\n" f"default_age: {Human.default_age}"
        )

    def earn_money(self, amount):
        self.__money += amount
        print(f"Earned {amount} money! Current value: {self.__money}")

    # Приватный метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("No money enough!")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f"Final price: {final_price}")
        return final_price


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == "__main__":

    Human.default_info()
    alexander = Human("Sasha", 27)
    alexander.info()

    small_house = SmallHouse(8_500)

    alexander.buy_house(small_house, 5)
    alexander.earn_money(5_000)
    alexander.buy_house(small_house, 5)
    alexander.earn_money(20_000)
    alexander.buy_house(small_house, 5)
    alexander.info()
