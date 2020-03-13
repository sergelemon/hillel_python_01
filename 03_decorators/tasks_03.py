# 1. Написать свой cache декоратор c максимальным размером кеша и его очисткой
# при необходимости.

def do_cache(maxsize):
    def decorator(func):
        cache = dict() # этот дикт будет доступен при следующих вызовах
        def wrapper(*args):

            if maxsize < 1:
                return func(*args)

            if len(cache) >= maxsize:
                # Если количество закешированных элементов превышает maxsize,
                # нужно удалить самый первый закешированный элемент.
                cache.pop(list(cache).pop(0))

            if args not in cache:
                cache[args] = func(*args)

            return cache.get(args)
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
        if 0 <= args[0] <= 100:
            rest = 100 % func(*args)
            if rest:
                print(f'Bad news guys, we got {rest}')
            else:
                print('We are OK!')
        else:
            print(f'Bad news guys, the value should be in the range 0..100')
        return None
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
        print(f'{args}: {cache_count[args]}')

        if args not in cache:
            cache[args] = func(*args)

        return cache.get(args)
    return wrapper


@count_args
def my_func(string):
    return string