import re
from pathlib import Path

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

this_dir = Path(__file__).parent
verbose = True


def p(*args):
    if verbose:
        print(*args)


def read_input(relative_filepath):
    filepath = this_dir / relative_filepath
    text = filepath.read_text()
    pattern = r'<\s*(-?\d+),\s*(-?\d+)>[^<>]+<\s*(-?\d+),\s*(-?\d+)>'
    lines = re.findall(pattern, text)
    array = np.array(lines, dtype=int)
    return array



class Point:
    def __init__(self, chars):
        numbers = [int(char) for char in chars]
        self.x, self.y, self.vx, self.vy = numbers

    def move(self):
        self.x += self.vx
        self.y += self.vy


def part_1(array):
    p = array[:, :2]
    v = array[:, 2:]
    fig, ax = plt.subplots()
    figures_dir = this_dir / 'figures'
    if figures_dir.is_dir():
        import shutil
        shutil.rmtree(figures_dir)
    figures_dir.mkdir(exist_ok=True)
    n = 0
    p += 10634 * v
    x, y = p.T
    handle = ax.scatter(x, y, 1)
    ax.axis('equal')
    ax.invert_yaxis()
    plt.show()
#     for i in tqdm(range(20000)):
#         if i > 10600 and i < 10700: # and i % 100 == 0:
#             fig.savefig(figures_dir / f'frame_{n}.png')
#         #     reply = input('Continue? [y]/n\n')
#         #     if reply != 'y':
#         #         break
#         p += v
#         n += 1
#         x, y = p.T
#         handle.set_offsets(p)
#         ax.set_xlim(x.min(), x.max())
#         # ax.set_xlim(-1000, 1000)
#         ax.set_ylim(y.min(), y.max())
#         # ax.set_ylim(-1000, 1000)


def part_2(data):
    answer = None
    return answer


if __name__ == "__main__":
    example = read_input('example.txt')
    data = read_input('input.txt')

#     p('Part 1')
#     example_1 = part_1(example)
#     p('Example 1:', example_1)
#     answer_1 = part_1(data)

#     p()

#     p('Part 2')
#     example_2 = part_2(example)
#     p('Example 2:', example_2)
#     answer_2 = part_2(data)
#     p('Answer 2:', answer_2)
