import unittest

DEBUG = False


def pos_visited(data, len_tail):
    visited = set()
    rope = [(0, 0)] * (1 + len_tail)
    visited.add(rope[-1])
    moves = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

    for move in data:
        d, s = move[0], int(move[1])
        for j in range(s):
            # move the head
            diff = moves[d]
            prev = rope[0]
            rope[0] = tuple(x + y for x, y in zip(prev, diff))

            # check the following nodes
            for i in range(1, len(rope)):
                if any(abs(p - n) > 1 for p, n in zip(rope[i - 1], rope[i])):
                    if sum(abs(p - n)
                           for p, n in zip(rope[i - 1], rope[i])) == 3:
                        if diff in moves.values():
                            prev, rope[i] = rope[i], prev
                        else:
                            prev, rope[i] = rope[i], tuple(
                                x + y for x, y in zip(rope[i], diff))
                    else:
                        direction = tuple(
                            (x - y) // 2 for x, y in zip(rope[i - 1], rope[i]))
                        prev, rope[i] = rope[i], tuple(
                            x + y for x, y in zip(rope[i], direction))
                        # prev, rope[i] = rope[i], tuple(
                        # x + y for x, y in zip(rope[i], moves[d]))

                diff = tuple(x - y for x, y in zip(rope[i], prev))
            if (DEBUG) and move == ['L', '8']:
                print(f'== {move} == {j}')
                for i in range(-14, 14):
                    for j in range(-14, 14):
                        if (-i, j) in rope:
                            print(f'{rope.index((-i,j))}', end='')
                        elif (i, j) == (0, 0):
                            print('s', end='')
                        else:
                            print('.', end='')
                    print('')

            # at end of move, add tail to visited
            visited.add(rope[-1])

        if (DEBUG):
            print(f'== {move} ==')
            for i in range(-14, 14):
                for j in range(-14, 14):
                    if (-i, j) in rope:
                        print(f'{rope.index((-i,j))}', end='')
                    elif (i, j) == (0, 0):
                        print('s', end='')
                    else:
                        print('.', end='')
                print('')

    if (DEBUG):
        print('VISITED')
        for i in range(-14, 14):
            for j in range(-14, 14):
                if (-i, j) in visited:
                    print('#', end='')
                elif (i, j) == (0, 0):
                    print('s', end='')
                else:
                    print('.', end='')
            print('')

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

        filename = 'data/09_e2.txt'
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        data = [line.split() for line in data]
        self.data_example2 = data

    def test_part1_example(self):
        self.assertEqual(13, pos_visited(self.data_example, 1))

    def test_part1(self):
        self.assertEqual(6087, pos_visited(self.data, 1))

    def test_part2_example1(self):
        self.assertEqual(1, pos_visited(self.data_example, 9))

    def test_part2_example2(self):
        self.assertEqual(36, pos_visited(self.data_example2, 9))

    def test_part2(self):
        self.assertEqual(2493, pos_visited(self.data, 9))


if __name__ == '__main__':
    unittest.main()
