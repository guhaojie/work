class BaseView:
    def display_message(self, message):
        print(f"{message}")

    def get_input(self, prompt):
        return input(f"\n{prompt} ")

    def display_menu(self, options, title="菜单"):
        print(f"\n{'='*30}\n{title}\n{'='*30}")
        for key, value in options.items():
            print(f"{key}. {value}")
        print("b. 返回上一级" if title != "菜单" else "q. 退出")
        print('='*30)

    def display_section_title(self, title):
        print(f"\n{'-'*30}\n{title}\n{'-'*30}")
