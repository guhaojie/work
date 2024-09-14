from core.menu import Menu

def register(menu, database):
    employee_menu = Menu('单位管理')

    def add_employee():
        print("添加员工功能")
        table = database.get_table('employees')
        name = input("输入员工名字: ")
        table.insert({'name': name})
        print(f"员工 {name} 已添加")

    def list_employees():
        table = database.get_table('employees')
        employees = table.all()
        print("员工列表:")
        for emp in employees:
            print(f"- {emp['name']}")

    employee_menu.register_option('2', '列出员工', list_employees)
    employee_menu.register_option('1', '添加员工', add_employee)

    menu.register_option('0', '单位管理', submenu=employee_menu)
