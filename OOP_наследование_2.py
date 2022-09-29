"""
Производные классы объявляются так же, как их родительский класс; однако список базовых классов для наследования дается
после имени класса

class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
"""


class Parent:  # define parent class

    parentAttr = 1000

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Parent1:  # define parent class

    parentAttr1 = 1001

    def __init__(self):
        print("Calling parent1 constructor")

    def parentMethod1(self):
        print("Calling parent1 method")

    def setAttr1(self, attr):
        Parent1.parentAttr1 = attr

    def getAttr1(self):
        print("Parent1 attribute :", Parent1.parentAttr1)


class Parent2:  # define parent class

    parentAttr2 = 1003

    def __init__(self):
        print("Calling parent2 constructor")

    def parentMethod2(self):
        print("Calling parent2 method")

    def setAttr2(self, attr):
        Parent2.parentAttr2 = attr

    def getAttr2(self):
        print("Parent attribute2 :", Parent2.parentAttr2)


class Parent3:  # define parent class

    parentAttr3 = 100

    def __init__(self):
        print("Calling parent3 constructor")

    def parentMethod3(self):
        print("Calling parent3 method")

    def setAttr3(self, attr):
        Parent3.parentAttr3 = attr

    def getAttr3(self):
        print("Parent3 attribute :", Parent3.parentAttr3)


class Child(Parent, Parent1, Parent2, Parent3):  # define child class
    def __init__(self):
        super().__init__()
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
print(c.parentAttr)
c.parentMethod1()  # calls parent's method
print(c.parentAttr1)
c.parentMethod2()  # calls parent's method
print(c.parentAttr2)
c.parentMethod3()  # calls parent's method
print(c.parentAttr3)
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method"""
print(c.parentAttr)

"""
Переопределяющие методы
Вы всегда можете переопределить ваши родительские методы класса. Одна из причин переопределения родительских методов 
заключается в том, что вам может потребоваться особая или другая функциональность в вашем подклассе.
"""


class Parent:  # define parent class
    def operate(self):
        print("Calling parent method")


class Child(Parent):  # define child class
    def operate(self):
        print("Calling child method")


c = Child()  # instance of child
c.operate()  # child calls overridden method
