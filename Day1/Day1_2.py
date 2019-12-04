import math

f = open("Input.txt", "r")

total = 0

for mass in f:
    print("Getting module mass")
    print("Module mass acquired = " + mass)
    print("Calculating fuel requirement for given mass")
    fuel_requirement = math.floor(int(mass)/3)-2
    total += fuel_requirement

    print("Checking if additional fuel is required")
    calculate_additional = math.floor(fuel_requirement/3-2) >= 0

    while calculate_additional:
        print("Calculating additional fuel requirement")
        fuel_requirement = math.floor(fuel_requirement/3-2)
        print("Additional fuel requirement has been calculated to " + str(fuel_requirement))
        if fuel_requirement <= 0:
            print("No additional fuel for given mass is required")
            break
        total += fuel_requirement

print(total)
