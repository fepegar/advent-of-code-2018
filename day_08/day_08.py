from collections import deque
from string import ascii_uppercase

from graphviz import Digraph


def p(*args, verbose=True):
    if verbose:
        print(*args)


def read_input(filepath):
    with open(filepath) as f:
        numbers = [int(c) for c in f.read().split()]
    tree = Tree(numbers)
    return tree


class Node:
    def __init__(self, node_id, num_children, num_metadata):
        self.id = str(node_id)
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.children_left = self.num_children
        self.children = []
        self.metadata_entries = None
        # print('New node:', self, num_children, self.num_metadata)

    def __repr__(self):
        return self.id

    def get_value(self):
        if not self.children:
            value = sum(self.metadata_entries)
        else:
            values = []
            for entry in self.metadata_entries:
                try:
                    child = self.children[entry - 1]
                    values.append(child.get_value())
                except IndexError:
                    pass
            value = sum(values)
        return value

    def add_child(self, node):
        self.children.append(node)
        self.children_left -= 1

    def add_metadata(self):
        return sum(self.metadata_entries)

    def read_metadata(self, queue):
        self.metadata_entries = [
            queue.popleft() for _ in range(self.num_metadata)]



class Tree:
    def __init__(self, numbers):
        queue = deque(numbers)
        # ids = list(reversed(ascii_uppercase))
        num_children = queue.popleft()
        num_metadata = queue.popleft()
        node_id = 0
        self.root = Node(node_id, num_children, num_metadata)
        node_id += 1
        self.nodes = [self.root]
        stack = [self.root]
        while stack:
            if stack[-1].children_left > 0:
                num_children = queue.popleft()
                num_metadata = queue.popleft()
                node = Node(node_id, num_children, num_metadata)
                node_id += 1
                stack[-1].add_child(node)
                stack.append(node)
                self.nodes.append(node)
            else:
                stack[-1].read_metadata(queue)
                stack.pop()

    def get_checksum(self):
        return sum(node.add_metadata() for node in self.nodes)

    def get_graph(self):
        dot = Digraph()
        for node in self.nodes:
            dot.node(node.id)
        for parent in self.nodes:
            for child in parent.children:
                dot.edge(parent.id, child.id)
        return dot

    def get_value(self):
        return self.root.get_value()



def part_1(tree):
    answer = tree.get_checksum()
    return answer


def part_2(tree):
    answer = tree.get_value()
    return answer


if __name__ == "__main__":
    verbose = True

    example = read_input('example.txt')
    data = read_input('input.txt')

    p('Part 1', verbose=verbose)
    example_1 = part_1(example)
    p('Example 1:', example_1, verbose=verbose)
    answer_1 = part_1(data)
    p('Answer 1:', answer_1, verbose=verbose)

    p(verbose=verbose)

    p('Part 2', verbose=verbose)
    example_2 = part_2(example)
    p('Example 2:', example_2, verbose=verbose)
    answer_2 = part_2(data)
    p('Answer 2:', answer_2, verbose=verbose)
