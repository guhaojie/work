from typing import TypeVar, Dict, List, Callable, Optional

Node: Dict[str, int | List[int | str]] = TypeVar('Node')
Tree: List[Node] = TypeVar('Tree')

Organization: Tree = []


def create_node(tree: Tree, parent_id: Optional[int] = 0, info: Optional[Dict] = None) -> int:
    """
    生成一个节点
    :param tree: 在何树增加？
    :param parent_id: 父节点为何？【可选】
    :param info: 节点信息为何？【可选】
    :return: 生成的节点
    """
    node: Node = {}
    tree.append(node)
    update_info(node, info={'id': tree.index(node),
                            'parent': parent_id,
                            'children': []})
    update_info(node, info)
    if node['id'] != 0:
        tree[parent_id]['children'].append(node['id'])
    return node['id']
def update_info(node: Node, info: Optional[Dict] = None) -> Node:
    """
    更新节点信息
    :param node: 需要更新信息的节点为何？
    :param info: 更新的信息为何？【可选】
    :return: 更新信息后的节点
    """
    node.update(info if info is not None else {})
    return node
def select_node(key: int | str, search_from: Tree, by: Callable) -> List[Node]:
    _x = []
    for _ in search_from:
        if by(_) == key:
            _x.append(_)
    return _x
def node_id(x: Node) -> int:
    return x.get('id', 0)
def parse_tree(tree: Tree, from_node: int, symbol: Optional[str] = "\\_") -> List[str]:
    _x = [f"{symbol}{tree[from_node]['id']}"]
    for _ in tree[from_node]['children']:
        _x += ["\t" + _ for _ in parse_tree(tree, _, symbol)]
    return _x
def print_tree(*args, **kwargs) -> None:
    for _ in parse_tree(*args, **kwargs):
        print(_)


r0 = create_node(Organization)
r1 = create_node(Organization, r0)
r2 = create_node(Organization, r0)
r3 = create_node(Organization, r1)
r4 = create_node(Organization, r1)
print_tree(tree=Organization, from_node=r0, symbol='|_')
print(select_node(key=1, search_from=Organization, by=node_id))
