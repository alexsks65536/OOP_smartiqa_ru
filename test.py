class YesInit:
    def __init__(self, one, two):
        self.fname = one
        self.sname = two


obj1 = YesInit("Peter", "Ok")
print(obj1.fname, obj1.sname)


class NoInit:
    def names(self, one, two):
        self.fname = one
        self.sname = two


obj2 = NoInit()
obj2.names("Peter", "Ok")
print(obj2.fname, obj2.sname)

"""--------описание класса---------------------"""


class ClassName:
    "Optional class documentation string"


print(ClassName().__doc__)

"""______________________________________________________"""


class Employee:
    "Common base class for all employees"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(f"Total Employee {Employee.empCount}")

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"""This would create first object of Employee class"""
emp1 = Employee("Zara", 2000)
emp1.displayEmployee()
"""This would create second object of Employee class"""
emp2 = Employee("Manni", 5000)
emp2.displayEmployee()
emp1.displayCount()

"""Вы можете добавлять, удалять или изменять атрибуты классов и объектов в любое время
"""
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.

"""
Встроенные атрибуты класса
Каждый класс Python поддерживает следующие встроенные атрибуты, и к ним можно получить доступ, используя оператор точки, как и любой другой атрибут —

__dict__ — словарь, содержащий пространство имен класса.
__doc__ — Строка документации класса или нет, если она не определена.
__name__ — Имя класса.
__module__ — Имя модуля, в котором определяется класс. Этот атрибут «__main__» в интерактивном режиме.
__bases__ — возможно пустой кортеж, содержащий базовые классы, в порядке их появления в списке базовых классов.
"""

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

""" ДЕструктор"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the obejcts
del pt1
del pt2
del pt3

try:
    print(id(pt1), id(pt2), id(pt3))
except NameError:
    print(f"Объекты pt1, pt2, pt3 уничтожены")
