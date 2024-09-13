import importlib
from plugins.employee_management import EmployeeModel, EmployeeView, EmployeeController


def load_plugin(plugin_name):
    try:
        module = importlib.import_module(f'plugins.{plugin_name}')
        return module
    except ModuleNotFoundError:
        print(f"插件 {plugin_name} 未找到。")
        return None


def main():
    plugins = {
        '1': 'employee_management',
    }

    while True:
        print("\n人事管理系统")
        print("1. 员工管理")
        print("q. 退出")

        choice = input("请选择一个选项: ")
        if choice == 'q':
            print("再见！")
            break
        elif choice in plugins:
            plugin = load_plugin(plugins[choice])
            if plugin:
                model = plugin.EmployeeModel()
                view = plugin.EmployeeView()
                controller = plugin.EmployeeController(model, view)
                controller.execute()
        else:
            print("无效选项，请重试。")


if __name__ == '__main__':
    main()
