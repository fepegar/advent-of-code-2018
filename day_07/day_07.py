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
    nodes_list = sorted(list(nodes_map.values()), key=lambda node: node.id)
    return nodes_list


def get_tree_roots(nodes):
    roots = [node for node in nodes if not node.parents]
    return roots


def assemble_nodes(nodes):
    roots = get_tree_roots(nodes)
    available = roots
    result = []
    while available:
        available.sort(reverse=True, key=lambda node: node.id)
        node = available.pop()
        node.assemble(available)
        result.append(node.id)
    return ''.join(result)


def assemble_nodes_delay(nodes, workers):
    roots = get_tree_roots(nodes)
    available = roots
    result = []
    second = 0
    workers_columns = [f'W {i}' for i in range(len(workers))]
    columns = ['Second'] + workers_columns + ['Done']
    print('\t'.join(columns))
    while len(result) < len(nodes): # ? available:
        available.sort(reverse=True, key=lambda node: node.id)
        for worker in workers:
            if worker.is_idle and available:
                worker.node = available.pop()
        workers_columns = [worker.node.id if worker.node is not None else '.' for worker in workers]
        columns = [str(second)] + workers_columns + [''.join(result)]
        print('\t'.join(columns))
        for worker in workers:
            node = worker.work(available)
            if node is not None:
                result.append(node.id)
        second += 1
    return ''.join(result)



class Node:
    def __init__(self, step_id):
        self.id = step_id
        self.children = []
        self.parents = []
        self.assembled = False
        self.seconds = 60 + ord(self.id) - ord('A') + 1


    def __repr__(self):
        return f'{self.__class__.__name__}({self.id})'


    def assemble(self, available):
        self.assembled = True
        for child in self.children:
            if child.parents_assembled():
                available.append(child)


    def parents_assembled(self):
        assembled = [parent.assembled for parent in self.parents]
        return all(assembled)



class Worker:
    def __init__(self):
        self.node = None

    @property
    def is_idle(self):
        return self.node is None

    def work(self, available):
        if self.is_idle:
            return
        else:
            self.node.seconds -= 1
            if self.node.seconds == 0:
                self.node.assemble(available)
                node = self.node
                self.node = None
                return node




def part_1(nodes):
    answer = assemble_nodes(nodes)
    return answer


def part_2(nodes, num_workers, short=False):
    if short:
        for node in nodes:
            node.seconds -= 60
    workers = [Worker() for _ in range(num_workers)]
    answer = assemble_nodes_delay(nodes, workers)
    return answer


if __name__ == "__main__":
    verbose = True

    example_data = read_input('example_1.txt')
    input_data = read_input('input.txt')

    p('Part 1', verbose=verbose)
    example_1 = part_1(example_data)
    p('Example 1:', example_1, verbose=verbose)
    answer_1 = part_1(input_data)
    p('Answer 1:', answer_1, verbose=verbose)

    p(verbose=verbose)

    p('Part 2', verbose=verbose)
    example_2 = part_2(example_data, 2, short=True)
    p('Example:', example_2, verbose=verbose)
    # answer_2 = part_2(input_data)
    # p('Answer:', answer_2, verbose=verbose)
