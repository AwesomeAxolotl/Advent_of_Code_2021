def get_common(arr, pos):
    sum = 0
    for elem in arr:
        sum += int(elem[pos])
    if sum > len(arr)*0.5:
        return 1
    elif sum < len(arr)*0.5:
        return 0
    else:
        return 2


def delete_elems(arr, pos, criteria):
    return([a for a in arr if a[pos] == criteria])


with open("tag3.txt") as f:
    lines = [line.rstrip() for line in f]
    
    #part 1
    gamma = ""
    epsilon = ""
    
    for n in range(len(lines[0])):
        result = sum([int(line[n]) for line in lines])
        gamma += str(int(result > len(lines) * 0.5))
        epsilon += str(int(result < len(lines) * 0.5))
        
    print(int(gamma, 2) * int(epsilon, 2))
    
    #part 2
    oxy = lines.copy()
    epsilon = lines.copy()
    for pos in range(len(lines[0])):
        common = get_common(oxy, pos)
        if common in [1,2]:
            oxy = delete_elems(oxy, pos, "0")
        else:
            oxy = delete_elems(oxy, pos, "1")
        if len(oxy) < 2:
            break
    for pos in range(len(lines[0])):
        common = get_common(epsilon, pos)
        if common in [1,2]:
            epsilon = delete_elems(epsilon, pos, "1")
        else:
            epsilon = delete_elems(epsilon, pos, "0")
        if len(epsilon) < 2:
            break
    
    print(int(oxy[0], 2) * int(epsilon[0], 2))






    
        
        


        
        
    

