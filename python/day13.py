import unittest


def is_correct_order(lt, rt):
    if type(lt) == int:
        return is_correct_order([lt], rt)

    if type(rt) == int:
        return is_correct_order(lt, [rt])

    if len(lt) == 0:
        return True
    elif len(rt) == 0:
        return False

    if type(lt[0]) == int:
        if type(rt[0]) == int:
            if lt[0] < rt[0]:
                return True
            elif lt[0] == rt[0]:
                return is_correct_order(lt[1:], rt[1:])
            else:
                return False
        else:
            return is_correct_order(lt[0], rt[0])
    elif type(lt[0]) == list:
        if type(rt[0]) == int:
            return is_correct_order(lt[0], rt[0])
        else:
            if is_correct_order(lt[0], rt[0]):
                return is_correct_order(lt[1:], rt[1:])


def sum_correct_order(data):
    sum_idx = 0
    offset = 3
    for idx, pair in enumerate(
        [data[s:s + offset] for s in range(0, len(data), offset)]):
        if is_correct_order(eval(pair[0]), eval(pair[1])):
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
        self.assertEqual(13, sum_correct_order(self.data))


if __name__ == '__main__':
    unittest.main()
