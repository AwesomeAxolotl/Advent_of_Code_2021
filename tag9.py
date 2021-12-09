def isLowpoint(arr, x, y):
    cur = arr[x][y]
    neighbors = []
    if x > 0:
        neighbors.append(arr[x-1][y])
    if y > 0:
        neighbors.append(arr[x][y-1])
    if x < len(arr)-1:
        neighbors.append(arr[x+1][y])
    if y < len(arr[0])-1:
        neighbors.append(arr[x][y+1])
    
    if all([x > cur for x in neighbors]):
        return True
    else:
        return False


def checkBasin(arr, x, y):
    if (x >= 0) and (x < len(arr)) and (y >= 0) and (y < len(arr[0])):
        if arr[x][y] == 9:
            return 0
        else:
            arr[x][y] = 9
            result = 1 + checkBasin(arr, x - 1, y) \
                     + checkBasin(arr, x + 1, y) \
                     + checkBasin(arr, x, y - 1) \
                     + checkBasin(arr, x, y + 1)
            return result
    else:
        return 0      
        

with open("tag9.txt") as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]
    
    # part 1
    risk = 0
    for row, r in enumerate(lines):
        for col, c in enumerate(r):
            if isLowpoint(lines, row, col):
                risk += (c + 1)
                
    print(risk)
    
    # part 2
    basins = []
    for row, r in enumerate(lines):
        for col, c in enumerate(r):
            val = checkBasin(lines, row, col)
            if val > 0:
                basins.append(val)
    basins.sort(reverse = True)
    print(basins[0]*basins[1]*basins[2])