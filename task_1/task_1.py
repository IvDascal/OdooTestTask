# Завдання 1.
# Створити функцію що приймає число, перевіряє його та виводить “Even” або “Odd”


def is_even(num):
    if isinstance(num, int):
        if num % 2:
            print(num, 'Odd')
        else:
            print(num, 'Even')
    else:
        print('Not valid input')


def is_even_binary(num):
    if isinstance(num, int):
        if num & 1:
            print(num, 'Odd')
        else:
            print(num, 'Even')
    else:
        print('Not valid input')


if __name__ == '__main__':
    is_even(41)
    is_even(42)
    is_even(-41)
    is_even(-42)
    is_even(0)
    is_even(42.42)
    is_even('testString')

    is_even_binary(41)
    is_even_binary(42)
    is_even_binary(-41)
    is_even_binary(-42)
    is_even_binary(0)
    is_even_binary(42.42)
    is_even_binary('testString')




