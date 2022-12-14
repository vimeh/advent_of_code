import unittest


def pos_visited(data):
    visited = set()
    start = (0, 0)
    head = (0, 0)
    tail = (0, 0)
    visited.add(tail)
    moves = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

    for move in data:
        d, s = move[0], int(move[1])
        for _ in range(s):
            temp = head
            head = (head[0] + moves[d][0], head[1] + moves[d][1])
            if any(abs(h - t) > 1 for h, t in zip(head, tail)):
                tail = temp
                visited.add(tail)

    return len(visited)


class Solution(unittest.TestCase):

    def setUp(self):
        filename = 'data/09_e.txt'
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        data = [line.split() for line in data]
        self.data_example = data

        filename = 'data/09_i.txt'
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        data = [line.split() for line in data]
        self.data = data

    def test_part1_example(self):
        self.assertEqual(13, pos_visited(self.data_example))

    def test_part1(self):
        self.assertEqual(6087, pos_visited(self.data))


if __name__ == '__main__':
    unittest.main()
