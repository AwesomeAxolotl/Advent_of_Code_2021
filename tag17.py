import re

valid_x = {}
valid_y = {}


def getHighestPoint(y, ymin, ymax):
    height = 0
    max_height = 0
    steps = 0
    hit_dest = False
    while height + y >= ymin:
        height += y
        if height > max_height:
            max_height = height
        steps += 1
        y -= 1
        if height >= ymin and height <= ymax:
            hit_dest = True
    return max_height, hit_dest, steps

# if given velocity meets the target area after s steps
# add it to valid_x
def getValidX(x, xmin, xmax, max_steps):
    initial = x
    d = 0
    steps = 0
    while d < xmax and steps <= max_steps:
        d += x
        steps += 1
        if x > 0:
            x -= 1
        if d >= xmin and d <= xmax:
            if steps in valid_x:
                valid_x[steps].append(initial)
            else:
                valid_x[steps] = [initial]
    return True


def getValidY(y, ymin, ymax, max_steps):
    initial = y
    h = 0
    steps = 0
    while h > ymin and steps <= max_steps:
        h += y
        steps += 1
        y -= 1
        if h >= ymin and h <= ymax:
            if steps in valid_y:
                valid_y[steps].append(initial)
            else:
                valid_y[steps] = [initial]
    return True


with open("tag17.txt") as f:
    line = f.readline()
    result = re.findall("[-0-9]+", line)
    result = [int(x) for x in result]
    
    xmin = result[0]
    xmax = result[1]
    ymin = result[2]
    ymax = result[3]
    
    #dermine slowest x possible
    
    # part 1
    # vel_y is symmetri, for every addition there will be a substraction
    # so we'll end up at y = 0 at one step, and  -vel_y - 1 at next step
    # this one needs to be inside the target area..
    vel_y = - ymin - 1
    max_height, hit, max_steps = getHighestPoint(vel_y, ymin, ymax)
    print(max_height)
    
    # part 2
    vel_x = xmax
    reaches_target = True
    while vel_x > 0:
        getValidX(vel_x, xmin, xmax, max_steps)
        vel_x -= 1
    
    # stop condition: y out of target after first step
    while vel_y >= ymin:
        getValidY(vel_y, ymin, ymax, max_steps)
        vel_y -= 1
    
    total = {}
    for i in range(1, max_steps + 1):
        if i in valid_x and i in valid_y:
            for x in valid_x[i]:
                for y in valid_y[i]:
                    total[(x,y)] = True
    print(len(total))