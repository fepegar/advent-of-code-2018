import re
from collections import defaultdict
from datetime import date, time, datetime

import numpy as np

WAKE_UP = 0
FALL_ASLEEP = 1


class Annotation:
    def __init__(self, parts):
        numbers = parts[:-1]
        self.string = parts[-1]
        year, month, day, hour, minute = [int(n) for n in numbers]
        self.date = date(year, month, day)
        self.time = time(hour, minute)
        self.datetime = datetime(year, month, day, hour, minute)
        self.guard_id = None
        self.action = None

        guard_match = re.findall(r'#(\d+)', self.string)
        if guard_match:
            self.guard_id = int(guard_match[0])
        elif self.string == 'falls asleep':
            self.action = FALL_ASLEEP
        elif self.string == 'wakes up':
            self.action = WAKE_UP


    def __repr__(self):
        return f'{self.datetime} - {self.string}'



class Day:
    def __init__(self, date, guard_id, actions):
        self.date = date
        self.guard_id = guard_id
        self.array = self.get_array(actions)


    def __repr__(self):
        return f'{self.date}: {self.guard_id:6} - {self.get_actions_string()}'


    @property
    def minutes_asleep(self):
        return int(self.array.sum())


    def get_actions_string(self):
        string = ''.join('.' if n == WAKE_UP else '#' for n in self.array)
        return string


    def get_array(self, actions):
        array = np.zeros(60)
        for time, action in actions:
            array[time.minute:] = action
        return array



def read_input(filepath):
    pattern = r'\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (.*)'
    with open(filepath) as f:
        matches = re.findall(pattern, f.read())
    annotations = [Annotation(match) for match in matches]
    annotations = sorted(annotations, key=lambda ann: ann.datetime)
    days = []
    guard_id = None
    actions = []
    date = annotations[1].date
    for i, annotation in enumerate(annotations):
        if annotation.guard_id is not None:
            if actions:
                days.append(Day(date, guard_id, actions))
                actions = []
            guard_id = annotation.guard_id
            date = annotations[i + 1].date
        else:
            actions.append((annotation.time, annotation.action))
    days.append(Day(date, guard_id, actions))
    return days


def find_most_asleep(days):
    guards = defaultdict(int)
    for day in days:
        guards[day.guard_id] += day.minutes_asleep
    ids = list(guards.keys())
    minutes = np.array(list(guards.values()))
    max_idx = np.argmax(minutes)
    return ids[max_idx]


def filter_days_by_guard_id(days, guard_id):
    return [day for day in days if day.guard_id == guard_id]


def get_guard_matrix(days, guard_id):
    guard_days = filter_days_by_guard_id(days, guard_id)
    matrix = np.row_stack([day.array for day in guard_days])
    return matrix


def find_best_minute(days, guard_id):
    matrix = get_guard_matrix(days, guard_id)
    best_minute = np.argmax(matrix.sum(axis=0))
    return best_minute


def find_most_asleep_minute(days):
    max_asleep_minute = None
    max_guard_id = None
    max_days_asleep = -np.infty
    guard_ids = set(day.guard_id for day in days)
    for guard_id in guard_ids:
        matrix = get_guard_matrix(days, guard_id)
        days_asleep = matrix.sum(axis=0)
        if days_asleep.max() > max_days_asleep:
            max_days_asleep = days_asleep.max()
            max_asleep_minute = np.argmax(days_asleep)
            max_guard_id = guard_id
    return max_guard_id, max_asleep_minute


def part_1(days):
    guard_id = find_most_asleep(days)
    minute = find_best_minute(days, guard_id)
    return guard_id * minute


def part_2(days):
    guard_id, minute = find_most_asleep_minute(days)
    return guard_id * minute


if __name__ == "__main__":
    data = read_input('input.txt')

    print('Part 1')
    data_example = read_input('example_1.txt')
    example_1 = part_1(data_example)
    print('Example:', example_1)
    answer_1 = part_1(data)
    print('Answer:', answer_1)

    print()

    print('Part 2')
    example_2 = part_2(data_example)
    print('Example:', example_2)
    answer_2 = part_2(data)
    print('Answer:', answer_2)
