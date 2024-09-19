from core.base_cmd import MenuCMD


class Jarvis(MenuCMD):
    prompt = 'Jarvis> '

    def preloop(self):
        print("\nJarvis 欢迎您! 输入 help 或 ? 查看帮助。\n")


if __name__ == '__main__':
    Jarvis().cmdloop()
