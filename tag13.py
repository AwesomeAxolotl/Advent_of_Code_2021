from PIL import Image

points = []
content = 0
part1 = True

with open("tag13.txt") as f:
    for line in f:
        if line.rstrip() == "":
            content += 1
        elif content == 0:
            points.append([int(x) for x in line.rstrip().split(",")])
        elif content == 1:
            fold = line.rstrip().split("=")
            fold_dir = fold[0][-1]
            fold_c = int(fold[1])
            new = []
            
            if fold_dir == "x":
                for p in points:
                    if p[0] > fold_c:
                        p2 = [2 * fold_c - p[0], p[1]]
                        new.append(p2)
                    else:
                        new.append(p)
                points = new
            else:
                for p in points:
                    if p[1] > fold_c:
                        p2 = [p[0], 2 * fold_c - p[1]]
                        new.append(p2)
                    else:
                        new.append(p)
                points = new
            
            #report after a single fold
            if part1:
                total = {}
                for p in points:
                    total[f"{p[0]}-{p[1]}"] = True
                print(len(total))
                part1 = False
                
# part 2:

img = Image.new('RGB', (100, 100))
for p in points:
    img.putpixel((p[0], p[1]), (255, 255, 255))

img = img.resize((300, 300))
img.show()