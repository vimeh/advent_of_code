import unittest


def is_correct_order(lt, rt):
    print(lt, rt)
    if type(lt) == int:
        if type(rt) == int:
            return lt <= rt
        elif type(rt) == list:
            return is_correct_order([lt], rt)
    elif type(lt) == list:
        if type(rt) == int:
            return is_correct_order(lt, [rt])
        elif type(rt) == list:
            if len(lt) == 0:
                return True
            elif len(rt) == 0:
                return False
            elif is_correct_order(lt[0], rt[0]):
                if type(lt[0]) == int and type(rt[0]) == int:
                    if lt[0] < rt[0]:
                        return True
                    else:
                        return is_correct_order(lt[1:], rt[1:])
                else:
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

    def rtest_part1(self):
        self.assertEqual(13, sum_correct_order(self.data))


if __name__ == '__main__':
    unittest.main()
