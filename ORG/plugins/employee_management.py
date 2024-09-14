from view.menu import Menu
from view.view import View
from model.employee import EmployeeModel

def register(menu, database):
    employee_menu = Menu('员工管理')
    employee_model = EmployeeModel(database)

    def add_employee():
        View.show_level_2_title("添加员工")
        name = View.get_message("输入员工名字: ")
        employee_model.add_employee(name)
        View.show_notification(f"员工 {name} 已添加")

    def list_employees():
        employees = employee_model.list_employees()
        View.show_level_2_title("员工列表")
        for emp in employees:
            View.show_message(f"- {emp['name']}")
        View.show_notification("所有员工均已列出")

    employee_menu.register_option('1', '添加员工', add_employee)
    employee_menu.register_option('2', '列出员工', list_employees)

    menu.register_option('1', '员工管理', submenu=employee_menu)
