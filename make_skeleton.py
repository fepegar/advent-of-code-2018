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

    data = read_input('input.txt')

    p('Part 1', verbose=verbose)
    example_1 = part_1(read_input('example_1.txt'))
    p('Example:', example_1, verbose=verbose)
    answer_1 = part_1(data)
    p('Answer:', answer_1, verbose=verbose)

    p(verbose=verbose)

    p('Part 2', verbose=verbose)
    example_2 = part_2(read_input('example_2.txt'))
    p('Example:', example_2, verbose=verbose)
    answer_2 = part_2(data)
    p('Answer:', answer_2, verbose=verbose)

"""

for i in range(25):
    day_string = f'day_{i + 1:02d}'
    day_dir = Path(day_string)
    code_path = day_dir / f'{day_string}.py'
    code_path.write_text(TEMPLATE)
    files = 'input', 'example_1', 'example_2'
    for filename in files:
        (day_dir / f'{filename}.txt').touch()
