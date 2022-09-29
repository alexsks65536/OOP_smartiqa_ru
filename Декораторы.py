# Простой декоратор
def my_decorator(my_func):
    def inner():
        print('Decorator starts...')
        my_func()
        print('Decorator finishes...')

    return inner


# Декоратор для функции с параметрами
def my_decorator_with_params(my_func):
    def inner(*args, **kwargs):
        print('Decorator with parameters starts...')
        my_func(*args, **kwargs)
        print('Decorator with parameters finishes...')

    return inner


# Использование декоратора
@my_decorator
def print_hi():
    print('Hi!')


print_hi()  # Вызов функции, обернутой декоратором

print('-' * 30)

# Создаем экземпляр функции декоратора и передаем в качестве параметра функцию
decorated_func = my_decorator(print_hi)
decorated_func()


# Использование декоратора для функции с параметрами
@my_decorator_with_params
def adder(**nums):
    print(f'Сумма равна: {sum(nums.values())}')


print('-' * 30)
print('-' * 30)

adder(c=1, b=2)

