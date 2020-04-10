from random import randrange

class Game:

    def __init__(self):
        self.table1 = self._make_table()
        self.table2 = self._make_table()
        self.players = ('Player 1', 'Player 2')

    @staticmethod
    def _good_slot(table, row, column):
        # При создании корабля проверяем,
        # что ячейка и все соседние с ней свободны от кораблей
        for i in range(3):
            for j in range(3):
                try:
                    if table[row+i-1][column+j-1] != '~':
                        return False
                except:
                    continue
        return True

    @staticmethod
    def _shot(table, row, col):
        # Стреляем по цели и возвращаем результат стрельбы
        value = table[row][col]
        if value == '~':
            value = '*'
        elif value == 'O':
            value = 'X'
        table[row][col] = value
        # если попал, обвести соседние поля
        if value == 'X':
            for i in range(3):
                for j in range(3):
                    if i == j == 1:
                        continue
                    try:
                        table[row + i - 1][col + j - 1] = '*'
                    except:
                        continue
        return value

    @staticmethod
    def _convert_table(table, showAll):
        # Если это таблица противника, маскируем неизвестную игроку информацию
        if showAll:
            return table.copy()
        else:
            return [[' ' if (x == '~' or x == 'O') else x for x in row] for row in table]

    @staticmethod
    def _input_row_column():
        # Ожидаем ввода координат для выстрела
        while True:
            csv_row_column = input('Row (0-9), Column (0-9):')
            row_column = csv_row_column.split(',')
            if len(row_column) != 2:
                continue
            row, column = int(row_column[0]), int(row_column[1])
            if row in range(10) and column in range(10):
                break
        return row, column

    @staticmethod
    def _print_shot_result(shot, mine=True):
        # Сообщения игрокам о результате выстрела
        if mine:
            if shot == 'X':
                print('You did it!')
            else:
                print('You missed.')
        else:
            if shot == 'X':
                print('You have been shot!')
            if shot == '*':
                print('Your enemy missed!')

    def _generate_ships(self, table, number):
        # Создаем однотрубные корабли в количестве (number) штук
        for ship_number in range(number):
            while True:
                row, col = randrange(10), randrange(10)
                if self._good_slot(table, row, col):
                    table[row][col] = 'O'
                    break

    def _make_table(self):
        # Создаем пустую таблицу и заполняем ее кораблями
        table = [['~' for i in range(10)] for j in range(10)]
        self._generate_ships(table, 10)
        return table

    def _print_table(self, table, showAll):
        # Выводим таблицу на экран
        print('Your table:' if showAll else 'Enemy table:')
        copy_table = self._convert_table(table, showAll)
        rows_str = list()
        for row in copy_table:
            row_str = ' '.join(row)
            rows_str.append(f'{len(rows_str)} | {row_str} |')
        all_rows = '\n'.join(rows_str)
        hat = ' '.join([str(x) for x in range(10)])
        line = '-' * 23
        table_str = f'    {hat}\n  {line}\n{all_rows}\n  {line}'
        print(table_str)

    def _read_tables(self, player):
        # Выгружаем таблицы объекта в служебные таблицы игрока
        if player == 'Player 1':
            my_table = self.table1.copy()
            enemy_table = self.table2.copy()
        else:
            my_table = self.table2.copy()
            enemy_table = self.table1.copy()
        return my_table, enemy_table

    def _write_enemy_table(self, player, enemy_table):
        # Загружаем служебную таблицу с выстрелом игрока в таблицу его соперника
        if player == 'Player 1':
            self.table2 = enemy_table.copy()
        else:
            self.table1 = enemy_table.copy()

    def _you_are_winner(self, enemy_table):
        # Если игрок выиграл у соперника, прекратить игру
        for row in enemy_table:
            if 'O' in row:
                return False
        print('You have won the battle!')
        return True

    def play(self):

        while True:
            shot = ''
            for player in self.players:

                my_table, enemy_table = self._read_tables(player)

                self._print_table(my_table, True)
                self._print_table(enemy_table, False)
                self._print_shot_result(shot, False)
                print(f'{player} - make your move.')

                row, column = self._input_row_column()
                shot = self._shot(enemy_table, row, column)
                self._write_enemy_table(player, enemy_table)

                self._print_table(my_table, True)
                self._print_table(enemy_table, False)
                self._print_shot_result(shot)

                if self._you_are_winner(enemy_table):
                    return True
                while True:
                    next_move = input(f'{player}, continue or finish game, y/n:')
                    if next_move == 'n':
                        return True
                    elif next_move == 'y':
                        break

game = Game()
game.play()