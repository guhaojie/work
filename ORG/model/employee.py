class EmployeeModel:
    def __init__(self, database):
        self.table = database.get_table('employees')

    def add_employee(self, name):
        if not name:
            raise ValueError("员工名字不能为空")
        self.table.insert({'name': name})

    def list_employees(self):
        return self.table.all()
