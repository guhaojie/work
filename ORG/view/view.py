import os
import platform

class View:
    def show_level_1_title(title):
        print(f"\n{title.center(60, '=')}\n")

    def show_level_2_title(title):
        print(f"\n{title.center(60, '-')}\n")

    def show_message(message, end='\n'):
        print(f"{message}", end=end)

    def get_message(prompt):
        try:
            return input(f"\n{prompt} ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n输入中断，程序退出。")
            exit()

    def show_notification(message):
        return input(f"\nNOTICE: {message}")

    def clear():
        sys = platform.system()
        if sys == u'Windows':
            os.system('cls')
        else:
            os.system('clear')
