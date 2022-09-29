class Cat:

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self, name, bred='pers', age=1, color='white'):
        print('hello new object is ', self, name, bred, age, color)
        self.name = name
        self.bred = bred
        self.age = age
        self.color = color


#jerry = Cat()
#print(jerry)
Cat('Tom', 'siam', 40, 'black')
walt = Cat('Walt')
kelly = Cat('Kelly', age=40)
