import re
import sys
import numpy as np



class Fabric:
    def __init__(self, filepath):
        self.claims = self.read_claims(filepath)


    def print(self, file=sys.stdout):
        for row in self.get_aoc_fabric():
            for n in row:
                if n == 0:
                    print('.', end='', file=file)
                elif n == -1:
                    print('X', end='', file=file)
                else:
                    print(n, end='', file=file)
            print()


    def show(self):
        import matplotlib.pyplot as plt
        plt.imshow(self.get_aoc_fabric())
        plt.show()


    def read_claims(self, filepath):
        pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
        with open(filepath) as f:
            lines = re.findall(pattern, f.read())
        return [Claim(numbers) for numbers in lines]


    def get_shape(self):
        lefts = np.array([claim.left for claim in self.claims])
        tops = np.array([claim.top for claim in self.claims])
        widths = np.array([claim.width for claim in self.claims])
        heights = np.array([claim.height for claim in self.claims])
        rights = lefts + widths
        bottoms = tops + heights
        shape = bottoms.max() + 2 - tops.min(), rights.max() + 2 - lefts.min()
        return shape


    def get_overlap_fabric(self):
        shape = self.get_shape()
        fabric = np.zeros(shape, np.uint16)
        for claim in self.claims:
            i_ini = claim.top
            i_fin = i_ini + claim.height
            j_ini = claim.left
            j_fin = j_ini + claim.width
            fabric[i_ini:i_fin, j_ini:j_fin] += 1
        return fabric


    def get_aoc_fabric(self):
        shape = self.get_shape()
        fabric = np.zeros(shape, np.int16)
        for claim in self.claims:
            i_ini = claim.top
            i_fin = i_ini + claim.height
            j_ini = claim.left
            j_fin = j_ini + claim.width
            current_occupied = (fabric > 0) | (fabric == -1)
            new_fabric = np.zeros_like(fabric).astype(bool)
            new_fabric[i_ini:i_fin, j_ini:j_fin] = True
            overlap = current_occupied & new_fabric
            fabric[i_ini:i_fin, j_ini:j_fin] = claim.id
            fabric[overlap] = -1
        return fabric


    def get_overlap_inches(self):
        overlap = self.get_overlap_fabric() > 1
        num_overlap = overlap.sum()
        return num_overlap


    def get_correct_claim(self):
        fabric = self.get_aoc_fabric()
        for claim in self.claims:
            i_ini = claim.top
            i_fin = i_ini + claim.height
            j_ini = claim.left
            j_fin = j_ini + claim.width
            claim_fabric = np.zeros_like(fabric, bool)
            claim_fabric[i_ini:i_fin, j_ini:j_fin] = True
            claim_in_aoc_fabric = fabric == claim.id
            if np.array_equal(claim_in_aoc_fabric, claim_fabric):
                answer = claim.id
                break
        else:
            answer = None
            print('No correct claim was found')
        return answer



class Claim:
    def __init__(self, numbers):
        claim_id, left, top, width, height = [int(n) for n in numbers]
        self.id = claim_id
        self.left = left
        self.top = top
        self.width = width
        self.height = height


    def __repr__(self):
        string = (
            f'#{self.id} @ {self.left + 1},{self.top + 1}:'
            f' {self.width}x{self.height}'
        )
        return string


def p(*args, verbose=True):
    if verbose:
        print(*args)


def part_1(filepath):
    fabric = Fabric(filepath)
    answer = fabric.get_overlap_inches()
    return answer


def part_2(filepath):
    fabric = Fabric(filepath)
    # with open('fabric.txt', 'w') as f:
    #     fabric.print(file=f)
    answer = fabric.get_correct_claim()
    return answer


if __name__ == "__main__":
    verbose = True

    p('Part 1', verbose=verbose)
    example_1 = part_1('example_1.txt')
    p('Example:', example_1, verbose=verbose)
    answer_1 = part_1('input.txt')
    p('Answer:', answer_1, verbose=verbose)

    p(verbose=verbose)

    p('Part 2', verbose=verbose)
    example_2 = part_2('example_1.txt')
    p('Example:', example_2, verbose=verbose)
    answer_2 = part_2('input.txt')
    p('Answer:', answer_2, verbose=verbose)
