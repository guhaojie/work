import uuid


def create_node(parent=None) -> dict:
    node = {'id': uuid.uuid1(),
            'parent': parent,
            'children': []}
    return node


def update_info(node: dict, info: dict) -> dict:
    node.update(info)
    return node


def add_child(parent: dict, info=None) -> dict:
    child = update_info(create_node(parent), info if info is not None else {})
    parent['children'].append(child)
    return child

def find_node(find_from: dict, key_words: str, by: str = 'name') -> list:
    match = []
    if find_from.get(by, "") == key_words:
        match.append(find_from)
    else:
        for _ in find_from['children']:
            match += find_node(_, key_words, by)
    return match


def print_tree(r: dict, k=None, indent: int = 0) -> None:
    k = ['id'] if k is None else k
    if r == {}:
        print(f'There is nothing in {r}.')
    else:
        print("\t" * indent, end="")
        print("\\_", end="")
        for _ in k:
            print(r.get(_, f"未发现 {_} 相关信息"), "\t", end="")
        print("\n", end="")
        for n in r['children']:
            print_tree(n, k, indent + 1)


ROOT = update_info(create_node(), info={'name': 'root'})
add_child(
    add_child(ROOT,
              info={'name': 'c1'}),
    info={'name': 'c2'})
add_child(
    add_child(
        add_child(
            add_child(ROOT,
                      info={'name': 'c3'}),
            info={'name': 'c4'}),
        info={'name': 'c5'}),
    info={'name': 'c6'})
add_child(ROOT, info={'name': 'c7'})
print_tree(ROOT, k=['name'])

print_tree(find_node(ROOT, 'c1')[0], k=['id', 'name'])
