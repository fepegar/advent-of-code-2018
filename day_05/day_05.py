import sys
import numpy as np

DIFF_CASE = 32  # distance between lower and upper case in ASCII


def p(*args, verbose=True):
    if verbose:
        print(*args)


def read_input(filepath):
    with open(filepath) as f:
        data = f.read().rstrip()
    return data


def encode_polymer(string):
    chars = [ord(c) for c in string]
    return np.array(chars)


def decode_polymer(numbers):
    chars = [chr(n) for n in numbers]
    return ''.join(chars)


def react(polymer):
    diffs = np.abs(np.diff(polymer))
    reactions = diffs == DIFF_CASE
    if reactions.any():
        index = np.flatnonzero(reactions)[0]
        polymer = np.delete(polymer, [index, index + 1])
        return react(polymer)
    else:
        return polymer


def remove_monomers(string, char):
    lower = char
    upper = char.upper()
    stripped = string.replace(lower, '').replace(upper, '')
    return stripped


def get_length_shortest_polymer(string):
    all_chars = set(string.lower())
    lengths = {}  # instead of list, for debugging
    for char in all_chars:
        substring = remove_monomers(string, char)
        polymer = encode_polymer(substring)
        resulting_polymer = decode_polymer(react(polymer))
        lengths[char] = len(resulting_polymer)
    return min(lengths.values())


def part_1(string):
    polymer = encode_polymer(string)
    resulting_polymer = decode_polymer(react(polymer))
    answer = len(resulting_polymer)
    return answer


def part_2(string):
    answer = get_length_shortest_polymer(string)
    return answer


if __name__ == "__main__":
    verbose = True

    data = read_input('input.txt')

    # Maximum level of recursion was being reached
    sys.setrecursionlimit(len(data))

    p('Part 1', verbose=verbose)
    example_1 = part_1(read_input('example_1.txt'))
    p('Example:', example_1, verbose=verbose)
    answer_1 = part_1(data)
    p('Answer:', answer_1, verbose=verbose)

    # p(verbose=verbose)

    p('Part 2', verbose=verbose)
    example_2 = part_2(read_input('example_1.txt'))
    p('Example:', example_2, verbose=verbose)
    answer_2 = part_2(data)
    p('Answer:', answer_2, verbose=verbose)
