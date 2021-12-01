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
    for i, line in enumerate(lines):
        if i < len(lines) - 3:
            sum1 = sum(lines[i:i+3])
            sum2 = sum(lines[i+1:i+4])
            increases += sum2 > sum1

print(increases)   

