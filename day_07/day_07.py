import re
from collections import defaultdict


def p(*args, verbose=True):
    if verbose:
        print(*args)


def read_input(filepath):
    with open(filepath) as f:
        text = f.read()
    pattern = re.compile(r'Step ([A-Z]) .* step ([A-Z])')
    pairs = pattern.findall(text)
    parents, children = zip(*pairs)
    all_chars = set(parents + children)
    nodes_map = {}
    for char in all_chars:
        nodes_map[char] = Node(char)
    for parent, child in pairs:
        nodes_map[parent].children.append(nodes_map[child])
        nodes_map[child].parents.append(nodes_map[parent])
    return list(nodes.values())


def get_tree_root(nodes):
    for node in nodes:
        if not node.parents:
            root = node
            break
    else:
        raise ValueError
    return root


def assemble(nodes):
    root = get_tree_root(nodes)
    available = [root]
    while available:
        root.



class Node:
    def __init__(self, step_id):
        self.id = step_id
        self.children = []
        self.parents = []
        self.assembled = False


    def __repr__(self):
        return f'{self.__class__.__name__}({self.id})'


    def assemble(self, available):
        self.assembled = True



def part_1(data):
    answer = None
    return answer


def part_2(data):
    answer = None
    return answer


if __name__ == "__main__":
    verbose = True

    example_1 = read_input('example_1.txt')
    print(example_1)
    print(get_tree_root(example_1))
    data = read_input('input.txt')

    p('Part 1', verbose=verbose)
    example_1 = part_1(example_1)
    p('Example:', example_1, verbose=verbose)
    # answer_1 = part_1(data)
    # p('Answer:', answer_1, verbose=verbose)

    # p(verbose=verbose)

    # p('Part 2', verbose=verbose)
    # example_2 = part_2(read_input('example_2.txt'))
    # p('Example:', example_2, verbose=verbose)
    # answer_2 = part_2(data)
    # p('Answer:', answer_2, verbose=verbose)
