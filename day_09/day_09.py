import re
from collections import deque, defaultdict

from tqdm import tqdm

verbose = False


def p(*args, verbose=True):
    if verbose:
        print(*args)


def read_input(filepath):
    pattern = r'(\d+) players.* worth (\d+) points'
    with open(filepath) as f:
        strings = re.findall(pattern, f.read())
    numbers = [tuple(map(int, t)) for t in strings]
    if len(numbers) == 1:
        numbers = numbers[0]
    return numbers


def print_circle(circle, player, current_index, num_players, last_marble):
    BOLD = '\033[1m'
    END = '\033[0m'
    digits_players = len(str(num_players))
    digits_marbles = len(str(last_marble))
    player_string = f'[{player:{digits_players}}]'
    line = player_string
    for i, marble in enumerate(circle):
        if i == current_index:
            marble_string = f'({marble})'
            marble_string = f'{marble_string:>{digits_marbles + 2}}'
            marble_string = f'{BOLD}{marble_string}{END}'
        elif i == current_index + 1:
            marble_string = f'{marble:{digits_marbles}}'
        else:
            marble_string = f'{marble:{digits_marbles + 1}}'
        line += marble_string
    print(line)


def play(num_players, last_marble):
    scores = defaultdict(int)
    marble = 0
    circle = deque([marble])
    marbles = range(1, last_marble + 1)
    iterable = tqdm(marbles) if verbose else marbles
    for marble in iterable:
        player = marble % num_players
        if marble % 23:
            circle.rotate(-1)
            circle.append(marble)
        else:
            circle.rotate(7)
            removed = circle.pop()
            score = marble + removed
            scores[player] += score
            circle.rotate(-1)
    return circle, scores


def part_1(data):
    _, scores = play(*data)
    highest_score = max(scores.values())
    answer = highest_score
    return answer


def part_2(data):
    num_players, last_marble = data
    last_marble *= 100
    _, scores = play(num_players, last_marble)
    highest_score = max(scores.values())
    answer = highest_score
    return answer


if __name__ == "__main__":
    examples = read_input('example.txt')
    data = read_input('input.txt')

    p('Part 1', verbose=verbose)
    for example in examples:
        example_1 = part_1(example)
        p('Example 1:', example_1, verbose=verbose)
    answer_1 = part_1(data)
    p('Answer 1:', answer_1, verbose=verbose)

    p(verbose=verbose)

    p('Part 2', verbose=verbose)
    answer_2 = part_2(data)
    p('Answer 2:', answer_2, verbose=verbose)
