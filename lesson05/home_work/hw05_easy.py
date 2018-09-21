import sys
import os
from shutil import copyfile

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# РЕШЕНИЕ:
# Объявляем функции folder_make и folder_del

def folder_make():
    for i in range(1,10):
        try:
            os.mkdir('dir_'+str(i))
        except:
            continue
    return 0


def folder_del():
    for i in range(1,10):
        try:
            os.rmdir('dir_'+str(i))
        except:
            continue
    return 0

# Проверяем работу функций:
# folder_make()
# folder_del()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# РЕШЕНИЕ:
# Просто печатаем названия папок одно за другим.
# При желании можно вернуть массив

def print_dir_list():
    dirs = []
    i = 0
    print("List of current dir:")
    for x in os.listdir():
        if os.path.isdir(x):
            i += 1
            print(i,x)
    return 0

# Проверяем работу функции:
# print_dir_list()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_this_file():
    src = str(sys.argv[0])
    dst = src.replace('.py','_copy.py')
    copyfile(src, dst)

# Проверяем работу функции:
#copy_this_file()