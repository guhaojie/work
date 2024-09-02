import random

BOUND_U = 100
BOUND_L = 0


def basic_gen(result=None):
    """
    根据提供的数，来生成一个结果是该数的算式
    :param result: 结果
    :return: 格式为{x,op,y,r}的算式
    """
    _r = random.randint(BOUND_L, BOUND_U) if result is None else result
    _op = random.choice(['+', '-', '×', '÷']) if _r != 0 else random.choice(['+', '-', '×'])
    _fn = {
        '+': [lambda r: random.randint(BOUND_L, r),
              lambda r, x: r - x],
        '-': [lambda r: random.randint(r, BOUND_U),
              lambda r, x: x - r],
        '×': [lambda r: random.choice([i for i in range(2, r) if r % i == 0] or [1, r]),
              lambda r, x: random.randint(BOUND_L, BOUND_U) if x == 0 else int(r / x)],
        '÷': [lambda r: random.choice([i for i in range(1, BOUND_U // r)] or [1]) * r,
              lambda r, x: int(x / r)]
    }
    while True:
        _x = _fn[_op][0](_r)
        _y = _fn[_op][1](_r, _x)
        if len(list(filter(
                lambda x: True if BOUND_L <= x <= BOUND_U else False,
                [_x, _y]))) == 2:
            break

    return {'x': _x,
            'op': _op,
            'y': _y,
            'r': _r}


def expand_gen(fn, n, x):
    """
    根据提供的公式、次数，拓展算式
    :param fn:生成公式的函数
    :param n:拓展次数
    :param x:初始算式
    :return:拓展的结果
    """
    if n != 0:
        i = random.choice(['x', 'y'])
        x[i] = fn(x[i])
        expand_gen(fn, n - 1, x[i])
    return x


def gen_print(x, last_op=None, lr=None):
    """
    打印公式，去括号版
    :param x: 公式
    :param last_op: 记录符号堆栈
    :param lr: 是否为右子树（减加、除乘不能去括号）
    :return: 去括号算式
    """
    _op_order = {'+': 0, '-': 0, '×': 1, '÷': 1}
    _r = ""
    _wrap = False if last_op is None else (
            (_op_order[last_op] > _op_order[x['op']]) or
            (last_op == '-' and _op_order[x['op']] == 0 and lr == 'r') or
            (last_op == '÷' and lr == 'r'))
    if _wrap:
        _r += "("
    if type(x['x']) is dict:
        _r += gen_print(x['x'], x['op'], 'l')
    else:
        _r += f"{x['x']}"
    _r += f" {x['op']} "
    if type(x['y']) is dict:
        _r += gen_print(x['y'], x['op'], 'r')
    else:
        _r += f"{x['y']}"
    if _wrap:
        _r += ")"
    if last_op is None:
        _r += " = ? "
    return _r


for _ in range(2):
    x_o = expand_gen(basic_gen,
                     2,
                     basic_gen(random.randint(BOUND_L, BOUND_U)))
    x_r = x_o['r']
    print(f"{_ + 1}>\t{gen_print(x_o)}", end='')
    ans = input()
    if ans == str(x_r):
        print("It's right!")
    else:
        print(f"It's wrong! The right answer is {x_r}.")
