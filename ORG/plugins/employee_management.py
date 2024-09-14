from core.menu import Menu
from core.view import View

def register(menu, database):
    employee_menu = Menu('员工管理')

    def add_employee():
        View.show_level_2_title("添加员工功能")
        table = database.get_table('employees')
        name = View.get_message("输入员工名字: ")
        table.insert({'name': name})
        View.show_message(f"员工 {name} 已添加")

    def list_employees():
        table = database.get_table('employees')
        employees = table.all()
        View.show_level_2_title("员工列表:")
        for emp in employees:
            View.show_message(f"- {emp['name']}")

    employee_menu.register_option('1', '添加员工', add_employee)
    employee_menu.register_option('2', '列出员工', list_employees)

    menu.register_option('1', '员工管理', submenu=employee_menu)
