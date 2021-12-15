from time import perf_counter

# part 1
with open("tag15.txt") as f:
    #3d array, each element: 0=cost, 1=parent, 2=min cost to reach, 3=min cost to target, 4=adjacent nodes
    grid = [[[int(y), False, False, 0] for y in x.rstrip()] for x in f.readlines()]
    grid[0][0][1] = 0
    grid[0][0][2] = 0
    
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            adjacent = []
            if r > 0:
                adjacent.append((r - 1, c))
            if r < len(grid) - 1:
                adjacent.append((r + 1, c))
            if c > 0:
                adjacent.append((r, c - 1))
            if c < len(row) - 1:
                adjacent.append((r, c + 1))
            grid[r][c].append(adjacent)
    
    t_start = perf_counter()
    n = [(0,0)]
    c = []
    target = (len(grid)-1, len(grid[0])-1)
    
    while len(n) > 0:
        min_cost = None
        min_index = None
        for i, p in enumerate(n):
            cost = grid[p[0]][p[1]][2]
            if min_index is None or cost < min_cost:
                min_cost = cost
                min_index = i
        
        c.append(n.pop(min_index)) 
        if c[-1] == target:
            print(grid[c[-1][0]][c[-1][1]][1])
            print(perf_counter() - t_start)
            break
        
        grid[c[-1][0]][c[-1][1]][3] = 2
        
        for a in grid[c[-1][0]][c[-1][1]][4]:
            #if not shortest path to that node found already
            if grid[a[0]][a[1]][3] != 2:
                #if not in n (open list)
                if grid[a[0]][a[1]][3] == 0:
                    cost = grid[a[0]][a[1]][0] + grid[c[-1][0]][c[-1][1]][1]
                    grid[a[0]][a[1]][1] = cost
                    grid[a[0]][a[1]][2] = cost + target[0] + target[1] - a[0] - a[1]
                    grid[a[0]][a[1]][3] = 1
                    n.append(a)
                
                #else it is in open list
                else:
                    cost = grid[a[0]][a[1]][0] + grid[c[-1][0]][c[-1][1]][1]
                    if cost < grid[a[0]][a[1]][1]:
                        grid[a[0]][a[1]][1] = cost
                        grid[a[0]][a[1]][2] = cost + target[0] + target[1] - a[0] - a[1]


# part 2
with open("tag15.txt") as f:
    #3d array, each element: 0=cost, 1=parent, 2=min cost to reach, 3=min cost to target, 4=adjacent nodes
    grid = [[int(y) for y in x.rstrip()] for x in f.readlines()]
    
    #tile the array:
    full_grid = [[0 for _ in range(len(grid[0]*5))] for _ in range(len(grid*5))]
    
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            for i in range(5):
                for j in range(5):
                    val = (col + i + j) % 9
                    if val == 0:
                        val = 9
                    full_grid[r + i * len(grid)][c + j * len(grid[0])] = [val, False, False, 0]
    
    grid = full_grid
    grid[0][0][1] = 0
    grid[0][0][2] = 0
    
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            adjacent = []
            if r > 0:
                adjacent.append((r - 1, c))
            if r < len(grid) - 1:
                adjacent.append((r + 1, c))
            if c > 0:
                adjacent.append((r, c - 1))
            if c < len(row) - 1:
                adjacent.append((r, c + 1))
            grid[r][c].append(adjacent)
    
    t_start = perf_counter()
    n = [(0,0)]
    c = []
    target = (len(grid)-1, len(grid[0])-1)
    
    while len(n) > 0:
        min_cost = None
        min_index = None
        for i, p in enumerate(n):
            cost = grid[p[0]][p[1]][2]
            if min_index is None or cost < min_cost:
                min_cost = cost
                min_index = i
        
        c.append(n.pop(min_index)) 
        if c[-1] == target:
            print(grid[c[-1][0]][c[-1][1]][1])
            print(perf_counter() - t_start)
            break
        
        grid[c[-1][0]][c[-1][1]][3] = 2
        
        for a in grid[c[-1][0]][c[-1][1]][4]:
            #if not shortest path to that node found already
            if grid[a[0]][a[1]][3] != 2:
                #if not in n (open list)
                if grid[a[0]][a[1]][3] == 0:
                    cost = grid[a[0]][a[1]][0] + grid[c[-1][0]][c[-1][1]][1]
                    grid[a[0]][a[1]][1] = cost
                    grid[a[0]][a[1]][2] = cost + target[0] + target[1] - a[0] - a[1]
                    grid[a[0]][a[1]][3] = 1
                    n.append(a)
                
                #else it is in open list
                else:
                    cost = grid[a[0]][a[1]][0] + grid[c[-1][0]][c[-1][1]][1]
                    if cost < grid[a[0]][a[1]][1]:
                        grid[a[0]][a[1]][1] = cost
                        grid[a[0]][a[1]][2] = cost + target[0] + target[1] - a[0] - a[1]