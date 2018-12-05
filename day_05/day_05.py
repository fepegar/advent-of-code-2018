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
    while True:
        diffs = np.abs(np.diff(polymer))
        reactions = diffs == DIFF_CASE
        if not reactions.any():
            break
        # Where two letters are going to disappear
        indices = np.flatnonzero(reactions)
        # But not if there are three together
        indices = np.delete(indices, np.flatnonzero(np.diff(indices) == 1) + 1)
        polymer = np.delete(polymer, [indices, indices + 1])
    return polymer


def remove_monomers(string, char):
    lower = char
    upper = char.upper()
    stripped = string.replace(lower, '').replace(upper, '')
    return stripped


def get_length_shortest_polymer(string):
    all_chars = set(string.lower())
    lengths = np.empty(len(all_chars), np.uint16)
    for i, char in enumerate(all_chars):
        substring = remove_monomers(string, char)
        polymer = encode_polymer(substring)
        resulting_polymer = decode_polymer(react(polymer))
        lengths[i] = len(resulting_polymer)
    return lengths.min()


def part_1(string):
    polymer = encode_polymer(string)
    short_polymer = react(polymer)
    result_string = decode_polymer(short_polymer)
    return result_string


def part_2(string):
    answer = get_length_shortest_polymer(string)
    return answer


if __name__ == "__main__":
    verbose = False

    example_data = read_input('example_1.txt')
    data = read_input('input.txt')

    p('Part 1', verbose=verbose)
    example_result_string = part_1(example_data)
    example_1 = len(example_result_string)
    p('Example:', example_1, verbose=verbose)
    result_string = part_1(data)
    answer_1 = len(result_string)
    p('Answer:', answer_1, verbose=verbose)

    p(verbose=verbose)

    p('Part 2', verbose=verbose)
    example_2 = part_2(example_result_string)
    p('Example:', example_2, verbose=verbose)
    answer_2 = part_2(result_string)
    p('Answer:', answer_2, verbose=verbose)
