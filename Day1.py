import InputGetter

test = "12,14,1969,100756"
test2 = "100756"

# Functions
def GetFuel(mass):
    return max(0, int(mass / 3) - 2)

# =================================================================================================================================================
# Actual Programm

split = InputGetter.GetInput(1)

# =================================================================================================================================================
# Part 1
print("Starting Programm")

fuelsum = 0

for i in split:
    fuelsum += GetFuel(int(i))

print("Part 1: ", fuelsum)

# =================================================================================================================================================
#Part 2
print("Starting Part 2")

fuelsum = 0

for i in split:
    module = int(i)
    while module > 0:
        module = GetFuel(module)
        fuelsum += module

print("Part 2: ", fuelsum)