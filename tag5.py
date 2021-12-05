from re import findall as findall

floor = {}

with open("tag5.txt") as f:
    for line in f:
        l = findall(r"[0-9]+", line)
        l = [int(x) for x in l]
        #same x
        if l[0] == l[2]:
            minimum = min(l[1], l[3])
            maximum = max(l[1], l[3])
            for i in range(minimum, maximum + 1):
                key = f"{l[0]},{i}"
                if key in floor:
                    floor[key] += 1
                else:
                    floor[key] = 1
        #same y
        elif l[1] == l[3]:
            minimum = min(l[0], l[2])
            maximum = max(l[0], l[2])
            for i in range(minimum, maximum + 1):
                key = f"{i},{l[1]}"
                if key in floor:
                    floor[key] += 1
                else:
                    floor[key] = 1
        #diagonal, skip if you wanna solve part 1
        elif abs(l[0] - l[2]) == abs(l[1] - l[3]):
            stepx = 1 if (l[0] < l[2]) else -1
            stepy = 1 if (l[1] < l[3]) else -1
            
            for i in range(abs(l[0] - l[2])+1):
                key = f"{l[0] + i * stepx},{l[1] + i * stepy}"
                if key in floor:
                    floor[key] += 1
                else:
                    floor[key] = 1
      

overlaps = 0
for v in floor.values():
    overlaps += v > 1

print(overlaps)