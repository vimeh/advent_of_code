filename = "data/02_i.txt"

# aka fun with state machines

# 3 situations
# outcome (state) points: 0, 3, 6
# move (transition) points: 1, 2, 3

def score(h1, h2):
    # draw condition
    if h1 == h2:
        return 3 + (h2+1)
    # win condition
    elif (h2-(h1+1)) % 3 == 0:
        return 6 + (h2+1)
    # lose condition
    return h2+1

# read in and transform data 
with open(filename, "r") as f:
    data = f.read().splitlines()
    data = [line.split() for line in data]
    data = [(ord(h1) - ord("A"), ord(h2) - ord("X")) for h1, h2 in data]

print(sum(score(h1,h2) for h1, h2 in data))
# move to outcome transformation swaps? the transition map of the state machine
# (0, 2) previously was lose + 2
# (0, 2) now is win + winningmove(0) 

def transform(h1, outcome):
    # draw condition:
    if outcome == 1:
        return h1
    # win condition
    elif outcome == 2:
        return (h1+1)%3
    else:
        # 0 -> 2
        # 1 -> 0
        # 2 -> 1
        return (h1+2)%3

data = [(h1, transform(h1,h2)) for h1, h2 in data]
print(sum(score(h1,h2) for h1, h2 in data))
