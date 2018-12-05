from itertools import combinations
from collections import defaultdict


def p(*args, verbose=True):
    if verbose:
        print(*args)


def get_boxes(filepath):
    with open(filepath) as f:
        boxes_ids = f.read().splitlines()
    return boxes_ids


def get_counts(string):
    counts = defaultdict(int)
    for letter in string:
        counts[letter] += 1
    twice = 1 if 2 in counts.values() else 0
    thrice = 1 if 3 in counts.values() else 0
    return twice, thrice


def get_checksum(filepath):
    twice_total = 0
    thrice_total = 0
    for box_id in get_boxes(filepath):
        twice, thrice = get_counts(box_id)
        twice_total += twice
        thrice_total += thrice
    checksum = twice_total * thrice_total
    return checksum


def are_correct(box_a, box_b):
    differents = sum([a != b for (a, b) in zip(box_a, box_b)])
    return differents == 1


def letters_in_common(box_a, box_b):
    return ''.join([a for (a, b) in zip(box_a, box_b) if a == b])


def find_correct_boxes(filepath):
    for box_a, box_b in combinations(get_boxes(filepath), 2):
        if are_correct(box_a, box_b):
            answer = letters_in_common(box_a, box_b)
            break
    else:
        print('No correct boxes found')
        answer = None
    return answer


if __name__ == "__main__":
    verbose = False
    p('Part 1', verbose=verbose)
    example_1 = get_checksum('example_1.txt')
    p('Example:', example_1, verbose=verbose)
    part_1 = get_checksum('box_ids.txt')
    p('Answer:', part_1, verbose=verbose)

    p(verbose=verbose)

    p('Part 2', verbose=verbose)
    example_2 = find_correct_boxes('example_2.txt')
    p('Example:', example_2, verbose=verbose)
    part_2 = find_correct_boxes('box_ids.txt')
    p('Answer:', part_2, verbose=verbose)
