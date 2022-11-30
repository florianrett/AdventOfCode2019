import InputGetter

input = InputGetter.GetInput(3)
input1 = input[0]
input2 = input[1]

test1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
test2 = "U62,R66,U55,R34,D71,R55,D58,R83"
test3 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
test4 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
test5 = "R3,U4"
test6 = "U3,R4"

# Functions
def GetManhattanDistance(x, y):
    return abs(x) + abs(y)

def AddPath(x, y):
    path.add((x, y))
    
def CheckCross(x, y):
    if path.__contains__((x, y)):
        cross.append((x, y))

def AddSteps(x, y, i):
    if steps.__contains__((x, y)) == False:
        steps.__setitem__((x, y), i)

def CheckCrossSteps(x, y, i):
    if steps.__contains__((x, y)) == True:     
        cross.append(i + steps.get((x, y)))

# =================================================================================================================================================
# Actual Programm

wire1 = input1.split(',')
wire2 = input2.split(',')

# =================================================================================================================================================
# Part 1
print("Starting Programm")

path = set()
x = 0
y = 0

cross = []

for i in wire1:
    if i.startswith('U'):
        for u in range(int(i[1:])):
            y += 1
            AddPath(x, y)      
    elif i.startswith('D'):
        for u in range(int(i[1:])):
            y -= 1
            AddPath(x, y)   
    elif i.startswith('R'):
        for u in range(int(i[1:])):
            x += 1
            AddPath(x, y)   
    elif i.startswith('L'):
        for u in range(int(i[1:])):
            x -= 1
            AddPath(x, y)   
#print(path)

x = 0
y = 0

for i in wire2:
    if i.startswith('U'):
        for u in range(int(i[1:])):
            y += 1
            CheckCross(x, y)
    elif i.startswith('D'):
        for u in range(int(i[1:])):
            y -= 1
            CheckCross(x, y)
    elif i.startswith('R'):
        for u in range(int(i[1:])):
            x += 1
            CheckCross(x, y)
    elif i.startswith('L'):
        for u in range(int(i[1:])):
            x -= 1
            CheckCross(x, y)

#print(cross)
distance = GetManhattanDistance(cross[0][0], cross[0][1])
for i in cross:
    distance = min(distance, GetManhattanDistance(i[0], i[1]))

print("Part 1: ", distance)

# =================================================================================================================================================
#Part 2
print("Starting Part 2")

steps = dict()
x = 0
y = 0
s = 0

cross = []

for i in wire1:
    if i.startswith('U'):
        for u in range(int(i[1:])):
            s += 1
            y += 1
            AddSteps(x, y, s)      
    elif i.startswith('D'):
        for u in range(int(i[1:])):
            s += 1
            y -= 1
            AddSteps(x, y, s)     
    elif i.startswith('R'):
        for u in range(int(i[1:])):
            s += 1
            x += 1
            AddSteps(x, y, s)      
    elif i.startswith('L'):
        for u in range(int(i[1:])):
            s += 1
            x -= 1
            AddSteps(x, y, s)     

#print(steps)

x = 0
y = 0
s = 0

for i in wire2:
    if i.startswith('U'):
        for u in range(int(i[1:])):
            s += 1
            y += 1
            CheckCrossSteps(x, y, s)
    elif i.startswith('D'):
        for u in range(int(i[1:])):
            s += 1
            y -= 1
            CheckCrossSteps(x, y, s)
    elif i.startswith('R'):
        for u in range(int(i[1:])):
            s += 1
            x += 1
            CheckCrossSteps(x, y, s)
    elif i.startswith('L'):
        for u in range(int(i[1:])):
            s += 1
            x -= 1
            CheckCrossSteps(x, y, s)

#print(cross)

minimum = cross[0]
for i in cross:
    minimum = min(minimum, i)

print("Part 2: ", minimum)