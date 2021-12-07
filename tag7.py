with open("tag7.txt") as f:
    for l in f:
        N = [int(x) for x in l.rstrip().split(",")]
    
    min_fuel = None # part 1
    min_fuel_p2 = None # part 2
    for i in range(max(N)+1):
        if min_fuel is None:
            min_fuel = sum([abs(i-x) for x in N])
            min_fuel_p2 = sum([(abs(i-x)**2+abs(i-x))/2  for x in N])
        else:
            fuel = sum([abs(i-x) for x in N])
            fuel_p2 = sum([(abs(i-x)**2+abs(i-x))/2  for x in N])
            if fuel < min_fuel:
                min_fuel = fuel
            if fuel_p2 < min_fuel_p2:
                min_fuel_p2 = fuel_p2

print(min_fuel) # part 1
print(int(min_fuel_p2)) # part 2