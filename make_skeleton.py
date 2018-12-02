from pathlib import Path

TEMPLATE = """


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
    print('Part 1')
    example_1 = part_1('example_1.txt')
    print('Example:', example_1)
    answer_1 = part_1('input.txt')
    print('Answer:', answer_1)

    print()

    print('Part 2')
    example_2 = part_2('example_2.txt')
    print('Example:', example_2)
    answer_2 = part_2('input.txt')
    print('Answer:', answer_2)

"""

for i in range(3, 26):
    day_string = f'day_{i:02d}'
    day_dir = Path(day_string)
    code_path = day_dir / f'{day_string}.py'
    code_path.write_text(TEMPLATE)
    (day_dir / 'input.txt').touch()
    (day_dir / 'example_1.txt').touch()
    (day_dir / 'example_2.txt').touch()
