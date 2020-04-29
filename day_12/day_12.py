from re import findall
from pathlib import Path
from copy import deepcopy
from collections import deque

this_dir = Path(__file__).parent
verbose = True


def p(*args):
    if verbose:
        print(*args)


def read_input(relative_filepath):
    filepath = this_dir / relative_filepath
    text = filepath.read_text()
    state = findall('initial state: ([#.]+)', text)[0]
    plants = [char == '#' for char in state]
    pots = [Pot(plant, i) for (i, plant) in enumerate(plants)]
    rules_pattern = r'([#.]+) .+ ([#.]).*'
    rules = [Rule(*groups) for groups in findall(rules_pattern, text)]
    return pots, rules


class Rule:
    def __init__(self, rule_string, result_char):
        self.string = rule_string
        self.result = result_char

    def __repr__(self):
        return f'{self.string}: {self.result}'


class Pot:
    def __init__(self, plant, number):
        self.plant = plant
        self.number = number

    def __repr__(self):
        return '#' if self.plant else '.'

    def get_neighborhood(self, pots):
        for i, pot in enumerate(pots):
            if pot.number == self.number:
                index_pots = i
                break
        neighbors = pots[index_pots - 2:index_pots + 3]
        neighborhood = ['#' if pot.plant else '.' for pot in neighbors]
        return ''.join(neighborhood)


    def evolve(self, pots, rule):
        neighborhood = self.get_neighborhood(pots)
        grow = rule.string == neighborhood
        return grow


def get_idx_extreme_pot(pots, left):
    for i, pot in enumerate(pots):
        if pot.plant:
            numbers = i, pot.number
            if left:
                return numbers
    return numbers


def expand_pots(pots):
    pots = deque(pots)
    expand_pots_left(pots)
    expand_pots_right(pots)
    return list(pots)


def expand_pots_left(pots):
    index, pot_number = get_idx_extreme_pot(pots, left=True)
    needed = 2 - index
    for i in range(needed):
        new_pot_number = pot_number - (i + 1)
        pot = Pot(plant=False, number=new_pot_number)
        pots.appendleft(pot)


def expand_pots_right(pots):
    index, pot_number = get_idx_extreme_pot(pots, left=False)
    needed = index + 2 - len(pots) + 1
    for i in range(needed):
        new_pot_number = pot_number + (i + 1)
        pot = Pot(plant=False, number=new_pot_number)
        pots.append(pot)


def print_pots(pots):
    for pot in pots:
        char = '#' if pot.plant else '.'
        char = pot.number
        print(char, end=' ')
    print()


def evolve(pots, rules, epochs=1):
    for _ in range(epochs):
        pots = expand_pots(pots)
        print_pots(pots)
        new_pots = deepcopy(pots)
        for new_pot in new_pots[2:-2]:
            for rule in rules:
                grow = new_pot.evolve(pots, rule)
                if grow:
                    new_pot.plant = True
                    break
            else:
                new_pot.plant = False
        pots = new_pots
    return pots


def part_1(data):
    pots, rules = data
    pots = evolve(pots, rules, epochs=20)
    answer = sum(pot.number for pot in pots if pot.plant)
    return answer


def part_2(data):
    answer = None
    return answer


if __name__ == "__main__":
    example = read_input('example.txt')
#     data = read_input('input.txt')

    p('Part 1')
    example_1 = part_1(example)
    p('Example 1:', example_1)
#     answer_1 = part_1(data)
#     p('Answer 1:', answer_1)

#     p()

#     p('Part 2')
#     example_2 = part_2(example)
#     p('Example 2:', example_2)
#     answer_2 = part_2(data)
#     p('Answer 2:', answer_2)
