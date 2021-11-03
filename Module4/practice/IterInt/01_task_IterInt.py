# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class IterInt(int):
    def __init__(self, integ, start=0):
        self.i = start
        self.integ = integ

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(str(self.integ)):
            return int(str(self.integ)[self.i])
        else:
            raise StopIteration


n = IterInt(123456)

for digit in n:
    print("digit = ", digit)

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6
