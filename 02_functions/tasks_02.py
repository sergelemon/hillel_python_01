def validate_password(password):

  # Функция принимает пароль строкой и выполняет валидацию с помощью трёх
  # вспомогательных функций:
  # 1. Содержит только a−z, A−Z, 0−9
  # 2. Содержит четное количество букв
  # 3. Содержит нечетное количество цифр
  # Основная функция возвращает True, если пароль валидный.
  # Если пароль не валидный, возвращает лист стрингов, в которых перечислены
  # причины неуспешной проверки. Например: ["содержит запрещенные символы"]

  error_list = list()

  if not symbols_correct(password):
    error_list.append('содержит запрещенные символы')

  if not even_letters(password):
    error_list.append('содержит нечетное число букв')

  if not odd_numbers(password):
    error_list.append('содержит четное число цифр')

  if len(error_list) == 0:
    return True
  else:
    return error_list


def symbols_correct(password):
  return len(set(password.lower()) - set('abcdefghijklmnopqrstuvwxyz0123456789')) == 0


def even_letters(password):
  return len([x for x in password if x.isalpha()]) % 2 == 0


def odd_numbers(password):
  return len([x for x in password if x.isdigit()]) % 2 != 0


def int_converter(input_int):

  # Функция принимает число и конвертирует его в 4 форматах:
  # decimal, octal, binary, hexadecimal. Каст в форматы описан в документации.
  # При касте нужно избавляться от первых символов (0o31 -> 31, 0xe6 -> e6).
  # Возвращает строку, отформатированную с помощью функции print_table.

  row1 = ['Decimal', 'Octal', 'Binary', 'Hexadecimal']
  row2 = [input_int, oct(input_int)[2:], bin(input_int)[2:], hex(input_int)[2:]]

  return print_table(4, 2, *[row1, row2])


def print_table(cols=1, rows=1, *data):

  # Функция генерирует псевдотаблицу текстом.
  # :cols: количество колонок в таблице
  # :rows: количество строк в таблице
  # :*data: лист листов, где каждый вложенный лист - строка данных.
  # Пример: print_table(cols=4, rows=2, [["Decimal", "Octal", "Binary", "Hexadecimal"], [230, 346, 11100110, "e6"]])
  # Вернет строку вида:
  #  -----------------------------------------------------------
  # | Decimal      | Octal        | Binary       | Hexadecimal  |
  # | 230          | 346          | 11100110     | e6           |
  #  -----------------------------------------------------------
  # Форматирование должно полностью совпадать с примером.
  # Обратить внимание на размеры ячеек - 12 символов на текст + по 1 вокруг
  # слева и справа от разделителя |.

  row_list = list()

  for row in range(rows):
    col_list = [f'{data[row][col]}' if (len(data) > row and len(data[row]) > col) else '' for col in range(cols)]
    s = ' | '.join([x.ljust(12) for x in col_list])
    row_list.append(f'| {s} |\n')

  line = ''.join([' ', '-' * (15 * cols - 1), '\n'])
  answer = ''.join([line, ''.join(row_list), line])

  return answer
