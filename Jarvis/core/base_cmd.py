import cmd
import os
import importlib


class BaseCMD(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.load_commands()
        self.load_menus()

    def emptyline(self):
        pass

    def load_commands(self):
        command_dir = 'commands'
        for filename in os.listdir(command_dir):
            if filename.endswith('.py') and filename.startswith(f'cmd_{self.get_class_name()}'):
                module_name = filename[:-3]
                module = importlib.import_module(f'commands.{module_name}')
                callable_functions = [
                    func for name, func in module.__dict__.items()
                    if callable(func) and name.startswith('do_')
                ]
                for method in callable_functions:
                    setattr(self, method.__name__, method)

    def load_menus(self):
        command_dir = 'commands'
        for filename in os.listdir(command_dir):
            if filename.endswith('.py') and filename.startswith(f'menu_{self.get_class_name()}'):
                module_name = filename[:-3]
                module = importlib.import_module(f'commands.{module_name}')
                callable_functions = [
                    func for name, func in module.__dict__.items()
                    if callable(func) and name.startswith('do_')
                ]
                for method in callable_functions:
                    setattr(self, method.__name__, method)

    def get_class_name(self):
        return self.__class__.__name__.lower()

    def do_help(self, line):
        """列出所有命令和基本说明"""
        if line:
            super().do_help(line)
        else:
            print(f"\n命令列表: \n{'=' * 50}")
            for cmd_name in self.__dict__:
                if cmd_name.startswith('do_'):
                    print(f'- {cmd_name[3:]:<20}: {getattr(self, cmd_name).__doc__}')
            names = self.get_names()
            for name in names:
                if name[:3] == 'do_':
                    print(f'- {name[3:]:<20}: {getattr(self, name).__doc__}')
            print('')


class MenuCMD(BaseCMD):
    def do_exit(self, line):
        """退出"""
        print('再见!')
        exit()


class SubMenuCMD(MenuCMD):
    def do_back(self, line):
        """返回主菜单"""
        return True
