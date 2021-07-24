class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point x:{self.x}, y:{self.y}"

    def distance(self, p2):  # метод - преобразован из функции (см. ниже)
        """
        Расстояние между двумя точками
        """
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# def distance(p1, p2): # функция
#     """
#     Расстояние между двумя точками
#     """
#     return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
point1 = Point(3, 5)  # Задаем точку
point1.move(-2, 4)  # смещаем точку методом move из класса
# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

lnt_max = 0
points.insert(0, Point(0, 0))
point_max = 0
for point in points:
    # if distance(points[0], point) > lnt_max: # для вызова функции
    if points[0].distance(point) > lnt_max:  # для вызова метода
        # lnt_max = distance(points[0], point) # для вызова функции
        lnt_max = points[0].distance(point)  # для вызова метода
        point_max = point

print(f"Координаты наиболее удаленной точки = {point_max.x}, {point_max.y}")
print(f"Растояние состаляет = {lnt_max:.2f}")
print(point_max)  # срабатывает def __str__(self):
