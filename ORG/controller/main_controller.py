from view.menu import Menu
from model.database import Database
from controller.plugin_manager import PluginManager

class MainController:
    def __init__(self):
        self.menu = Menu()
        self.database = Database()
        self.plugin_manager = PluginManager(self.menu, self.database)
        self.plugin_manager.load_plugins()

    def run(self):
        self.menu.run()
