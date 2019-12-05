# Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class Expt:
    def __init__(self,):
        self.my_list_int = []

    def us_inp(self):
        while True:
            try:
                us_int = int(input('Введите данные: '))
                self.my_list_int.append(us_int)
                print(f'список: {self.my_list_int}')
            except:
                print('В список добавляются только числа!')
                user_answer = input('NEXT???(Y/N)')
                if user_answer.lower() == 'y':
                    continue

                else:
                    return f'the end\nyour list {self.my_list_int}'


try_us = Expt()
print(try_us.us_inp())