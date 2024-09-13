from core.controller import BaseController
from core.model import BaseModel
from core.view import BaseView

class Model(BaseModel):
    def __init__(self):
        self.employees = []

    def add_employee(self, name, position):
        self.employees.append({'name': name, 'position': position})

    def list_employees(self):
        return self.employees

    def remove_employee(self, name):
        self.employees = [emp for emp in self.employees if emp['name'] != name]

class View(BaseView):
    def get_employee_details(self):
        name = self.get_input("请输入员工姓名")
        position = self.get_input("请输入员工职位")
        return name, position

    def display_employees(self, employees):
        self.display_section_title("员工列表")
        if not employees:
            self.display_message("当前没有员工。")
        else:
            for emp in employees:
                self.display_message(f"姓名: {emp['name']}, 职位: {emp['position']}")

    def get_employee_name(self):
        return self.get_input("请输入要删除的员工姓名")

class Controller(BaseController):
    def execute(self):
        while True:
            self.view.display_menu({
                '1': '添加员工',
                '2': '列出员工',
                '3': '删除员工',
            }, title="员工管理")
            choice = self.view.get_input("请选择一个选项")

            if choice == '1':
                name, position = self.view.get_employee_details()
                self.model.add_employee(name, position)
                self.view.display_message("员工添加成功。")
            elif choice == '2':
                employees = self.model.list_employees()
                self.view.display_employees(employees)
            elif choice == '3':
                name = self.view.get_employee_name()
                self.model.remove_employee(name)
                self.view.display_message("员工删除成功。")
            elif choice == 'b':
                break
            else:
                self.view.display_message("无效选项，请重试。")
