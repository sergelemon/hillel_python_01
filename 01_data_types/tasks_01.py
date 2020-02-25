def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    result_list = [x for x in url_list if x.find('/catalog/') >= 0]

    return result_list


def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    idiotic_str = ''

    for i in input_str:
        idiotic_str += i.capitalize() if len(idiotic_str) % 2 else i

    return idiotic_str


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    if len(input_str) < 4:
        return input_str

    point = int(len(input_str) / 2)
    output_str = input_str[point - 1: 1 - point]

    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = dict()

    for x in input_str:
        if not output_dict.get(x):
            output_dict[x] = 0
        output_dict[x] += 1

    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    point = int(len(str1) / 2)
    result_str = ''.join([str1[:point], str2, str1[point:]])

    return result_str


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    avg_scores = dict()

    for x in score_list:

        key_value = x.split('|')
        name, str_values = key_value[0], key_value[1]
        values = str_values.split(',')

        sum = 0
        for x in values:
            sum += int(x)

        avg_scores[name] = 0 if not sum else round(sum / len(values))

    return avg_scores


def encrypt_str(input_str):
    """
    Дописать функцию, которая будет шифровать полученную строку следующим
    образом:
    Пример 1: "www" -> "w3"
    Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
    """
    encrypted_str, current_letter, letter_count = '', '', 0

    for x in input_str:

        if x == current_letter:
            letter_count += 1
            continue

        encrypted_str += current_letter
        if letter_count > 1:
            encrypted_str += str(letter_count)

        current_letter, letter_count = x, 1

    encrypted_str += current_letter
    if letter_count > 1:
        encrypted_str += str(letter_count)

    return encrypted_str


def square_dict(input_dict):
    """
    Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
    """
    squared_dict = dict()

    for x in input_dict:
        squared_dict[x] = x ** 2

    return squared_dict


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    return [x for x in range(100) if not x % 2]


def replace_vowels(input_str):
    """
    Заменить в произвольной строке согласные буквы на гласные.
    """
    import random

    result_str = ''
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')

    for x in input_str:

        letter = x
        upper_flag = x.isupper()
        if upper_flag:
            letter = letter.lower()

        if letter in vowels:
            result_str += x
            continue

        index = random.randint(0, len(vowels) - 1)
        letter = vowels[index]

        if upper_flag:
            letter = letter.capitalize()

        result_str += letter

    return result_str


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """

    unique_int_list = list()
    for x in input_list:
        if not x in unique_int_list:
            unique_int_list.append(x)

    return unique_int_list


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """

    sorted_list = filter_unique_int(input_list)
    sorted_list.sort(reverse=True)

    return sorted_list[0:3]


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """

    return input_list.index(min(input_list))


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """

    return input_list[::-1]


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """

    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())

    common_keys = list(keys1 & keys2)
    common_keys.sort()

    return common_keys


def sort_by_age(student_list):
    """
    Дан массив из словарей. C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """
    # your code here
    sorted_dict = None
    return sorted_dict
