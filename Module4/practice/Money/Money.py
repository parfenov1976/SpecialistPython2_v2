import urllib.request
import json


class Money:
    def __init__(self, rub, cop, valute='RUB'):
        self.rub = rub
        self.rub += cop // 100
        self.cop = cop % 100
        self.valute = valute

    def __str__(self):
        if self.valute == 'RUB':
            return f'{self.rub}руб {self.cop}коп'
        elif self.valute == 'USD':
            return f'{self.rub}usd {self.cop}cen'
        elif self.valute == 'EUR':
            return f'{self.rub}eur {self.cop}cen'

    def __add__(self, other):
        return Money(self.rub + other.rub, self.cop + other.cop)

    def __mod__(self, other):
        return Money(self.rub * other // 100, round(self.rub * other % 100 + self.cop * other / 100))

    def __mul__(self, other):
        return Money(int(self.rub * other), round(self.rub * other % 1 * 100 + self.cop * other))

    def __rmul__(self, other):
        return Money(int(self.rub * other), round(self.rub * other % 1 * 100 + self.cop * other))

    def __truediv__(self, other):
        return Money(int(self.rub / other), round(self.rub / other % 1 * 100 + self.cop * other))

    def convert(self, cur):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        converted_sum = self / data_dict['Valute'][cur]['Value']
        converted_sum.valute = cur
        return converted_sum


if __name__ == '__main__':
    money_sum1 = Money(20, 120)
    print(money_sum1)
    money_sum1 = Money(20, 60)
    money_sum2 = Money(10, 45)
    money_result = money_sum1 + money_sum2
    print(money_result)

    money_sum1 = Money(20, 60)
    # Находим 21% от суммы
    percent_sum = money_sum1 % 21
    print(percent_sum)

    # Конвертация в USD
    money_sum3 = Money(1234, 54)
    print(money_sum3)
    print(money_sum3.convert('EUR'))
    print(money_sum3.convert('USD'))
