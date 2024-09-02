def sigma(_from, _to, _step, _func):
    _ans = 0
    for _ in range(_from, _to + 1, _step):
        _ans += _func(_)
    return _ans
