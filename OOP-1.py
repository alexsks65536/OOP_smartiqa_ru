#  Создадим класс "Car"
class Car:
    #  атрибуты класса
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive():
        print("'Let's Go!'")


car_1 = Car()  # Создали переменную с классом "Car"
car_2 = Car()
print(car_1)  # переменные car_1 и car_2 принадлежат классу "Car"
print(car_2)  # но видно что это различные объекты
print(car_1.model)
print(car_1.engine)
print(car_2.model)
print(car_2.engine)
print(Car.__dict__)  # просмотр атрибутов класса
print(getattr(Car, 'model'))  # просмотр аттрибута по имени "model"
print(getattr(Car, 'xxx',
              100))  # если атрибут "ххх" отсутствует, то вернется "100", это помогает избежать исключения "AttributeError"
Car.model = "Mercedes"  # Изменение атрибута
print(car_1.model)
Car.x = "X-type"  # если отсутствует атрибут с именем "х", то можно есго создать с присвоением ему значения
print(Car.x)
setattr(Car, 'volume', 1500)  # установка аттрибута
print(Car.volume)
print(Car.__dict__)
del Car.volume  # удаление аттрибута "Volume"
print(Car.__dict__)
delattr(Car, 'x')  # удаление аттрибута строенной функцией "delattr"
print(Car.__dict__)
print(f'{"-" * 50}')
a1 = Car()
a2 = Car()
a1.seat = 4
print(a1.__dict__)
a1.model = 'Lada'  # Устанавливаем атрибут экземпляра класса
print(a1.__dict__)
print(a1.model)  # Атрибут экземпляра класса изменился только у данного экземпляра
print(f'{"-" * 50}')
print(Car.drive())  # Вызов функции класса
getattr(Car, 'drive')()  # Вызов функции класса
a = Car()
a.drive()  # Таким образом, drive является методом, если не использовать декоратор "@staticmethod"

'''class Person:  #  Создадим класс "Person"
    name = 'Ivan'
    age = 30

print(Person())  # Вызовем экземпляр класса
a = Person()
print(a)'''
