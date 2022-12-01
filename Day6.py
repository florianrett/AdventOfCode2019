import InputGetter as IG

input = IG.GetInput(6)

test = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L"
test2 = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L,K)YOU,I)SAN"

# Functions
def GetNumOrbits(o, n):
    num = n
    if o in orbits:
        for c in orbits[o]:
            num += GetNumOrbits(c, n+1)
    
    #print("Get orbits for ", o, " ", num)        
    return num

# =================================================================================================================================================
# Actual Programm

split = input
orbits = dict()
centers = dict()

# =================================================================================================================================================
# Part 1
print("Starting Programm")

numOrbits = 0
for o in split:
    s = o.split(')')
    if s[0] in orbits:
        orbits[s[0]].append(s[1])
    else:
        orbits.__setitem__(s[0], [s[1]])

print("Part 1: ", GetNumOrbits("COM", 0))

# =================================================================================================================================================
#Part 2
print("Starting Part 2")

for os in orbits.keys():
    for o in orbits[os]:
        centers.__setitem__(o, os)

start = centers["YOU"]
end = centers["SAN"]
you = []
san = []
current = start
while current != "COM":
    current = centers[current]
    you.append(current)
current = end
while current != "COM":
    current = centers[current]
    san.append(current)

you.reverse()
san.reverse()

n = 0
while(n < you.__len__() and n < san.__len__() and you[n] == san[n]):
    n += 1

n -= 1

print("Part 2: ", you.__len__() + san.__len__() - 2 * n)