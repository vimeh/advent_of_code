# filename = 'data/03_e.txt'
filename = 'data/03_i.txt'

def priority(char):
    if char.isupper():
        return 27 + ord(char) - ord('A')
    else:
        return 1 + ord(char) - ord('a')

with open(filename, 'r') as f:
    data = f.read().splitlines()
    priority_sum = 0
    for line in data:
        mid = len(line) // 2
        shared = set(line[:mid]).intersection(set(line[mid:])).pop()
        priority_sum += priority(shared)

print(priority_sum)

with open(filename, 'r') as f:
    data = f.read().splitlines()
    priority_sum = 0
    data = [list(map(set, data[i:i+3])) for i in range(0,len(data),3)]
    for group in data:
        shared = group[0].intersection(group[1]).intersection(group[2]).pop()
        priority_sum += priority(shared)

print(priority_sum)
