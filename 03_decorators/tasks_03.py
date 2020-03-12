# 1. Написать свой cache декоратор c максимальным размером кеша и его очисткой
# при необходимости.

def do_cache(maxsize):
    def decorator(func):
        cache = dict() # этот дикт будет доступен при следующих вызовах
        def wrapper(*args):

            if len(cache) > maxsize:
                # Если количество закешированных элементов превышает maxsize,
                # нужно удалить самый первый закешированный элемент.
                cache.pop(list(cache).pop(0))

            if args in cache:
                # Если элемент уже есть в кеше, нужно вернуть его, не вызывая
                # декорируемой функции
                result = cache.get(args)
            else:
                # Если элемента нет в кеше, нужно вызвать декорируемую функцию,
                # сохранить ее результат в кеш и вернуть ее результат
                result = func(*args)
                cache[args] = result

            return result
        return wrapper
    return decorator


@do_cache(maxsize=2)
def test(v, i):
    return v + i


# 2. Написать свой декоратор который будет проверять остаток от деления числа 100
# на результат работы функции ниже. Если остаток от деления = 0, вывести
# сообщение "We are OK!», иначе «Bad news guys, we got {остаток от деления}».
# Этот декоратор не должен возвращать результат работы функции. Только один из
# указанных принтов.

def div100(func):
    def wrapper(*args):
        rest = 100 % func(*args)
        return f'Bad news guys, we got {rest}' if rest else 'We are OK!'
    return wrapper

@div100
def test2(v):
    return v


# 3. Декоратор должен кэшировать значения аргументов, считать количество
# использований одних и тех же аргументов и печатать их перед исполнением
# декорируемой функции.

def count_args(func):

    cache = dict() # этот дикт будет доступен при следующих вызовах
    cache_count = dict() # этот дикт будет доступен при следующих вызовах

    def wrapper(*args):

        if cache_count.get(args) == None:
            cache_count[args] = 0
        cache_count[args] += 1
        print(cache_count)

        if args in cache:
            result = cache.get(args)
        else:
            result = func(*args)
            cache[args] = result

        return result

    return wrapper


@count_args
def my_func(string):
    return string