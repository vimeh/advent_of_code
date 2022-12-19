import unittest
import re


class Monkey():
    inspects = 0

    def __init__(self, items, op, co, test, test_t, test_f):
        self.items = items
        if op == '+':
            if co == 'old':
                self.op = lambda x: x + x
            else:
                self.op = lambda x: x + int(co)
        elif op == '*':
            if co == 'old':
                self.op = lambda x: x * x
            else:
                self.op = lambda x: x * int(co)

        self.div = lambda x: test_t if x % test == 0 else test_f


def monkey_business(data, rounds):
    len_monkey = 7
    monkeys = []
    for monkey in [
            data[s:s + len_monkey] for s in range(0, len(data), len_monkey)
    ]:
        items = re.findall(r'\d+', monkey[1])
        items = [int(item) for item in items]

        op, co = re.search(r'([+*]) (\d+|old)', monkey[2]).groups()

        test = int(re.search(r'\d+', monkey[3]).group(0))
        test_t = int(re.search(r'\d+', monkey[4]).group(0))
        test_f = int(re.search(r'\d+', monkey[5]).group(0))
        monkeys.append(Monkey(items, op, co, test, test_t, test_f))

    for _ in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item = monkey.items.pop(0)
                item = monkey.op(item) // 3
                to = monkey.div(item)
                monkeys[to].items.append(item)
                monkey.inspects += 1

    monkeys = sorted(monkeys, key=lambda x: x.inspects, reverse=True)

    return monkeys[0].inspects * monkeys[1].inspects


class Solution(unittest.TestCase):

    def setUp(self):
        filename = "./data/11_e.txt"
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        self.data_example = data
        filename = "./data/11_i.txt"
        with open(filename, 'r') as f:
            data = f.read().splitlines()

        self.data = data

    def test_part1_example(self):
        self.assertEqual(10605, monkey_business(self.data_example, 20))

    def test_part1(self):
        self.assertEqual(54036, monkey_business(self.data, 20))


if __name__ == '__main__':
    unittest.main()
