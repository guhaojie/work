def do_greet(arg):
    """Greet the user."""
    print(f"Hello, {"User" if not arg else arg}!")

def do_get_news(arg):
    """获取每日新闻"""
    import os
    os.system('/Users/haojiegu/PycharmProjects/Jasmine/GET_NEWS/每日新闻.command')
