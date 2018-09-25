# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# РЕШЕНИЕ:
# Чтобы не плодить сущности, будем решать обе задачи через создание общего класса многоугольник (polygon) у которого
# будет пока один метод - определение длин сторон. Если соображу как, то навешу туда периметр, площадь и т.п.

import math


# Класс Многоугольник
class PolyGon:
    def __init__(self):
        pass

    def sideof(self, p_1, p_2):
        return math.sqrt((int(p_1[0]) - int(p_2[0])) ** 2 + (int(p_1[1]) - int(p_2[1])) ** 2)

# Задача №1 - создаем класс треугольника от многоугольника


class TriAngle(PolyGon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = self.sideof(self.a, self.b)
        self.bc = self.sideof(self.b, self.c)
        self.ac = self.sideof(self.a, self.c)

    @property
    def tr_area(self):
        semi_per = (self.ab + self.bc + self.ac) / 2 # вычисляем полупериметр треугольника
        s = math.sqrt(semi_per * (semi_per - self.ab) * (semi_per - self.bc) * (semi_per - self.ac))
        return s

    @property
    def tr_perimeter(self):
        return self.ab + self.bc + self.ac

    def tr_height(self, tr_base):
        return self.tr_area * 2 / tr_base


tr_1 = TriAngle((5, 5), (5, 20), (25, 5)) # Тут мы задаем экземпляр с координатами вершин


print('AB:', str(tr_1.ab))
print('BC:', str(tr_1.bc))
print('AC:', str(tr_1.ac))
print('Area of Triangle: ', str(tr_1.tr_area))
print('Perimeter of Triangle: ', str(tr_1.tr_perimeter))
print('Height: ', str(tr_1.tr_height(tr_1.bc)))
print('\n')


# Задача №2 - создаем класс трапеции от многоугольника


class Trapeze(PolyGon):
    def __init__(self, a, b, c, d):

        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.ab = self.sideof(self.a, self.b)
        self.bc = self.sideof(self.b, self.c)
        self.cd = self.sideof(self.c, self.d)
        self.ad = self.sideof(self.a, self.d)

    @property
    def isosceles(self):
        if self.sideof(self.a, self.c) == self.sideof(self.b, self.d):
            return True
        else:
            return False

    # Возвращает площадь трапеции, либо полупериметр если неравнобедренная. Не успеваю накатить
    # формулу Герона чтобы давала плозадь неравнобочной трапеции также.
    @property
    def tr_area(self):
        if self.isosceles:
            s = ((self.bc + self.ad) / 2) * math.sqrt(self.ab ** 2 - ((self.bc - self.ad) ** 2) / 4)
            return s
        else:
            semi_per = (self.ab + self.bc + self.cd + self.ad) / 2
            s = semi_per
            return s

    @property
    def tr_perimeter(self):
        return self.ab + self.bc + self.cd + self.ad


trap_1 = Trapeze((5, 5), (10, 20), (25, 25), (30, 5)) # Тут мы задаем экземпляр с координатами вершин
if trap_1.isosceles:
    print('Trapezium is isosceles')
else:
    print('Trapezium is NOT isosceles')


print('Area of Trapezium: ', str(trap_1.tr_area))
print('Perimeter of Trapezium: ', str(trap_1.tr_perimeter))
