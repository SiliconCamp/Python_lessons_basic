import random
import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# РЕШЕНИЕ:
# Генерируем ряд Фиббоначи с самого начала. По достижении начального элемента ряда (n), начинаяем добавлять
# значения i-того элемента в результирующий массив. И так до тех пор, пока не достигнем конечного элемента (m)

print("_____________________________")
print("Task #1 - OK")


def fibonacci(n, m):
    fib1 = 1
    fib2 = 1
    fibarray = []


    i = 2
    while i < m:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        if i >= n-1:
            fibarray.append(fib2)
        i += 1

    return fibarray

# Проверяем работу функции:
# Рандомно генерируем начальную и конечную позицию ряда в переменных fibo_start и fibo_finish
# Максимальное значение генератора в примере ограничено 40 элементами, но можно поставить любые значения.

fibo_start = random.randint(1, 40)
fibo_finish = random.randint(fibo_start, 40)

print("Fibonacci: from", fibo_start, "to", fibo_finish, "=", fibonacci(fibo_start, fibo_finish))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
# РЕШЕНИЕ:
# Мы воспользуемся гномьим алгоритмом сортировки. Данный алгоритм очень прост и задействует только один цикл:
# "Это метод, которым садовый гном сортирует линию цветочных горшков. По существу он смотрит на текущий и предыдущий
# садовые горшки: если они в правильном порядке, он шагает на один горшок вперёд, иначе он меняет их местами и шагает
# на один горшок назад. Граничные условия: если нет предыдущего горшка, он шагает вперёд; если нет следующего горшка,
# он закончил."
# Дик Грун http://kvodo.ru/gnome-sorting.html


print("_____________________________")
print("Task #2 - OK")
print("Generating the list ...")
rand_list_len = random.randint(10, 50) # Определяем количество элементов в списке от 10 до 50 элементов
print("List len (elements):", rand_list_len)

rand_list = []

while len(rand_list) != rand_list_len:
    num = random.randint(-100,100) # Генерируем элемент от -100 до 100
    rand_list.append(num)

print("Random list: ",rand_list)


def sort_to_max(arr):
    i = 1
    while i < len(arr):
        if not i or arr[i - 1] <= arr[i]:
            i+=1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i-=1
    return arr

# Проверяем работу функции:
print("Gnome sorted random list:", sort_to_max(rand_list))
print("Gnome sorted list from task:", sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# РЕШЕНИЕ:
# Исходя из сути условия точки расположены в двухмерном пространстве.
# На данный момент программа может некорректно определять вершины, но при ручной установке вершин - работает.
print("_____________________________")


def abs_vector(coor_x1, coor_y1, coor_x2, coor_y2):
    abs_vect_len = math.sqrt((coor_x2 - coor_x1) ** 2 + (coor_y2 - coor_y1) ** 2)
    return abs_vect_len


print("Task #4")
print("Generating points...")
x1, y1 = random.randint(1,100), random.randint(1,100)
x2, y2 = random.randint(1,100), random.randint(1,100)
x3, y3 = random.randint(1,100), random.randint(1,100)
x4, y4 = x1+(x3-x2), y3+(y1-y2) # Для тестирования вставить после равно x1+(x3-x2), y3+(y1-y2), либо рандинты
print("A1=", x1, y1)
print("A2=", x2, y2)
print("A3=", x3, y3)
print("A4=", x4, y4)

# Определяем расстояния от точки к A1 к трем остальным
len_1_2 = abs_vector(x1, y1, x2, y2)
print("A1A2 =", len_1_2)
len_1_3 = abs_vector(x1, y1, x3, y3)
print("A1A3=", len_1_3)
len_1_4 = abs_vector(x1, y1, x4, y4)
print("A1A4=", len_1_4)

# Проверям все три возможных комбинации диагональной вершины
# Внутри каждого случая проверяем выполнение условия о равенстве противолежащих сторон
if (len_1_2 > len_1_3) & (len_1_2 > len_1_4):
    print("max == A1A2 ==", len_1_2)
    if (len_1_3 == abs_vector(x2, y2, x4, y4)) & (len_1_4 == abs_vector(x2, y2, x3, y3)):
        print("Parallelogram = A1A3A2A4")
elif (len_1_3 > len_1_2) & (len_1_3 > len_1_4):
    print("max == A1A3 ==", len_1_3)
    if (len_1_2 == abs_vector(x3, y3, x4, y4)) & (len_1_4 == abs_vector(x3, y3, x2, y2)):
        print("Parallelogram = A1A3A2A4")
else:
    print("max == A1A4 ==", len_1_4)
    if (len_1_2 == abs_vector(x4, y4, x3, y3)) & (len_1_3 == abs_vector(x4, y4, x2, y2)):
        print("Parallelogram = A1A3A2A4")




