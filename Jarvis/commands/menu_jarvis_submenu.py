from core.base_cmd import SubMenuCMD


class SubMenu(SubMenuCMD):
    prompt = "Jarvis-submenu> "


def do_submenu(arg):
    """进入submenu"""
    SubMenu().cmdloop()
