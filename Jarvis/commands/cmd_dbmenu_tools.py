from tinydb import TinyDB
from config import DATABASE_PATH

db = TinyDB(DATABASE_PATH)

def do_add(line):
    """add <table_name> <data>"""
    s = line.split()
    tb = db.table(s[0])
    if not s[1]:
        print("内容不能为空")
    else:
        tb.insert({'name': s[1]})
        print(f'{s[1]} inserted in {s[0]}.')

def do_list(line):
    """list <table_name>"""
    tb = db.table(line)
    for _ in tb.all():
        print(f'- name: {_.get('name', 'Anonymous')}')
