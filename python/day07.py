import unittest
import re


def dir_sizes(stream):
    stack = [0]
    res = []

    while stack:
        line = next(stream, "$ cd ..")

        if line == '$ cd ..':
            usize = stack.pop()
            if stack:
                res.append(usize)
                stack[-1] += usize
        elif cd := re.match(r"\$ cd .+", line):
            stack.append(0)
        elif file := re.match(r"(\d+) .+", line):
            stack[-1] += int(file.group(1))

    return res


def sum_dir_lt(stream, limit):
    res = dir_sizes(stream)
    res = [x for x in res if x < limit]

    return sum(res)


def min_delete(stream, tot, need):
    res = dir_sizes(stream)
    res = sorted(res)

    free = tot - res[-1]
    need -= free
    for v in res:
        if v > need:
            return v


class Tests(unittest.TestCase):
    limit = 100000
    need = 30000000
    tot = 70000000

    def setUp(self) -> None:
        filename = "data/07_e.txt"
        with open(filename, 'r') as f:
            self.data_example = iter(f.read().splitlines())

        filename = "data/07_i.txt"
        with open(filename, 'r') as f:
            self.data = iter(f.read().splitlines())

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
