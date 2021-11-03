# Задание:
# Напишите класс для работы с римскими цифрами.
class Roman:
    roman_digits = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                    500: 'D', 900: 'CM', 1000: 'M'}

    def __init__(self, number):
        self.dec_number = number

    @property
    def rom_number(self):
        rom_numb = ''
        dec_number = self.dec_number
        for item in sorted(Roman.roman_digits, reverse=True):
            digit = dec_number // item
            dec_number %= item
            rom_numb += Roman.roman_digits[item] * digit
        return rom_numb

    def __str__(self):
        return self.rom_number

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.dec_number + other.dec_number)
        else:
            return Roman(self.dec_number + other)

    def __radd__(self, other):
        return Roman(self.dec_number + other)

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.dec_number * other.dec_number)
        else:
            return Roman(self.dec_number * other)

    def __rmul__(self, other):
        return Roman(self.dec_number * other)

    def __floordiv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.dec_number // other.dec_number)
        else:
            return Roman(self.dec_number // other)

    def __rfloordiv__(self, other):
        return Roman(self.dec_number // other)

    def __gt__(self, other):
        if isinstance(other, Roman):
            return self.dec_number > other.dec_number
        else:
            return self.dec_number > other

    def __lt__(self, other):
        if isinstance(other, Roman):
            return self.dec_number < other.dec_number
        else:
            return self.dec_number < other

    def __eq__(self, other):
        if isinstance(other, Roman):
            return self.dec_number == other.dec_number
        else:
            return self.dec_number == other

    def __ne__(self, other):
        if isinstance(other, Roman):
            return self.dec_number != other.dec_number
        else:
            return self.dec_number != other


# Реализуйте операции:
# Сложение
# Вычитание
# Умножение
# Целочисленное деление
# Сравнение (> < == !=)
# Пример:
n1 = Roman(10)
n2 = Roman(14)
print(n1)  # X
print(n2)  # XIV
n3 = n1 + n2
print(n3)  # XXIV
n3 *= 2
print(n3)  # XLVIII
n3 //= 2
print(n3)  # XXIV
print(n3 > n2)
print(n3 > 2)
print(n3 < n2)
print(n3 < 2)
print(n3 == 2)
print(n3 == n1 + n2)
print(n3 != 2)
print(n3 != n1 + n2)

# ограничение: 4-значные числа.
# Алгоритм
# 1. Выделяем (если есть) количество целых тысяч.
# Полученное значение позволить сгенерировать строку с n количеством «M» (читаем, n*1000).
# Пример: 2012 после первого пункта даст «MM»
#
# 2. Получаем остаток после деления на 1000, чтобы выделить в дальнейшем следующие значения.
#
# 3. Выделяем (если возможно), целые 500. При этом учитываем что если полученное значение равно 4 (5+4=9),
# то следует записывать как значение 1000-100, что в римский СС равнозначно «CM».
# Пример: 1887 после этого пункта даст нам «MD».
# 1945 соответственно «MCM».
#
# 4. Получаем остаток от деления на 500.
#
# 5. Делим на 100 чтобы выделить целые сотни и складываем к предыдущему результату. Учитываем что если получили 4,
# что равнозначно 400, то записываем как 500-100, то есть «CD».
# Пример: 1709 даст после этого шага «MDCCC».
#
# 6. Получаем остаток от деления на 100.
#
# 7. Выделяем из него целые полсотни. Если значение будет равно 4 (то есть 90), то записываем как 100-10,
# что равно «XC». Иначе прибавляем к строке «L»
# Пример: 1986 после всего выдаст нам «MCML».
#
# 8. Выделяем остаток от 50.
#
# 9. Выделяем целое количество десятков и складываем к строке n раз символ «X».
# При этом учитываем что 40 пишется как 50-10, то есть «XL».
# Пример: 1986 после всего выдаст нам «MCMLXXX».
#
# 10. Получаем остаток от деления на 10. Этот шаг отличается от других тем,
# что можно сразу приравнять остаток к его эквиваленту. 1=I, 7=VII и так далее.
#
# После перебора числа этим алгоритмом мы получаем примерно такое:
# 2012 == MMXII
