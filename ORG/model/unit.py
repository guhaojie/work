from model.model import BaseModel

class UnitModel(BaseModel):
    def __init__(self, database):
        self.table = database.get_table('units')

    def add_unit(self, name):
        if not name:
            raise ValueError("单位名字不能为空")
        self.add({'name': name})

    def list_units(self):
        return self.list()
