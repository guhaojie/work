from tinydb import TinyDB
from config import DATABASE_PATH

class Database:
    def __init__(self, db_path=DATABASE_PATH):
        self.db = TinyDB(db_path)

    def get_table(self, table_name):
        return self.db.table(table_name)
