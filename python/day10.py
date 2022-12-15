import unittest
import re
from math import prod


def signal_strength(data):
    reg_X = 1
    state_history = [reg_X]

    for op in data:
        if V := re.match(r'addx (-?\d+)', op):
            state_history.append(reg_X)
            reg_X += int(V.group(1))
            state_history.append(reg_X)
        else:
            state_history.append(reg_X)

    return sum(
        state * (cycle + 1)
        for state, cycle in zip(state_history[19:220:40], range(19, 220, 40)))


class Solution(unittest.TestCase):

    def setUp(self):
        filename = "./data/10_e.txt"
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        self.data_example = data

        filename = "./data/10_i.txt"
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        self.data = data

    def test_part1_example(self):
        self.assertEqual(13140, signal_strength(self.data_example))

    def test_part1(self):
        self.assertEqual(15360, signal_strength(self.data))


if __name__ == '__main__':
    unittest.main()
