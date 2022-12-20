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
                row[-1] = ord('a') - ord('a')
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


def find_path(grid, S, E):

    queue = deque([(S, [])])
    seen = set()
    curr = None

    while curr != E and queue:
        curr, path = queue.popleft()
        path.append(curr)

        valid_neighbors = get_valid_neighbors(curr, grid)
        for nm, nn in valid_neighbors:
            if (nm, nn) not in seen:
                queue.append(((nm, nn), path.copy()))
                seen.add((nm, nn))

    if curr == E:
        return len(path) - 1
    else:
        return 2**10


def find_best_path(data, all_starts=False):
    grid, S, E = parse_input(data)

    if all_starts:
        starts = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    starts.append((i, j))
    else:
        starts = [S]

    best_path = None
    for start in starts:
        path = find_path(grid, start, E)
        if best_path is None or path < best_path:
            best_path = path

    return best_path


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
        self.assertEqual(31, find_best_path(self.data_example))

    def test_part1(self):
        self.assertEqual(394, find_best_path(self.data))

    def test_part2_example(self):
        self.assertEqual(29, find_best_path(self.data_example, True))

    def test_part2(self):
        self.assertEqual(388, find_best_path(self.data, True))


if __name__ == '__main__':
    unittest.main()
