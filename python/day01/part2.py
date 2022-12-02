filename = "input.txt"
# filename = "example.txt" 

import heapq

top = [0 for _ in range(3)] 

with open(filename, "r") as file:
    temp = 0

    for line in file.readlines():
        if line.strip() == '':
            heapq.heappushpop(top, temp)
            temp = 0 
        else: 
            temp += int(line.strip())

    heapq.heappushpop(top, temp)

print(sum(top))
