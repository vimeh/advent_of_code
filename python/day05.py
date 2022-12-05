filename = "data/05_i.txt"
# filename = "data/05_e.txt"

with open(filename, 'r') as f:
    levels = []
    line = f.readline()
    num_stacks = 1 + (len(line) - 3)//4

    while line[0] in [' ', '[']:
        level = []
        for i in range(num_stacks):
            level.append(line[4*i:4*i+3])
        levels.append(level)
        line = f.readline()

    levels = levels[:-1]
    stacks = [[] for _ in range(num_stacks)]
    for level in levels[::-1]:
        for i, stack in enumerate(level):
            if stack != '   ':
                stacks[i].append(stack[1])
    import copy
    stacks_9001 = copy.deepcopy(stacks) 

    moves = f.read().splitlines()
    moves = [move.split(' ') for move in moves]
    moves = [list(map(int, [move[1], move[3], move[5]])) for move in moves]

    for move in moves:
        for _ in range(0, move[0]):
            stacks[move[2]-1].append(stacks[move[1]-1].pop())

    print(''.join([stack[-1] for stack in stacks]))

    for move in moves:
        temp = []
        for _ in range(0, move[0]):
            temp.append(stacks_9001[move[1]-1].pop())
        stacks_9001[move[2]-1].extend(temp[::-1]) 

    print(''.join([stack[-1] for stack in stacks_9001]))
