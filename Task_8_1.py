# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    def __str__(self):
        return f'Data {self.day_month_year}'

    @classmethod
    def get_int_data(cls, day_month_year):
        int_data = []
        for i in day_month_year.split():
            if i != '-':
                int_data.append(i)
        return int(int_data[0]), int(int_data[1]), int(int_data[2])

    @staticmethod
    def check_data(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Ok'
                else:
                    return f'year incorrect'
            else:
                return f'month incorrect'
        else:
            return f'day incorrect'


print(Data.get_int_data('1 - 6 - 1978'))
print(Data.check_data(1, 6, 1978))
