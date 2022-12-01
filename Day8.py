import InputGetter as IG

input = IG.GetInput(8)[0]

test = "123456789012"
test2 = "0222112222120000"


# Functions
def GetColor(first, second):
    if first == '2':
        return second
    else:
        return first

# =================================================================================================================================================
# Actual Programm

img = input
width = 25
height = 6

# =================================================================================================================================================
# Part 1
print("Starting Programm")

layers = []
size = width * height

for i in range(0, int(img.__len__() / size)):
    start = i * size
    layers.append(img[start : start + size])

layer = ""
fewest = size
for l in layers:
    c = l.count('0')
    if c < fewest:
        fewest = c
        layer = l


print("Part 1: ", layer.count('1') * layer.count('2'))

# =================================================================================================================================================
#Part 2
print("Starting Part 2")

colors = ['2'] * size
for l in layers:
    for i in range(0, size):
        colors[i] = GetColor(colors[i], l[i])

msg = ""
for c in colors:
    msg += c
msg = msg.replace('0', ' ')

for i in range(0, height):
    start = i * width
    print(msg[start : start + width])

#print("Part 2: ", msg)