from aocd import data
from aocd import submit1, submit2

from itertools import cycle


def get_numbers():
    return map(int, data.splitlines())

def part1():
    frequency = sum(get_numbers())
    return frequency

def part2():
    device = cycle(get_numbers())
    frequencies = set()
    frequency = 0
    for change in device:
        frequency += change
        if frequency in frequencies:
            return frequency
        else:
            frequencies.add(frequency)

if __name__ == "__main__":
    answer1 = part1()
    submit1(answer1)

    answer2 = part2()
    submit2(answer2)
