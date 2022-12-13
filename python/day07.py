import unittest


def sum_dir_lt(stream, limit):
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

    res = [(k, v) for k, v in res.items() if v < limit]

    return sum([x[1] for x in res])


class Tests(unittest.TestCase):
    limit = 100000

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


if __name__ == '__main__':
    unittest.main()
