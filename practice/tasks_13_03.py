import os
from datetime import datetime


# Напишите функцию копирования файлов. На вход ваша функция принимает два аргумента:
# - путь файла который необходимо скопировать
# - путь каталога куда этот файл необходимо скопировать

def copyFileDir(inFile, outDir):
    file_name = inFile.split('/')[-1]
    with open(inFile, 'r') as source, open(f'{outDir}/{file_name}', 'a') as recipient:
        recipient.write(source.read())


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
            result = text
            for tag in tags:
                result = tag_base[tag].replace('%text%', result)
            return result
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
        return [file_name for file_name in func(*args) if file_name[-4:] == '.log']
    return wrapper


@log_reading
def get_files():
    return os.listdir()


# Напишите функцию, которая читает и распечатывает текстовый файл.
# Напишите декоратор к этой функции, который печатает название файла и количество слов в нем

def check_file(func):
    def wrapper(*args):
        file_name = args[0]
        print(file_name)
        with open(file_name, 'r') as log:
            print(len(log.read().split()))
        result = func(*args)
        return result
    return wrapper

@check_file
def printfile(file_name):
    with open(file_name, 'r') as log:
        print(log.read())
