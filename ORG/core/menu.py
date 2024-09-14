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
        print(f"\n==== {self.title} ====")
        for key, (description, _) in self.options.items():
            print(f"{key}. {description}")
        for key, submenu in self.sub_menus.items():
            print(f"{key}. {submenu.title}")
        if self.parent_menu:
            print("b. 返回")
        else:
            print("q. 退出")

    def execute(self, choice):
        if choice in self.options:
            self.options[choice][1]()
        elif choice in self.sub_menus:
            self.sub_menus[choice].run()
        elif choice == 'b' and self.parent_menu:
            return True  # 返回上一级菜单
        elif choice == 'q':
            print("感谢使用，再见！")
            exit()
        else:
            print("无效的选项，请重试。")

    def run(self):
        while True:
            self.display()
            choice = input("请输入选项: ").strip()
            if self.execute(choice):
                break
