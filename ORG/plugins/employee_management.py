from core.menu import Menu

def register(menu, database):
    employee_menu = Menu()
    employee_menu.set_title('员工管理')

    def add_employee():
        print("添加员工功能")
        table = database.get_table('employees')
        name = input("输入员工名字: ")
        table.insert({'name': name})
        print(f"员工 {name} 已添加")

    employee_menu.register_option('1', '添加员工', add_employee)

    menu.register_option('1', '员工管理', submenu=employee_menu)
