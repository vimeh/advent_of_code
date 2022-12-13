import unittest


def dir_sizes(stream):
    stack = []
    res = {}

    cwd, usize = '', 0
    for line in stream[1:]:
        line = line.split()

        # options
        if line[0] == '$':
            if line[1] == 'cd':
                # cd
                if line[2] == '..':
                    path = '/'.join([x[0] for x in stack]) + '/' + cwd
                    res[path] = usize
                    parent = stack.pop()
                    cwd = parent[0]
                    usize += parent[1]
                else:
                    # cd dir
                    stack.append((cwd, usize))
                    cwd, usize = line[2], 0
            else:
                # ls -- ignore
                continue
        else:
            if line[0] == 'dir':
                # dir name
                continue
            else:
                # file, usize
                usize += int(line[0])

    while stack:
        path = '/'.join([x[0] for x in stack]) + '/' + cwd
        res[path] = usize
        parent = stack.pop()
        cwd = parent[0]
        usize += parent[1]
    path = '/'.join([x[0] for x in stack]) + '/' + cwd
    res[path] = usize

    return res


def sum_dir_lt(stream, limit):
    res = dir_sizes(stream)
    res = [(k, v) for k, v in res.items() if v < limit]

    return sum([x[1] for x in res])


def min_delete(stream, tot, need):
    res = dir_sizes(stream)
    res = sorted(res.items(), key=lambda x: x[1])

    free = tot - res[-1][1]
    need -= free
    for _, v in res:
        if v > need:
            return v


class Tests(unittest.TestCase):
    limit = 100000
    need = 30000000
    tot = 70000000

    def setUp(self) -> None:
        filename = "data/07_e.txt"
        with open(filename, 'r') as f:
            self.data_example = f.read().splitlines()

        filename = "data/07_i.txt"
        with open(filename, 'r') as f:
            self.data = f.read().splitlines()

    def test_part1_example(self):
        res = 95437
        self.assertEqual(sum_dir_lt(self.data_example, self.limit), res)

    def test_part1(self):
        res = 1428881
        self.assertEqual(sum_dir_lt(self.data, self.limit), res)

    def test_part2(self):
        res = 10475598
        self.assertEqual(min_delete(self.data, self.tot, self.need), res)


if __name__ == '__main__':
    unittest.main()
