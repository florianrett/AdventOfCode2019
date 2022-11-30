import itertools

input = [3,8,1001,8,10,8,105,1,0,0,21,38,63,80,105,118,199,280,361,442,99999,3,9,102,5,9,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,4,9,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,5,9,101,3,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]
test = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
test2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
test3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
test4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
test5 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

mem = []
inputValue = 5
outputValue = 0

# Functions
def InitProgram():
    global mem
    mem = []
    for i in test4:
        mem.append(int(i))
    for i in range(10):
        mem.append(0)

def HandleInstruction(code, p1, p2, p3):
    paramModes = []
    paramModes.append(int(code / 100) % 10)
    paramModes.append(int(code / 1000) % 10)
    paramModes.append(int(code / 10000) % 10)
    
    #def global variables
    global inputValue
    global outputValue

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
        inputValue = outputValue
        return 2
    elif opcode == 4:
        print("Output: ", v1)
        outputValue = v1
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

phases = [0,1,2,3,4]

inputValue = phases[0]
outputValue = 0
maxOutput1 = 0

perms = list(itertools.permutations(phases))

for permutation in perms:
    outputValue = 0
    for p in permutation:
        inputValue = p
        InitProgram()

        ins = 0
        while(mem[ins] != 99):
            numSteps = HandleInstruction(mem[ins], mem[ins+1], mem[ins+2], mem[ins+3])
            if numSteps == 0:
                break
            else:
                ins += numSteps
        maxOutput1 = max(outputValue, maxOutput1)

print("Part 1 Maximum Output: ", maxOutput1)
print("Part 2 has not been done as I was too lazy to rework the whole implementation of the intcode computer to allow multiple instances running in parallel")
