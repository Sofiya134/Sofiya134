def my_decorator(func):
    def qwerty(*args, **kwargs):
        print(f'Received value {args}, {kwargs}')
        r = func(*args, **kwargs)
        print (f'Result {r}')
        return r
    return qwerty
@my_decorator
def myfunc(a, b, c):
    return a + b + c
s = myfunc(1, 2, 3)
print(f'result = {s}')
