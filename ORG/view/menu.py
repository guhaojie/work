from view.view import View

class Menu:
    def __init__(self, title="主菜单"):
        self.title = title
        self.options = {}
        self.sub_menus = {}
        self.parent_menu = None

    def register_option(self, key, description, action=None, submenu=None):
        if submenu:
            submenu.parent_menu = self
            self.sub_menus[key] = submenu
        else:
            self.options[key] = (description, action)

    def display(self):
        View.show_level_1_title(self.title)
        for _ in sorted(self.options.keys()):
            View.show_message(f"{_}. {self.options[_][0]}")
        for _ in sorted(self.sub_menus.keys()):
            View.show_message(f"{_}. {self.sub_menus[_].title}")
        if self.parent_menu:
            View.show_message("b. 返回")
        else:
            View.show_message("q. 退出")

    def execute(self, choice):
        if choice in self.options:
            self.options[choice][1]()
        elif choice in self.sub_menus:
            self.sub_menus[choice].run()
        elif choice == 'b' and self.parent_menu:
            return True  # 返回上一级菜单
        elif choice == 'q':
            View.show_message("感谢使用，再见！")
            exit()
        else:
            View.show_message("无效的选项，请重试。")

    def run(self):
        while True:
            self.display()
            choice = View.get_message("请输入选项:")
            if self.execute(choice):
                break
