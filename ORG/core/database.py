from tinydb import TinyDB

class Database:
    def __init__(self, db_path='db.json'):
        self.db = TinyDB(db_path)

    def get_table(self, table_name):
        return self.db.table(table_name)
