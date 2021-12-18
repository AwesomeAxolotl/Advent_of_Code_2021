from operator import mul
from functools import reduce

b = None
ver = 0
# returns the value of a packet
# literal packets return their value
# operator packets parse their subpackets then return their value after op
# subpackets of an operator packet do not count towards length or remaining packets
# in: c - cursor

# out: new_cursor, value_from_packet

def calculate(type, arr):
    if type == 0:
        return(sum(arr))
    elif type == 1:
        return(reduce(mul, arr))
    elif type == 2:
        return(min(arr))
    elif type == 3:
        return(max(arr))
    elif type == 5:
        return(arr[0] > arr[1])
    elif type == 6:
        return(arr[0] < arr[1])
    elif type == 7:
        return(arr[0] == arr[1])



def parsePacket(c):
    global b, ver
    
    if c > len(b) - 7:
        return False
    
    ver += int(b[c:c+3], 2)
    t = int(b[c+3:c+6], 2)
    
    if t == 4:
        i = 0
        numstring = ""
        while True:
            numstring += b[c+7+5*i:c+11+5*i]
            if b[c+6+5*i] == "0":
                return (c+11+5*i), int(numstring, 2)
            i += 1
    
    elif b[c+6] == "0":
        #length based
        l = int(b[c+7:c+22], 2)
        
        next = c + 22
        packet_values = []
        while (next - c - 22) < l:
            next, val = parsePacket(next)
            packet_values.append(val)
            if next is False:
                break
        val = calculate(t, packet_values)
        return (c+22+l), val
    
    
    else:
        #sub packet num based
        l = int(b[c+7:c+18], 2)
        count = 0
        next = c + 18
        packet_values = []
        while count < l:
            next, val = parsePacket(next)
            packet_values.append(val)
            count += 1
        val = calculate(t, packet_values)
        return next, val



with open("tag16.txt") as f:
    b = bin(int(f.readline().rstrip(), 16))[2:]
    if len(b) % 4 != 0:
        missing = 4 - (len(b) % 4)
        b = "0" * missing + b
    
    next = 0
    while True:
        try:
            next, val = parsePacket(next)
            print(f"part 2: {val}")
        except:
            print(f"part 1: {ver}")
            exit()
        if not next:
            break
print(f"part 1: {ver}")