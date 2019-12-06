f = open("Intcodes.txt", "r")
intcodes = f.read().split(',')
f.close()
# Convert intcode list of strings to ints
intcodes = [int(x) for x in intcodes]
intcodes[1] = 0
intcodes[2] = 1

index = 0

while index < len(intcodes):
    code = int(intcodes[index])
    if code == 1:
        a = intcodes[int(intcodes[index + 1])]
        b = intcodes[int(intcodes[index + 2])]
        intcodes[intcodes[index + 3]] = a + b
        index += 4
        continue
    if code == 2:
        a = intcodes[intcodes[index + 1]]
        b = intcodes[intcodes[index + 2]]
        intcodes[intcodes[index + 3]] = a * b
        index += 4
        continue
    if code == 99:
        break
    else:
        raise Exception("Unidentified intcode encountered")

print("Value at position zero is: " + str(intcodes[0]))
