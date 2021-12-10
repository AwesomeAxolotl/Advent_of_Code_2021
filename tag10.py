points = {")": 3, "]": 57, "}": 1197, ">": 25137, "(":1, "[":2, "{":3, "<":4}
match = {")": "(", "]": "[", "}": "{", ">": "<"}
total = 0
totals_p2 = []

with open("tag10.txt") as f:
    for line in f:
        stack = []
        corrupt = False
        line = line.strip()
        for c in line:
            if c in ["(", "[", "{", "<"]:
                stack.append(c)
            else:
                if stack[-1] == match[c]:
                    stack.pop()
                else:
                    total += points[c]
                    corrupt = True
                    break
        
        #part 2
        p2 = 0
        if not corrupt and len(stack) > 0:
            for i in reversed(stack):
                p2 = p2 * 5 + points[i]
            totals_p2.append(p2)


print(total)
totals_p2.sort()
print(totals_p2[int(len(totals_p2)*0.5)])