import InputGetter

input = InputGetter.GetInput(4)[0]
input1 = int(input.split('-')[0])
input2 = int(input.split('-')[1])


test = ""
test2 = ""

# Functions
def TestNumber(n):
    d = []
    d.append(int(n / 100000))
    d.append(int(n % 100000 / 10000))
    d.append(int(n % 10000 / 1000))
    d.append(int(n % 1000 / 100))
    d.append(int(n % 100 / 10))
    d.append(int(n % 10 / 1))

    if d[0] == d[1] or d[1] == d[2] or d[2] == d[3] or d[3] == d[4] or d[4] == d[5]:
        if d[0] <= d[1] and d[1] <= d[2] and d[2] <= d[3] and d[3] <= d[4] and d[4] <= d[5]:
            return True
        else:
            return False
    else:
        return False

def TestNumber2(n):
    d = []
    d.append(int(n / 100000))
    d.append(int(n % 100000 / 10000))
    d.append(int(n % 10000 / 1000))
    d.append(int(n % 1000 / 100))
    d.append(int(n % 100 / 10))
    d.append(int(n % 10 / 1))

    if d[0] <= d[1] and d[1] <= d[2] and d[2] <= d[3] and d[3] <= d[4] and d[4] <= d[5]:
        if (d[0] == d[1] and d[0] < d[2]) or (d[1] == d[2] and d[1] < d[3] and d[0] < d[2]) or (d[2] == d[3] and d[2] < d[4] and d[1] < d[3]) or (d[3] == d[4] and d[3] < d[5] and d[2] < d[4]) or (d[4] == d[5] and d[3] < d[5]):
            return True
        else:
            return False
    else:
        return False 

# =================================================================================================================================================
# Actual Programm



# =================================================================================================================================================
# Part 1
print("Starting Programm")


num = 0
for i in range(input1, input2):
    if TestNumber(i):
        num += 1

print("Part 1: ", num)

# =================================================================================================================================================
#Part 2
print("Starting Part 2")

num = 0
for i in range(input1, input2):
    if TestNumber2(i):
        num += 1

print("Part 2: ", num)