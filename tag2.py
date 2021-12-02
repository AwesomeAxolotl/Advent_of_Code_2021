p1 = {"depth":0, "horizontal":0}
p2 = {"depth":0, "horizontal":0, "aim":0}

def piloting(direction, n):
    if direction == "forward":
        p1["horizontal"] += n
        p2["horizontal"] += n
        p2["depth"] += n * p2["aim"]
    elif direction == "down":
        p1["depth"] += n
        p2["aim"] += n
    else:
        p1["depth"] -= n
        p2["aim"] -= n


with open("tag2.txt") as f:
    for line in f:
        splitted = line.split()
        piloting(splitted[0], int(splitted[1]))


print(p1["depth"]*p1["horizontal"])
print(p2["depth"]*p2["horizontal"])