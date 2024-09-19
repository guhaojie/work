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
