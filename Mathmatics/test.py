import random

BOUND_U = 100


def basic_gen(result=None):
    _r = random.randint(0, BOUND_U) if result is None else result
    _op = random.choice(['+', '-', '×', '÷']) if _r != 0 else random.choice(['+', '-', '×'])
    _fn = {
        '+': [lambda r: random.randint(0, r),
              lambda r, x: r - x],
        '-': [lambda r: random.randint(r, BOUND_U),
              lambda r, x: x - r],
        '×': [lambda r: random.choice([i for i in range(2, r) if r % i == 0] or [1]),
              lambda r, x: int(r / x)],
        '÷': [lambda r: random.choice([i for i in range(1, 10)]) * r,
              lambda r, x: int(x / r)]
    }
    while True:
        _x = _fn[_op][0](_r)
        _y = _fn[_op][1](_r, _x)
        if len(list(filter(
                lambda x: True if 0 <= x <= BOUND_U else False,
                [_x, _y]))) == 2:
            break

    return [[_x, _op, _y], _r]


def expand_gen(fn, n, x):
    if n != 0:
        i = random.choice([0, 2])
        x[0][i] = fn(x[0][i])
        expand_gen(fn, n - 1, x[0][i])
    return x


def gen_print(x, last_op=None, lr=None, p_fn=print):
    _op_order = {'+': 0, '-': 0, '×': 1, '÷': 1}
    x0 = x[0]
    _wrap = False if last_op is None else (
            (_op_order[last_op] > _op_order[x0[1]]) or
            (last_op == '-' and lr == 'r') or
            (last_op == '÷' and lr == 'r'))
    if _wrap:
        p_fn("(", end='')
    if type(x0[0]) is list:
        gen_print(x0[0], x0[1], 'l', p_fn)
    else:
        p_fn(f"{x0[0]}", end='')
    print(f" {x0[1]} ", end='')
    if type(x0[2]) is list:
        gen_print(x0[2], x0[1], 'r', p_fn)
    else:
        p_fn(f"{x0[2]}", end='')
    if _wrap:
        p_fn(")", end='')
    if last_op is None:
        p_fn(" = ? ", end='')


def testp(*args, **kwargs):
    print(*args, **kwargs)


for _ in range(2):
    x_o = expand_gen(basic_gen,
                     2,
                     basic_gen(random.randint(1, 99)))
    x_r = x_o[1]
    print(f"{_+1}>\t", end='')
    gen_print(x_o, p_fn=testp)
    ans = input()
    if ans == str(x_r):
        print("It's right!")
    else:
        print(f"It's wrong! The right answer is {x_r}.")
