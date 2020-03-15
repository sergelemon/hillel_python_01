import os
from datetime import datetime


# Напишите функцию копирования файлов. На вход ваша функция принимает два аргумента:
# - путь файла который необходимо скопировать
# - путь каталога куда этот файл необходимо скопировать

def copyFileDir(inFile, outDir):
    # if inFile.find('/') > 0:
    file_name = inFile.split('/')[-1]
    # else:
    #     file_name = inFile
    with open(inFile, 'r') as source, open(f'{outDir}/{file_name}', 'a') as recipient:
        recipient.write(source.read())

testfile = 'tasks_13_03.py'
testdir = 'C://Users/Sergey/Documents/GitHub/hillel_python_01/test'
copyFileDir(testfile, testdir)


# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline

def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }
        def wrapper(text):
            # your code here
            pass
        return wrapper
    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

def log_reading(func):
    def wrapper(*args):
        # your code here
        pass
    return wrapper


@log_reading
def get_files():
    # your code here
    return file_list


# Напишите функцию, которая читает и распечатывает текстовый файл.
# Напишите декоратор к этой функции, который печатает название файла и количество слов в нем
