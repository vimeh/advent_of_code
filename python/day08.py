import unittest
import numpy as np


def get_visible_trees(grid):
    M, N = grid.shape

    # edge trees always visible
    visible = 2 * M + 2 * (N - 2)

    for n in range(1, N - 1):
        for m in range(1, M - 1):
            vis_up = all(grid[m][n] > x for x in grid[:m, n])
            vis_dn = all(grid[m][n] > x for x in grid[m + 1:, n])
            vis_lt = all(grid[m][n] > x for x in grid[m, :n])
            vis_rt = all(grid[m][n] > x for x in grid[m, n + 1:])

            if vis_up or vis_dn or vis_lt or vis_rt:
                visible += 1

    return visible


def get_max_score(grid):
    M, N = grid.shape

    def num_trees(val, line):
        line = np.atleast_1d(line)
        for i, x in np.ndenumerate(line):
            if x >= val:
                return i[0] + 1

        return line.size

    max_score = 0
    for m in range(1, M - 1):
        for n in range(1, N - 1):
            val = grid[m, n]
            score = num_trees(val, np.flip(grid[:m, n])) * num_trees(
                val, grid[m + 1:, n]) * num_trees(val, np.flip(
                    grid[m, :n])) * num_trees(val, grid[m, n + 1:])
            max_score = max(max_score, score)

    return max_score


class Tests(unittest.TestCase):

    def setUp(self):
        filename = 'data/08_e.txt'
        with open(filename) as f:
            data = f.read().splitlines()

        for i in range(len(data)):
            data[i] = [int(x) for x in data[i]]

        self.data_example = np.array(data)

        filename = 'data/08_i.txt'
        with open(filename) as f:
            data = f.read().splitlines()

        for i in range(len(data)):
            data[i] = [int(x) for x in data[i]]

        self.data = np.array(data)

    def test_part1_example(self):
        self.assertEqual(21, get_visible_trees(self.data_example))

    def test_part1(self):
        self.assertEqual(1703, get_visible_trees(self.data))

    def test_part2_example(self):
        self.assertEqual(8, get_max_score(self.data_example))

    def test_part2(self):
        self.assertEqual(8, get_max_score(self.data))


if __name__ == '__main__':
    unittest.main()
