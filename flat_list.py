# Вам нужно распаковать вложенный лист [1,2,3,[5,6,[7,8]],9] в один "плоский" лист. Нужно 2 реализации:
#
# Сделать это с импортируемого функционала

# Подходящего функционала в itertools не нашел :(
# Есть функция flatten в библиотеке iteration_utilities, но, кажется, она малопопулярна

# Сделать это самостоятельно

def flat_list(basic_list):
    for i in basic_list:
        if isinstance(i, list):
            yield from flat_list(i)
        else:
            yield i

old_list = [1,2,3,[5,6,[7,8]],9]
print(list(flat_list(old_list)))



