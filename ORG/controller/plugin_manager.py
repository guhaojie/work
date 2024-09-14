import os
import importlib

class PluginManager:
    def __init__(self, main_menu, database):
        self.main_menu = main_menu
        self.plugin_folder = 'plugins'
        self.database = database

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module = importlib.import_module(f'{self.plugin_folder}.{module_name}')
                module.register(self.main_menu, self.database)
