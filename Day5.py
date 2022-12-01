import InputGetter as IG

input = IG.GetInput(5)[0].split(',')

test = [3,0,4,0,99]
test2 = [1101,100,-1,4,0]
test3 = [3,9,8,9,10,9,4,9,99,-1,8]
test4 = [3,9,7,9,10,9,4,9,99,-1,8]
test5 = [3,3,1108,-1,8,3,4,3,99]
test6 = [3,3,1107,-1,8,3,4,3,99]
test7 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
test8 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
test9 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


mem = []
inputValue = 1

for i in input:
    mem.append(int(i))
for i in range(10):
    mem.append(0)

# Functions
def HandleInstruction(code, p1, p2, p3):
    paramModes = []
    paramModes.append(int(code / 100) % 10)
    paramModes.append(int(code / 1000) % 10)
    paramModes.append(int(code / 10000) % 10)
    
    #get actual opcode
    opcode = code % 100

    #get actual parameter values
    #param 1
    if(paramModes[0] == 0):
        v1 = mem[p1]
    elif(paramModes[0] == 1):
        v1 = p1
        
    if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
        #param 2
        if(paramModes[1] == 0):
            v2 = mem[p2]
        elif(paramModes[1] == 1):
            v2 = p2
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:        
        #param 3
        if(paramModes[2] == 0):
            v3 = p3
        elif(paramModes[2] == 1):
            print("Target Parameter is in immediate mode! This should not be happening")

    if opcode == 1:
        mem[v3] = v1 + v2
        return 4
    elif opcode == 2:
        mem[v3] = v1 * v2
        return 4
    elif opcode == 3:
        mem[p1] = inputValue
        # Input value is always 1 for now
        return 2
    elif opcode == 4:
        print("Output: ", v1)
        return 2
    elif opcode == 5:
        if v1 != 0:
            return v2 - ins
        else:
            return 3
    elif opcode == 6:
        if v1 == 0:
            return v2 - ins
        else:
            return 3
    elif opcode == 7:
        if v1 < v2:
            mem[p3] = 1
        else:
            mem[p3] = 0
        return 4
    elif opcode == 8:
        if v1 == v2:
            mem[p3] = 1
        else:
            mem[p3] = 0
        return 4
    else:
        print("encountered unknown opcode: ", opcode)
        print(mem)
        return 0

# =================================================================================================================================================
# Actual Programm

# =================================================================================================================================================
# Part 1
print("Starting Programm")


ins = 0
while(mem[ins] != 99):
    numSteps = HandleInstruction(mem[ins], mem[ins+1], mem[ins+2], mem[ins+3])
    if numSteps == 0:
        break
    else:
        ins += numSteps

