from model.model import BaseModel

class EmployeeModel(BaseModel):
    def __init__(self, database):
        self.table = database.get_table('employees')

    def add_employee(self, name):
        if not name:
            raise ValueError("员工名字不能为空")
        self.add({'name': name})

    def list_employees(self):
        return self.list()
