class Menu:
    def __init__(self):
        self.title = None
        self.options = {}
        self.sub_menus = {}

    def register_option(self, key, description, action=None, submenu=None):
        if submenu:
            self.sub_menus[key] = submenu
        else:
            self.options[key] = (description, action)

    def display(self):
        print("请选择一个选项:")
        for key, (description, _) in self.options.items():
            print(f"{key}. {description}")
        for key, submenu in self.sub_menus.items():
            print(f"{key}. {submenu.title}")

    def execute(self, choice):
        if choice in self.options:
            self.options[choice][1]()
        elif choice in self.sub_menus:
            self.sub_menus[choice].run()
        else:
            print("无效的选项")

    def set_title(self, title):
        self.title = title

    def run(self):
        while True:
            self.display()
            choice = input("输入选项: ").strip()
            self.execute(choice)
