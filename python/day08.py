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


if __name__ == '__main__':
    unittest.main()
