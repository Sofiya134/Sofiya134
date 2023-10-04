from functools import reduce
w = input('Enter words').split()
s = input('Enter separator')
def my_join(w, s):
    return reduce(lambda x, y: x + s + y, w)
n = my_join(w, s)
print(f'result: {n}')
