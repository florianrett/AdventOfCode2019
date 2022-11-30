import InputGetter

input = InputGetter.GetInput(2)[0].split(',')

test = [1,1,1,4,99,5,6,0,99]

mem = []

for i in input:
    mem.append(int(i))

# Functions
def HandleInstruction(code, s1, s2, target):
    if code == 1:
        mem[target] = mem[s1] + mem[s2]
    elif code == 2:
        mem[target] = mem[s1] * mem[s2]
    else:
        print("encountered unknown opcode: ", code)

# =================================================================================================================================================
# Actual Programm

# =================================================================================================================================================
# Part 1
print("Starting Programm")

mem[1] = 12
mem[2] = 2

ins = 0
while(mem[ins] != 99):
    HandleInstruction(mem[ins], mem[ins+1], mem[ins+2], mem[ins+3])
    ins += 4

print("Part 1: ", mem[0])

# =================================================================================================================================================
#Part 2
print("Starting Part 2")

for i in range(99):
    for j in range(99):
        mem = []
        for k in input:
            mem.append(int(k))

        mem[1] = i
        mem[2] = j
        ins = 0
        while(mem[ins] != 99):
            HandleInstruction(mem[ins], mem[ins+1], mem[ins+2], mem[ins+3])
            ins += 4

        if mem[0] == 19690720:
            print("Part 2: ", 100 * i + j)