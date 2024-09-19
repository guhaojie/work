from config import BANNER
from core.base_cmd import MenuCMD


class Jarvis(MenuCMD):
    intro = BANNER + "Jarvis 欢迎您! 输入 help 或 ? 查看帮助。\n"
    prompt = 'Jarvis> '


if __name__ == '__main__':
    Jarvis().cmdloop()
