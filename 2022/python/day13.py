import unittest


def is_correct_order(lt, rt):

    for l, r in zip(lt, rt):
        if l == r:
            continue

        if (type(l), type(r)) == (int, int):
            return (l > r) - (l < r)

        l = [l] if type(l) == int else l
        r = [r] if type(r) == int else r

        if (res := is_correct_order(l, r)) != 0:
            return res

    return (len(lt) > len(rt)) - (len(lt) < len(rt))


def sum_correct_order(data):
    sum_idx = 0
    offset = 3
    for idx, pair in enumerate(
        [data[s:s + offset] for s in range(0, len(data), offset)]):
        lt, rt = eval(pair[0]), eval(pair[1])
        if is_correct_order(lt, rt) == -1:
            sum_idx += idx + 1

    return sum_idx


class Solution(unittest.TestCase):

    def setUp(self):
        filename = 'data/13_e.txt'
        with open(filename) as f:
            data = f.read().splitlines()
        self.data_ex = data

        filename = 'data/13_i.txt'
        with open(filename) as f:
            data = f.read().splitlines()
        self.data = data

    def test_part1_example(self):
        self.assertEqual(13, sum_correct_order(self.data_ex))

    def test_part1(self):
        self.assertEqual(5808, sum_correct_order(self.data))


if __name__ == '__main__':
    unittest.main()
