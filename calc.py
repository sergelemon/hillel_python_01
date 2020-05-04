import tkinter as tk

class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.max_height = 580
        self.max_width = 470
        root.geometry(f'{self.max_width}x{self.max_height}')
        root.title("Калькулятор")
        self.pack()
        self._create_main_layout()

    def _create_main_layout(self):
        self._create_labels()
        self._create_buttons()

    def _create_labels(self):
        # Служебные
        self._delete_if_add_number = False
        self._point_control = False

        label_dict = dict()
        label_dict['bg'] = 'sky blue'
        label_dict['justify'] = 'right'
        label_dict['anchor'] = 'e'
        label_dict['width'] = self.max_width

        self.formula = ''
        self.str_formula = tk.StringVar()
        label_dict['textvariable'] = self.str_formula
        label_dict['font'] = 'Arial 48'

        label = tk.Label(self, label_dict)
        label.pack(side='top')

        self.result = 0
        self.str_result = tk.StringVar()
        label_dict['textvariable'] = self.str_result
        label_dict['font'] = 'Arial 20'

        label2 = tk.Label(self, label_dict)
        label2.pack(side='top', anchor='n')

    def _create_buttons(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        button_style = dict()
        button_style['height'] = 3
        button_style['width'] = 7
        button_style['bd'] = 0
        button_style['fg'] = '#FFFFFF'
        button_style['bg'] = '#666666'
        button_style['font'] = f'Arial 20'

        self.button_frame_741 = tk.Frame(self, bg='#666666', padx=2)
        self.button_frame_741.pack(side='left')
        self._create_button(self.button_frame_741, button_style, '7', self.click_7)
        self._create_button(self.button_frame_741, button_style, '4', self.click_4)
        self._create_button(self.button_frame_741, button_style, '1', self.click_1)
        self._create_button(self.button_frame_741, button_style, ',', self.click_point)

        self.button_frame_852 = tk.Frame(self, bg='#666666', padx=2)
        self.button_frame_852.pack(side='left')
        self._create_button(self.button_frame_852, button_style, '8', self.click_8)
        self._create_button(self.button_frame_852, button_style, '5', self.click_5)
        self._create_button(self.button_frame_852, button_style, '2', self.click_2)
        self._create_button(self.button_frame_852, button_style, '0', self.click_0)

        self.button_frame_963 = tk.Frame(self, bg='#666666', padx=2)
        self.button_frame_963.pack(side='left')
        self._create_button(self.button_frame_963, button_style, '9', self.click_9)
        self._create_button(self.button_frame_963, button_style, '6', self.click_6)
        self._create_button(self.button_frame_963, button_style, '3', self.click_3)
        self._create_button(self.button_frame_963, button_style, '=', self.click_eval)

        button_style['bg'] = '#808080'
        button_style['font'] = f'Arial 16'

        self.button_frame_actions = tk.Frame(self, bg='#808080', padx=7, pady=17)
        self.button_frame_actions.pack(side='left')
        self.button_del = self._create_button(self.button_frame_actions, button_style, 'DEL', self.click_del)
        self._create_button(self.button_frame_actions, button_style, '/', self.click_divide)
        self._create_button(self.button_frame_actions, button_style, '*', self.click_multiply)
        self._create_button(self.button_frame_actions, button_style, '-', self.click_subtraction)
        self._create_button(self.button_frame_actions, button_style, '+', self.click_addition)

    def _create_button(self, owner, button_style, title, command):
        button_style['text'] = title
        button_style['command'] = command
        new_button = tk.Button(owner, button_style)
        new_button.pack()
        return new_button

    def _eval_result(self):
        formula = self.formula
        if len(formula) and formula[-1] in '+-*/':
            formula = formula[:-1]
        if formula == '':
            self.result = 0
            self.str_result.set('')
            return
        try:
            self.result = eval(formula)
            if isinstance(self.result, float) and int(self.result) == self.result:
                self.result = int(self.result)
            self.str_result.set(self.result)
        except:
            self.str_result.set('ERROR')

    def evaluate_string(self, string):
        for symbol in string:
            self.add_symbol(symbol)
        return self.result

    def add_symbol(self, symbol):
        formula = self.formula

        # Если после нажатия на "=" вводится цифра,
        # тогда нужно удалить результат предыдущего вычисления и начать создание новой формулы
        if self._delete_if_add_number:
            if not symbol in '+-*/':
                formula = ''
            self._delete_if_add_number = False

        # Если пользователь вводит два операнда подряд, первый из них будет удален из формулы
        if symbol in '+*/' and len(formula) and formula[-1] in '+-*/':
            formula = formula[:-1]

        # Если вводится ноль, а потом любая цифра, ноль удаляется
        if formula == '0' and symbol in '0123456789':
            formula = ''

        # Проверяем, чтобы правильно вводили точки
        if self._point_control:
            if symbol == '.':
                return
            elif symbol in '+-*/':
                self._point_control = False
        elif symbol == '.':
            self._point_control = True
            # Если вводится точка, и предыдущий символ в формуле не был цифрой
            # тогда добавим ноль перед точкой
            if not len(formula) or not formula[-1] in '0123456789':
                formula = f'{formula}0'

        new_formula = f'{formula}{symbol}'
        self.formula = new_formula
        self.str_formula.set(new_formula)

        self._eval_result()

        if self.button_del['text'] == 'CLR':
            self.button_del['text'] = 'DEL'

    def click_0(self):
        self.add_symbol('0')

    def click_1(self):
        self.add_symbol('1')

    def click_2(self):
        self.add_symbol('2')

    def click_3(self):
        self.add_symbol('3')

    def click_4(self):
        self.add_symbol('4')

    def click_5(self):
        self.add_symbol('5')

    def click_6(self):
        self.add_symbol('6')

    def click_7(self):
        self.add_symbol('7')

    def click_8(self):
        self.add_symbol('8')

    def click_9(self):
        self.add_symbol('9')

    def click_point(self):
        self.add_symbol('.')

    def click_addition(self):
        self.add_symbol('+')

    def click_subtraction(self):
        self.add_symbol('-')

    def click_multiply(self):
        self.add_symbol('*')

    def click_divide(self):
        self.add_symbol('/')

    def click_eval(self):
        # Клавиша "=" не сработает, если формула содержит ошибку, например, было деление на 0
        if self.str_result.get() == 'ERROR':
            return
        self._delete_if_add_number = True
        self._point_control = False
        self.formula = str(self.result)
        self.str_formula.set(self.formula)
        self.button_del['text'] = 'CLR'

    def click_del(self):
        if self.button_del['text'] == 'CLR':
            # Полная очистка регистров
            self._delete_if_add_number = False
            self._point_control = False
            self.formula = ''
            self.result = 0
            self.str_formula.set('')
            self.str_result.set('')
        else:
            # Удаляем только последний символ в формуле
            if self.formula[-1] == '.':
                self._point_control = False
            new_formula = self.formula[:-1]
            self.formula = new_formula
            self.str_formula.set(new_formula)
            self._eval_result()


root = tk.Tk()
app = Application(root=root)

# 1 вариант использования
# app.click_5()
# app.click_addition()
# app.click_5()
# print(app.result)

# 2 вариант использования
# app.add_symbol('5')
# app.add_symbol('+')
# app.add_symbol('5')
# print(app.result)

# 3 вариант использования
# print(app.evaluate_string('5+5'))

app.mainloop()