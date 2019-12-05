f = open("Intcodes.txt", "r")
intcodes = f.read().split(',')
f.close()

intcodes[1] = "12"
intcodes[2] = "2"

index = 0

while index < len(intcodes):
    code = int(intcodes[index])
    if code == 1:
        a = intcodes[int(intcodes[index + 1])]
        b = intcodes[int(intcodes[index + 2])]
        intcodes[int(intcodes[index + 3])] = str(int(a) + int(b))
        index += 4
        continue
    if code == 2:
        a = intcodes[int(intcodes[index + 1])]
        b = intcodes[int(intcodes[index + 2])]
        intcodes[int(intcodes[index + 3])] = str(int(a) * int(b))
        index += 4
        continue
    if code == 99:
        break
    else:
        raise Exception("Unidentified intcode encountered")
print("Value at position zero is: " + intcodes[0])
