from core.base_cmd import SubMenuCMD


class dbMenu(SubMenuCMD):
    prompt = "Jarvis-dbMenu> "


def do_db(line):
    """进入db menu"""
    dbMenu().cmdloop()
