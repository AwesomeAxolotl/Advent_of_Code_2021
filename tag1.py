#part 1
with open("tag1.txt") as f:
    c = 0
    increases = 0
    skip = True
    for line in f:
        if skip:
            c = int(line)
            skip = False
        else:
            increases += int(line) > c
            c = int(line)

print(increases)


#part2
with open("tag1.txt") as f:
    lines = [int(line) for line in f.readlines()]
    increases = 0
    for i in range(0,len(lines)-3):
        increases += lines[i+3] > lines[i]

print(increases)   

