from view.menu import Menu
from view.view import View
from model.unit import UnitModel

def register(menu, database):
    unit_menu = Menu('单位管理')
    unit_model = UnitModel(database)

    def add_unit():
        View.show_level_2_title("添加单位")
        name = View.get_message("输入单位名字: ")
        unit_model.add_unit(name)
        View.show_notification(f"单位 {name} 已添加")

    def list_units():
        units = unit_model.list_units()
        View.show_level_2_title("单位列表")
        count = 0
        for uni in units:
            View.show_message(f"{uni.doc_id:>2}. {uni['name']}\t", end="")
            count += 1
            if count % 4 == 0:
                print('')
        print('')

    def show_all_units():
        list_units()
        View.show_notification("所有单位均已列出")

    def choose_a_unit():
        list_units()
        unit_no = View.get_message("输入一个单位的序号：")
        name = unit_model.get_by_id(unit_no).get('name', None)
        View.show_notification(f"单位 {name} 已选择")

    unit_menu.register_option('1', '添加单位', add_unit)
    unit_menu.register_option('2', '列出单位', show_all_units)
    unit_menu.register_option('3', '选择单位', choose_a_unit)

    menu.register_option('0', '单位管理', submenu=unit_menu)
