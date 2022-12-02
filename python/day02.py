filename = "data/02_i.txt"

# 3 situations
# 0, 3, 6
# 1, 2, 3



def score(h1, h2):
    # draw condition
    if h1 == h2:
        return 3 + (h2+1)
    # win condition, modulo would work here but be slower
    elif h2 - h1 == 1 or h2 - h1 == -2:
        return 6 + (h2+1)
    # lose condition
    return h2+1

# read in and transform data 
with open(filename, "r") as f:
    data = f.read().splitlines()
    data = [line.split() for line in data]
    data = [(ord(h1) - ord("A"), ord(h2) - ord("X")) for h1, h2 in data]

print(sum(score(h1,h2) for h1, h2 in data))
