filename = "data/04_i.txt"
# filename = "data/04_e.txt"

with open(filename, "r") as f:
    data = f.read().splitlines()

import re
assignments = [list(map(int, re.split(',|-', line))) for line in data]
subsets = 0

for a in assignments:
    set1 = set(x for x in range(a[0], a[1]+1))
    set2 = set(x for x in range(a[2], a[3]+1))
    if set1.issubset(set2) or set2.issubset(set1):
        subsets += 1

print(subsets)

overlaps = 0
for a in assignments:
    set1 = set(x for x in range(a[0], a[1]+1))
    set2 = set(x for x in range(a[2], a[3]+1))
    if len(set1 | set2) < len(set1) + len(set2):
        overlaps += 1
            
print(overlaps)
