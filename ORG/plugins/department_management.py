from core.controller import BaseController
from core.model import BaseModel
from core.view import BaseView

class Model(BaseModel):
    def __init__(self):
        self.department = []

    def add_employee(self, name, position):
        self.employees.append({'name': name, 'position': position})

    def list_employees(self):
        return self.employees

    def remove_employee(self, name):
        self.employees = [emp for emp in self.employees if emp['name'] != name]

class View(BaseView):
    def get_department_details(self):
        name = self.get_input("请输入单位")
        return name

class Controller(BaseController):
    def execute(self):
        while True:
            self.view.display_menu({
                '1': '添加单位',
                '2': '列出单位',
                '3': '删除单位',
            }, title="单位管理")
            choice = self.view.get_input("请选择一个选项")

            if choice == '1':
                self.view.display_message("单位添加成功。")
            elif choice == '2':
                self.view.display_message("列出单位成功。")
            elif choice == '3':
                self.view.display_message("单位删除成功。")
            elif choice == 'b':
                break
            else:
                self.view.display_message("无效选项，请重试。")
