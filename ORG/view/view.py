class View:
    def show_level_1_title(title):
        print(f"\n{title.center(60, '=')}\n")

    def show_level_2_title(title):
        print(f"\n{title.center(60, '-')}\n")

    def show_message(message):
        print(f"{message}")

    def get_message(prompt):
        try:
            return input(f"{prompt} ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n输入中断，程序退出。")
            exit()

    def show_notification(message):
        input(f"\nNOTICE: {message}\nPress ANY KEY to continue: ")
