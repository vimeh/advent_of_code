import unittest
from math import prod


def get_visible_trees(grid):
    M, N = len(grid), len(grid[0])
    # edge trees always visible
    visible = 2 * M + 2 * (N - 2)

    grid_t = [*zip(*grid)]

    for m in range(1, M - 1):
        row = grid[m]
        for n in range(1, N - 1):
            col = grid_t[n]
            val = grid[m][n]

            runs = (row[n - 1::-1], row[n + 1:], col[m - 1::-1], col[m + 1:])
            visible += any(all(x < val for x in run) for run in runs)

    return visible


def get_max_score(grid):
    M, N = len(grid), len(grid[0])

    grid_t = [*zip(*grid)]

    max_score = 0
    for m in range(1, M - 1):
        row = grid[m]
        for n in range(1, N - 1):
            col = grid_t[n]
            val = grid[m][n]

            runs = (row[n - 1::-1], row[n + 1:], col[m - 1::-1], col[m + 1:])

            score = prod(
                next((k + 1 for k, t in enumerate(run) if t >= val), len(run))
                for run in runs)
            max_score = max(max_score, score)

    return max_score


class Tests(unittest.TestCase):

    def setUp(self):
        filename = 'data/08_e.txt'
        with open(filename) as f:
            data = f.read().splitlines()

        self.data_example = [[int(x) for x in line] for line in data]

        filename = 'data/08_i.txt'
        with open(filename) as f:
            data = f.read().splitlines()

        self.data = [[int(x) for x in line] for line in data]

    def test_part1_example(self):
        self.assertEqual(21, get_visible_trees(self.data_example))

    def test_part1(self):
        self.assertEqual(1703, get_visible_trees(self.data))

    def test_part2_example(self):
        self.assertEqual(8, get_max_score(self.data_example))

    def test_part2(self):
        self.assertEqual(496650, get_max_score(self.data))


if __name__ == '__main__':
    unittest.main()
