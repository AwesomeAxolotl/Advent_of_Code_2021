n = None

#part1
with open("tag6.txt") as f:
    for line in f:
        n = [int(x) for x in line.rstrip().split(",")]
    
    for i in range(80):
        spawn = 0
        for no, fish in enumerate(n):
            if fish > 0:
                n[no] -= 1
            else:
                n[no] = 6
                #9 because it ticks down once in the loop
                n.append(9)
        
print(len(n))

#part2
class Fish:
    cache = {}
    
    def __init__(self):
        pass
    
    def getLength(self, days):
        if days <= 8:
            return(1)
        elif days in Fish.cache:
            return(Fish.cache[days])
        else:
            #fish 8
            res1 = Fish().getLength(days - 9)
            #fish 6   
            res2 = Fish().getLength(days - 7)
            res = res1 + res2
            Fish.cache[days] = res
            return(res)


with open("tag6.txt") as f:
    for line in f:
        fishes = [int(x) for x in line.rstrip().split(",")]
    
    sum = 0
    for fish in fishes:
        sum += Fish().getLength(256 + 8 - fish)
    print(sum)