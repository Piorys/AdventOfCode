import math

f = open("Input.txt", "r")

total = 0

for mass in f:

    print("Getting module mass...")
    print("Module mass acquired = " + mass)
    print("Calculating fuel requirement for given mass...")
    fuel_requirement = math.floor(int(mass)/3)-2
    total += fuel_requirement

print(total)
