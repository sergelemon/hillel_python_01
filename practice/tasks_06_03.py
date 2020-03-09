def count_work_hours(in_time, out_time, rate):
    """
    Функция считает оплату за отработанные часы.
    :in_time int: время начала, в целых часах, например, 8
    :out_time int: время окончания, в целых часах, например, 19
    :rate float: стоимость полного часа
    Возвращает строку вида "57.63 for 9 hours"
    Если количество часов < 8, оплата не считается и равна 0.
    Если количество часов > 8, оплата за каждый сверхурочный час считается по
    полуторному рейту.
    """
    work_time = out_time - in_time
    payment = 0.0
    if work_time == 8:
        payment = float(work_time * rate)
    elif work_time > 8:
        payment = (work_time * rate) + (work_time - 8) * (rate * 1.5)
    return f"{payment} for {work_time} hours"


def plan_trip(destination_list):
    """
    Функция считает стоимость путешествия.
    :destination_list list: список кортежей вида (длительность поездки, город),
    то есть, можно за один вызов посчитать несколько поездок.
    Возвращает цену для каждой поездки (float) списком.
    Стоимость путешествия = прямой перелет + обратный перелет + длительность *
    стоимость отеля.
    Цены:
    1. Получение стоимости отеля в заданном городе (за 1 ночь: Odesa - 33,
    Kyiv - 42, Larnaka - 49, Istanbul - 38);
    2. Получение стоимости перелета в заданный город или обратно (в 1 сторону:
    Odesa - 80, Kyiv - 97, Larnaka - 134, Istanbul - 149).
    """
    result = list()
    prices = {"Odesa": {"hotel": 33, "flight": 80}, "Kyiv": {"hotel": 42, "flight": 97}}
    for dest in dest_list:
        trip_days, dest_name = dest
        dest_data = prices[dest_name]
        flight_price = dest_data["flight"] * 2
        hotel_price = dest_data["hotel"] * trip_days
        result.append(hotel_price + flight_price)
    return result


from datetime import date
# d = date(1969, 6, 26) - конструктор даты
# d.year < 2020 - проверка даты

# database - список словарей, эмулирующий базу данных со строками и полями
database = list()


def validate_input(data: tuple):
    # """
    # Функция принимает список словарей, валидирует каждый из словарей на наличие
    # всех необходимых полей и тип их данных. Возвращает:
    # 1. bool в зависимости от результатов проверки;
    # 2. None или словарь, где ключ - тип ошибки (ValueError, KeyError),
    # а значение - список кортежей вида (ключ с ошибкой, словарь полностью).
    # Правила валидации:
    # first_name - string, не пустой, короче 48 символов
    # last_name - string, не пустой, короче 64 символов
    # birth - date, не пустой, не в будущем, не старше 100 лет
    # email - string, формат строка, затем @, затем опять строка, точка,
    # строка от 2 до 3 символов
    # Допустимые символы в email: буквы, цифры, символы (-_.)
    # """

    result = True
    error_dict = {'KeyError': [], 'ValueError':[]}

    for profile in data:
        result *= check_first_name(profile, error_dict)
        result *= check_last_name(profile, error_dict)
        result *= check_birth(profile, error_dict)
        result *= check_email(profile, error_dict)

    return result, error_dict

def check_first_name(profile, error_dict):

    result = True
    check_key = 'first_name'
    value = profile.get(check_key)

    if value == None:
        result = log_error(error_dict, 'KeyError', check_key, profile)
    elif not isinstance(value, str) or not len(value) or len(value) >= 48:
        result = log_error(error_dict, 'ValueError', check_key, profile)

    return result


def check_last_name(profile, error_dict):

    result = True
    check_key = 'last_name'
    value = profile.get(check_key)

    if value == None:
        result = log_error(error_dict, 'KeyError', check_key, profile)
    elif not isinstance(value, str) or not len(value) or len(value) >= 64:
        result = log_error(error_dict, 'ValueError', check_key, profile)

    return result


def check_birth(profile, error_dict):

    result = True
    check_key = 'birth'
    value = profile.get(check_key)

    if value == None:
        result = log_error(error_dict, 'KeyError', check_key, profile)
    elif not isinstance(value, date) or value > date.today() or date.replace(value, value.year + 100) < date.today():
        result = log_error(error_dict, 'ValueError', check_key, profile)

    return result


def check_email(profile, error_dict):

    check_key = 'email'
    value = profile.get(check_key)

    if value == None:
        return log_error(error_dict, 'KeyError', check_key, profile)

    while True:

        email_error = True
        if not isinstance(value, str) or not len(value):
            break

        email_parts = value.split('@')
        if not len(email_parts) == 2:
            break

        login, domain = email_parts
        last_point = domain.rfind('.')
        if last_point == -1:
            break
        elif not (1 < len(domain) - last_point - 1 < 4):
            break

        mask = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
        if len(set(login.lower()) - mask) > 0:
            break
        elif len(set(domain.lower()) - mask) > 0:
            break

        email_error = False
        break

    if email_error:
        return log_error(error_dict, 'ValueError', check_key, profile)
    else:
        return True


def log_error(error_dict, key1, key2, profile):
    error_dict[key1].append((key2, profile))
    return False


def handle_error(error_dict) -> None:
    """
    Функция принимает словарь ошибок и проблемных словарей и принтит их.
    Пример:
    ValueError found in:
    {"first_name": {"first_name": 42, "second_name": "Van Rossum"}}
    {"second_name": {"first_name": "Guido", "second_name": 42}}
    """
    print(error_dict)

    pass


def save_to_db(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей с данными, валидирует каждую запись с
    помощью вспомогательной функции validate_input, и если данные валидны,
    добавляет их в database.
    Возвращает bool по результатам успешного/неуспешного выполнения.
    """
    result, error_dict = validate_input(data)

    if not result:
        handle_error(error_dict)
    else:
        database.extend(list(data))

    return result


def select_from_db(field, value):
    """
    Функция возвращает кортеж словарей, где переданное значение встречается в
    переданном ключе.
    """
    pass





test = ({"first_name": "Guido", "last_name": "Van Rossum", "birth": date(1956,1,31), "email": "test@test.com"},
          {"first_name": "Sergey", "last_name": "Limanchuk", "birth": date(1976,1,2), "email": "sergelemon@gmail.com"})

if save_to_db(test):
    print('Data was successfully added.')
else:
    print('No data has been added.')