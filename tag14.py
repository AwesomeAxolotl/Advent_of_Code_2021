polymer = None
polymer_string = None
subs = {}
steps = 40 #use 10 for part 1, 40 for part 2


with open("tag14.txt") as f:
    for line in f:
        if not polymer:
            polymer_string = line.rstrip()
            polymer = {}
            for i in range(1, len(line.rstrip())):
                pair = f"{line[i-1]}{line[i]}"
                if pair in polymer:
                    polymer[pair] += 1
                else:
                    polymer[pair] = 1
        
        elif line.rstrip() != "":
            sub = line.rstrip().split(" -> ")
            subs[sub[0]] = sub[1]
    
    # part 1 + 2, adjust steps at the start of file
    for step in range(steps):
        new = {}
        for pair in subs:
            if pair in polymer:
                pair1 = f"{pair[0]}{subs[pair]}"
                pair2 = f"{subs[pair]}{pair[1]}"
                if pair1 in new:
                    new[pair1] += polymer[pair]
                else:
                    new[pair1] = polymer[pair]
                if pair2 in new:
                    new[pair2] += polymer[pair]
                else:
                    new[pair2] = polymer[pair]
        polymer = new
    
    counts = {}
    for pair in polymer:
        if pair[0] in counts:
            counts[pair[0]] += polymer[pair]
        else:
            counts[pair[0]] = polymer[pair]
        if pair[1] in counts:
            counts[pair[1]] += polymer[pair]
        else:
            counts[pair[1]] = polymer[pair]
    
    #adjust for starting and end letter
    counts[polymer_string[0]] += 1
    counts[polymer_string[-1]] += 1
    
    min_count = None
    max_count = None
    for v in counts.values():
        if min_count is None or v < min_count:
            min_count = v
        if max_count is None or v > max_count:
            max_count = v
    
    print(int(max_count * 0.5 - min_count * 0.5))