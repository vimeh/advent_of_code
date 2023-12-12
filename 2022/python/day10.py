import unittest
import re
from math import prod


def get_state_history(data):
    reg_X = 1
    state_history = [reg_X]

    for op in data:
        if V := re.match(r'addx (-?\d+)', op):
            state_history.append(reg_X)
            reg_X += int(V.group(1))
            state_history.append(reg_X)
        else:
            state_history.append(reg_X)

    return state_history


def signal_strength(data):
    state_history = get_state_history(data)
    return sum(
        state * (cycle + 1)
        for state, cycle in zip(state_history[19:220:40], range(19, 220, 40)))


def draw(data, path=None):
    state_history = get_state_history(data)

    screen = []

    for line in [
            state_history[start:end]
            for start, end in zip(range(0, 201, 40), range(40, 241, 40))
    ]:
        row = ''
        for cycle, pos in enumerate(line):
            if cycle in [*range(pos - 1, pos + 2)]:
                row += '#'
            else:
                row += '.'

        screen.append(''.join(row))

    if path:
        with open(path, 'w') as f:
            f.write('\n'.join(screen))

    return screen


class Solution(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

        filename = "./data/10_e.txt"
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        self.data_example = data

        filename = "./data/10_i.txt"
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        self.data = data

        filename = "./data/10_e2.txt"
        with open(filename, 'r') as f:
            result = f.read().splitlines()

        self.result_example = result

        filename = "./data/10_out.txt"
        with open(filename, 'r') as f:
            result = f.read().splitlines()

        self.result = result

    def test_part1_example(self):
        self.assertEqual(13140, signal_strength(self.data_example))

    def test_part1(self):
        self.assertEqual(15360, signal_strength(self.data))

    def test_part2_example(self):
        self.assertEqual(self.result_example, draw(self.data_example))

    def test_part2(self):
        self.assertEqual(self.result, draw(self.data))


if __name__ == '__main__':
    unittest.main()
