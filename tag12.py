from re import match as match

map = {}

with open("tag12.txt") as f:
    for line in f:
        line = line.rstrip().split("-")
        
        if line[0] in map:
            map[line[0]].append(line[1])
        else:
            map[line[0]] = [line[1]]
        if line[1] in map:
            map[line[1]].append(line[0])
        else:
            map[line[1]] = [line[0]]
    
    # part 1
    #traverse:
    cur = [["start", -1]]
    visited = {"start": True}
    paths = 0
    
    while True:
        cur[-1][1] += 1
        node = cur[-1][0]
        choice = cur[-1][1]
        
        if choice < len(map[node]) and map[node][choice] not in visited:
            next = map[node][choice]
            if next == "end":
                paths += 1
                
            else:
                cur.append([next, -1])
                if match("[a-z]", next):
                    visited[next] = True
        
        elif choice >= len(map[node]):
            removed = cur.pop()
            if match("[a-z]", removed[0]):
                visited.pop(removed[0])
        
        if len(cur) == 0:
            break
    print(paths)
    
    # part 2
    #traverse:
    cur = [["start", -1]]
    visited = {"start": True}
    paths = 0
    twice = ""
    
    while True:
        cur[-1][1] += 1
        node = cur[-1][0]
        choice = cur[-1][1]
        
        if choice < len(map[node]) and (twice == "" or map[node][choice] not in visited):
            next = map[node][choice]
            if next == "start":
                pass
                
            elif next == "end":
                paths += 1
                
            else:
                cur.append([next, -1])
                if match("[a-z]", next):
                    if next in visited:
                        twice = next
                    else:
                        visited[next] = True
        
        elif choice >= len(map[node]):
            removed = cur.pop()
            if twice == removed[0]:
                twice = ""
            elif match("[a-z]", removed[0]):
                visited.pop(removed[0])
        
        if len(cur) == 0:
            break
    print(paths)