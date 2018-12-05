from itertools import cycle


def get_numbers():
    with open('input.txt') as f:
        data = f.read()
    return map(int, data.splitlines())

def part1(numbers):
    frequency = sum(numbers)
    return frequency

def part2(numbers):
    device = cycle(numbers)
    frequencies = set()
    frequency = 0
    for change in device:
        frequency += change
        if frequency in frequencies:
            return frequency
        else:
            frequencies.add(frequency)

if __name__ == "__main__":
    numbers = get_numbers()
    answer1 = part1(numbers)
    answer2 = part2(numbers)
