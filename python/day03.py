# filename = 'data/03_e.txt'
filename = 'data/03_i.txt'

def priority(char):
    if char.isupper():
        return 27 + ord(char) - ord('A')
    else:
        return 1 + ord(char) - ord('a')

with open(filename, 'r') as f:
    data = f.readlines()
    priority_sum = 0
    for line in data:
        mid = len(line) // 2
        shared = set(line[:mid]).intersection(set(line[mid:])).pop()
        priority_sum += priority(shared)

print(priority_sum)

