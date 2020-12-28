import time
from os import system


def hello_by_num():
    while True:
        system('CLS')
        try:
            num = float(input('Введите число: '))
            if num > 7:
                print('\n\tПривет')
                time.sleep(5)
                break
        except ValueError:
            print('Это не число! Попробуйте еще раз...')
            time.sleep(2)


def names_match():
    while True:
        name = 'Вячеслав'
        system('CLS')
        inputted_name = input('Введите имя: ')
        if inputted_name == name:
            print('\n\tПривет,', name)
            time.sleep(5)
            break
        else:
            print('\n\tНет такого имени')
            time.sleep(5)
            break


def get_multiples_of_three():
    pass



while True:
    system('CLS')
    print('<1> - Составить алгоритм: если введенное число больше 7, то вывести “Привет”\n')
    print('<2> - Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести\n'
          '\t“Привет, Вячеслав”, если нет, то вывести "Нет такого имени"\n')
    print('<3> - Составить алгоритм: на входе есть числовой массив, необходимо вывести\n'
          '\tэлементы массива кратные 3\n')
    print('<4> - Выход')
    try:
        choice = int(input('Введите номер(1-4) для выполнения: '))
        if choice == 1:
            hello_by_num()
        elif choice == 2:
            names_match()
        elif choice == 3:
            pass
        elif choice == 4:
            print('Выход...')
            break
        else:
            print('Некорректный ввод! Попробуйте еще раз...')
            time.sleep(1)
    except ValueError:
        print('Некорректный ввод! Попробуйте еще раз...')
        time.sleep(1)
