import unittest
from collections import deque


def parse_input(data):
    grid = []
    S, E = None, None

    for i, line in enumerate(data):
        row = []
        for j, elev in enumerate(line):
            row.append(ord(elev) - ord('a'))
            if row[-1] == (ord('S') - ord('a')):
                row[-1] = 1024
                S = (i, j)
            elif row[-1] == (ord('E') - ord('a')):
                row[-1] = (ord('z') - ord('a'))
                E = (i, j)
        grid.append(row)

    return grid, S, E


def get_valid_neighbors(curr, grid):
    M, N = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dm, dn in dirs:
        if 0 <= curr[0] + dm < M and 0 <= curr[1] + dn < N:
            if grid[curr[0] + dm][curr[1] + dn] <= grid[curr[0]][curr[1]] + 1:
                yield (curr[0] + dm, curr[1] + dn)


def find_path(data):
    grid, S, E = parse_input(data)

    queue = deque()
    curr = S
    seen = set([S])
    path = []

    while curr != E:
        path.append(curr)

        valid_neighbors = get_valid_neighbors(curr, grid)
        for nm, nn in valid_neighbors:
            if (nm, nn) not in seen:
                queue.append(((nm, nn), path.copy()))
                seen.add((nm, nn))

        curr, path = queue.popleft()

    return len(path)


class Solution(unittest.TestCase):

    def setUp(self):
        filename = 'data/12_e.txt'
        with open(filename) as f:
            data = f.read().splitlines()
        self.data_example = data

        filename = 'data/12_i.txt'
        with open(filename) as f:
            data = f.read().splitlines()
        self.data = data

    def test_part1_example(self):
        self.assertEqual(31, find_path(self.data_example))

    def test_part1(self):
        self.assertEqual(394, find_path(self.data))


if __name__ == '__main__':
    unittest.main()
