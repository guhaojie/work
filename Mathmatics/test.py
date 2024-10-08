from sympy import *

x = symbols('x')
res = integrate(3 * x ** 4 * exp(-2 * x), (x, 0, oo))


def pipeline(data, *funcs):
    _data = data
    for _func in funcs:
        try:
            _data = _func(_data)
        except Exception as e:
            print(f"ERROR: {e}, {_func.__name__}({_data})")
    return _data


def add(num):
    return num + 1


def power(num):
    return num * num

def sq(num):
    return num/0


print(pipeline(3, power, add, sq, add, power, sq))
