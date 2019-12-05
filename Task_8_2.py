# Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class ErrorZeroDelete(Exception):
    def __init__(self, my_int):
        self.my_int = my_int


inp_a = input('Введите число: ')
inp_b = input('Введите число на которое будете делить: ')


try:
    inp_a = int(inp_a)
    inp_b = int(inp_b)
    if inp_b == 0:
        raise ErrorZeroDelete(f'На ноль делить нельзя!')
except ErrorZeroDelete as err:
    print(err)
else:
    res = inp_a / inp_b
    print(f'result of deleted: {res}')
