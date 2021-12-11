flashes = 0

def flash(arr, r, c):
    if r >= 0 and r < len(arr) and c >= 0 and c < len(arr[0]):
        if arr[r][c] != -1:
            arr[r][c] += 1
        if arr[r][c] > 9:
            arr[r][c] = -1
            flash(arr, r-1,c-1)
            flash(arr, r-1,c)
            flash(arr, r-1,c+1)
            flash(arr, r,c-1)
            flash(arr, r,c+1)
            flash(arr, r+1,c-1)
            flash(arr, r+1,c)
            flash(arr, r+1,c+1)


def simulate(arr):
    global flashes
    #step 1
    for r, _ in enumerate(arr):
        for c, __ in enumerate(arr):
            arr[r][c] += 1
    
    #step 2
    for r, _ in enumerate(arr):
        for c, __ in enumerate(arr):
            if arr[r][c] > 9:
                arr[r][c] = -1
                flash(arr, r-1,c-1)
                flash(arr, r-1,c)
                flash(arr, r-1,c+1)
                flash(arr, r,c-1)
                flash(arr, r,c+1)
                flash(arr, r+1,c-1)
                flash(arr, r+1,c)
                flash(arr, r+1,c+1)
    
    #step 3
    for r, _ in enumerate(arr):
        for c, __ in enumerate(arr):
            if arr[r][c] == -1:
                flashes += 1
                arr[r][c] = 0
                

with open("tag11.txt") as f:
    arr = [[int(x) for x in y.strip()] for y in f.readlines()]
    arr2 = [[x for x in y] for y in arr]
    
    # part 1
    for i in range(100):
        simulate(arr)
    
    print(flashes)
    
    
    # part 2
    c = 0
    while True:
        c += 1
        flashes = 0
        max_flashes = len(arr2) * len(arr2[0])
        simulate(arr2)
        if flashes == max_flashes:
            break
    
    print(c)