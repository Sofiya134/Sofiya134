from functools import reduce
def my_decorator(func):
    def qwerty(x):
        print(f'Received value {x}')
        r = func(x)
        print (f'Result {r}')
        return r
    return qwerty
@my_decorator
def myfunc(x):
    return reduce(lambda x, y: x * y, range(1, x + 1))
f = myfunc(3)
print(f'result = {f}')
