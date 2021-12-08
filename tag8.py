import re

with open("tag8.txt") as f:
    inputs = [[x.split(" ") for x in l.strip().split(" | ")] for l in f]
    
    # part 1
    c = 0
    for input in inputs:
        for outputs in input[1]:
            if len(outputs) in [2, 3, 4, 7]:
                c += 1 
    print(c)
    
    # part 2
    total = 0
    for input in inputs:
        # looks like I've missed the chars would be ordered differently between input and output..
        input[0] = [''.join(sorted(x)) for x in input[0]]
        decode = {}
        input[0].sort(key = len)
        decode[input[0][0]] = "1"
        decode[input[0][1]] = "7"
        decode[input[0][2]] = "4"
        decode[input[0][9]] = "8"
        #determine 2:
        for sub_input in input[0][3:6]:
            regex = f"[{input[0][2]}]"
            if len(re.findall(regex, sub_input)) == 2:
                decode[sub_input] = "2"
                decode[2] = sub_input
        
        #determine 3 and 5:
        for sub_input in input[0][3:6]:
            regex = f"[{decode[2]}]"
            if len(re.findall(regex, sub_input)) == 4:
                decode[sub_input] = "3"
                decode[3] = sub_input
            elif len(re.findall(regex, sub_input)) == 3:
                decode[sub_input] = "5"
                decode[5] = sub_input
        
        #determine 9:
        for sub_input in input[0][6:9]:
            regex = f"[{decode[3]}]"
            if len(re.findall(regex, sub_input)) == 5:
                decode[sub_input] = "9"
                decode[9] = sub_input
        
        #determine 0 and 6:
        for sub_input in input[0][6:9]:
            regex = f"[{decode[5]}]"
            if len(re.findall(regex, sub_input)) == 5 and sub_input != decode[9]:
                decode[sub_input] = "6" 
            elif len(re.findall(regex, sub_input)) == 4:
                decode[sub_input] = "0"
        
        digits = ""
        for output in input[1]:
            digits += decode[''.join(sorted(output))]
        
        total += int(digits)
    
    print(total)
        
        