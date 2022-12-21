import unittest


def is_correct_order(lt, rt):
    # ensure always operating on a list
    if type(lt) == int:
        return is_correct_order([lt], rt)

    if type(rt) == int:
        return is_correct_order(lt, [rt])

    # this is the problem here
    # not always the case that when len(lt) == 0 you're good. might just continue
    if len(lt) == 0:
        return True
    elif len(rt) == 0:
        return False

    # anywhere where type(lt[0]) or type(rt[0]) is a list,
    # recurse on rest of list and do a cast on xt[0] if necessary
    types = (type(lt[0]), type(rt[0]))
    if types == (list, list):
        return is_correct_order(lt[0], rt[0]) and is_correct_order(
            lt[1:], rt[1:])
    elif types == (list, int):
        return is_correct_order(lt[0], [rt[0]]) and is_correct_order(
            lt[1:], rt[1:])
    elif types == (int, list):
        return is_correct_order([lt[0]], rt[0]) and is_correct_order(
            lt[1:], rt[1:])
    elif types == (int, int):
        # both are ints and we can finally iterate
        if lt[0] < rt[0]:
            return True
        elif lt[0] == rt[0]:
            return is_correct_order(lt[1:], rt[1:])
        else:
            return False

    print(f'INVALID STATE: lt: {type(lt)}, rt: {type(rt)}')
    print(f'\tlt: {lt}, rt: {rt}')


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
        self.assertEqual(952, sum_correct_order(self.data))


if __name__ == '__main__':
    unittest.main()
