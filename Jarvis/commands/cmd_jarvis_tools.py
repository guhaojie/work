from sympy.matrices.expressions.kronecker import validate


def do_greet(line):
    """Greet the user."""
    print(f"Hello, {"User" if not line else line}!")

def do_get_news(line):
    """更新每日新闻"""
    import os
    os.system('/Users/haojiegu/PycharmProjects/Jasmine/GET_NEWS/每日新闻.command')

def do_math(line):
    """math <num of questions>"""
    import os
    os.system('python /Users/haojiegu/PycharmProjects/Jasmine/Mathmatics/FFR.py '+line)

def do_scanf(line):
    from core.base_io import Validate
    x = Validate()
    x.input("请输入15-20之间的整数", 'int', (15, 20))
    x.input("请输入15-20之间的数", 'float', (15, 20))
    x.input("请输入日期 (格式: YYYY-MM-DD)", 'date')
