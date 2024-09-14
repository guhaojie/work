from core.menu import Menu
from core.database import Database
from core.plugin_manager import PluginManager

class MainController:
    def __init__(self):
        self.menu = Menu()
        self.database = Database()
        self.plugin_manager = PluginManager(self.menu, self.database)
        self.plugin_manager.load_plugins()

    def run(self):
        while True:
            self.menu.display()
            choice = input("输入选项: ").strip()
            self.menu.execute(choice)
