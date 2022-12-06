import unittest


def stream_start(seq: str, marker_len: int) -> int:
    for i in range(marker_len, len(seq)):
        window = seq[i - marker_len:i]
        if len(set(window)) == marker_len:
            return i

    raise LookupError


class Examples(unittest.TestCase):
    START_PKT_LEN = 4
    START_MSG_LEN = 14

    def test_partA_examples(self):
        seq_list = [
            'mjqjpqmgbljsphdztnvjfqwrcgsmlb', 'bvwbjplbgvbhsrlpgdmjqwftvncz',
            'nppdvjthqldpwncqszvftbrmjlhg',
            'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
            'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        ]

        res_list = [7, 5, 6, 10, 11]
        self.assertListEqual(
            list(map(lambda x: stream_start(x, self.START_PKT_LEN), seq_list)),
            res_list)

    def test_partA(self):
        filename = 'data/06_i.txt'
        with open(filename, 'r') as f:
            seq = f.read()
        self.assertEqual(stream_start(seq, self.START_PKT_LEN), 1794)

    def test_partB_examples(self):
        seq_list = [
            'mjqjpqmgbljsphdztnvjfqwrcgsmlb', 'bvwbjplbgvbhsrlpgdmjqwftvncz',
            'nppdvjthqldpwncqszvftbrmjlhg',
            'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
            'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        ]

        res_list = [19, 23, 23, 29, 26]
        self.assertListEqual(
            list(map(lambda x: stream_start(x, self.START_MSG_LEN), seq_list)),
            res_list)

    def test_partB(self):
        filename = 'data/06_i.txt'
        with open(filename, 'r') as f:
            seq = f.read()
        self.assertEqual(stream_start(seq, self.START_MSG_LEN), 2851)


if __name__ == '__main__':
    unittest.main()
