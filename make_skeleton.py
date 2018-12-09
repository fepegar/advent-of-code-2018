from pathlib import Path

TEMPLATE = """


def p(*args, verbose=True):
    if verbose:
        print(*args)


def read_input(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    return lines


def part_1(data):
    answer = None
    return answer


def part_2(data):
    answer = None
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

"""

for i in range(8, 25):
    day_string = f'day_{i + 1:02d}'
    day_dir = Path(day_string)
    day_dir.mkdir(exist_ok=True)
    code_path = day_dir / f'{day_string}.py'
    code_path.write_text(TEMPLATE)
    files = 'input', 'example'
    for filename in files:
        (day_dir / f'{filename}.txt').touch()
