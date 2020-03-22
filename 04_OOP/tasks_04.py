import os
import json

'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''

class IpHandler:

    def __init__(self, ipList):
        self._ipList = ipList

    @property
    def ipList(self):
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        self._ipList = newList

    def reverse_IP(self):
        return ['.'.join(id.split('.')[::-1]) for id in self._ipList]

    def get_oct_1_3(self):
        return ['.'.join(id.split('.')[1:]) for id in self._ipList]

    def get_oct_3(self):
        return [id.split('.')[-1] for id in self._ipList]


'''У вас несколько JSON файлов. В каждом из этих файлов есть
произвольная структура данных. Вам необходимо написать
класс (без реализации конструктора) который будет описывать работу с
этими файлами, а именно:
1) Запись в файл
2) Чтение из файла
3) Получить путь относительный путь к файлу
4) Получить абсолютный путь к файлу'''


class JSONhandler:
    """Handles .json files: read, write, get abs/rel path"""

    def read(self, file):
        """Reads json file"""
        with open(file) as f:
            return json.load(f)

    def write(self, input_data, file):
        """Writes json-formatted data to provided file"""
        with open(file, 'w') as json_file:
            json.dump(input_data, json_file)

    def get_absolute_path(self, file):
        """Returns absolute path to provided file"""
        return os.path.abspath(file)

    def get_relative_path(self, file):
        """Returns relative path to provided file"""
        return os.path.relpath(file)


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''

class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, new_value):
        self._unit_name = new_value

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, new_value):
        self._mac_address = new_value

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, new_value):
        self._ip_address = new_value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_value):
        self._login = new_value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_value):
        self._password = new_value


'''Создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, new_value):
        self._hours = new_value if new_value < 23 else 23

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, new_value):
        self._minutes = new_value if new_value < 59 else 59

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, new_value):
        self._seconds = new_value if new_value < 59 else 59

    def __repr__(self):
        h = '%02d' % self.hours
        m = '%02d' % self.minutes
        s = '%02d' % self.seconds
        return f'{h}:{m}:{s}'

    # Если __str__ не определён, то str() использует repr().
    # def __str__(self):
    #     pass

    def change(self, h=0, m=0, s=0):
        self._seconds += s
        while self._seconds < 0:
            self._seconds += 60
            self._minutes -= 1
        while self._seconds > 59:
            self._seconds -= 60
            self._minutes += 1
        self._minutes += m
        while self._minutes < 0:
            self._minutes += 60
            self._hours -= 1
        while self._minutes > 59:
            self._minutes -= 60
            self._hours += 1
        self._hours += h
        while self._hours < 0:
            self._hours += 24
        while self._hours > 23:
            self._hours -= 24


'''Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер
группы, успеваемость (массив из пяти элементов).
Создайте список студентов из десяти элементов (10 экземпляров вашего класса).
Напиши функции:
1. Упорядочить массив по возрастанию среднего балла.
2. Вывести фамилии и номера групп студентов, имеющих оценки, равные
только 4 или 5.'''

class Student:
    def __init__(self, surname, name, patronymic, group, avg_mark):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.group = group
        self.avg_mark = avg_mark
    def __repr__(self):
        return f'{self.surname} {self.name}.{self.patronymic}, group {self.group} - mark {self.avg_mark}'

def sort_by_avg_mark(s_list):
    return sorted(s_list, key=lambda x: x.avg_mark)

def get_best_by_mark(s_list):
    return [x for x in s_list if x.avg_mark > 3]