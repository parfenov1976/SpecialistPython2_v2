# Разработать класс TotalDict со следующими возможностями:
class TotalDict(dict):
    def __str__(self):
        return f'TD:{repr(self)}'

    def __add__(self, other):
        for el in other.keys():
            if el in self.keys():
                self[el] += other[el]
            else:
                self.update([(el, other[el])])
        return self

    def most_expensive(self, ind=-1):
        lst = [*self.items()]
        lst.sort(key=lambda x: x[1], reverse=True)
        return lst[0:ind]


# 1. Объект выводит себя в консоли как обычный словарь, НО с символами TD: в начале
items1 = TotalDict(milk=250, bread=120, meat=450.6)
items2 = TotalDict(juice=99.9, fish=120, milk=50.2)
print(items1)  # TD:{'milk': 250, 'bread': 120, 'meat': 450.6}

# 2. При сложении объектов TotalDict значения элементов с одинаковыми ключами суммируются
all_items = items1 + items2
print(all_items)  # TD:{'milk': 300.2, 'bread': 120, 'meat': 450.6, 'juice': 99.9, 'fish': 120}

# 3. Добавить метод .most_expensive() выводящий все элементы в виде списка кортежей,
# упорядоченного по убыванию по значениям
print(all_items.most_expensive())  # [('meat', 450.6), ('milk', 300.2), ('bread', 120), ('fish', 120), ('juice', 99.9)]

# 4. Метод .most_expensive() можно передать целое число, ограничивающее кол-во возвращаемых значений
print(all_items.most_expensive(3))  # [('meat', 450.6), ('milk', 300.2), ('bread', 120)] <-- только 3 кортежа
