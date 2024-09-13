import importlib


def load_plugin(plugin_name):
    try:
        module = importlib.import_module(f'plugins.{plugin_name}')
        return module
    except ModuleNotFoundError:
        print(f"插件 {plugin_name} 未找到。")
        return None


def main():
    plugins = {
        '1': ('employee_management', '员工管理'),
        '2': ('department_management', '单位管理'),
    }

    while True:
        print("\n人事管理系统")
        print("=" * 30)
        print("请选择一个功能模块:")
        for key, value in plugins.items():
            print(f"{key}. {value[1]}")
        print("q. 退出")
        print("=" * 30)

        choice = input("请输入选项: ")
        if choice == 'q':
            print("再见！")
            break
        elif choice in plugins:
            plugin = load_plugin(plugins[choice][0])
            if plugin:
                model = plugin.Model()
                view = plugin.View()
                controller = plugin.Controller(model, view)
                controller.execute()
        else:
            print("无效选项，请重试。")


if __name__ == '__main__':
    main()
