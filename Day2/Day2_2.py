import sys

f = open("Intcodes.txt", "r")
initial_intcodes = f.read().split(',')
f.close()


def parse_intcodes(noun, verb):
    table = [int(x) for x in initial_intcodes]
    table[1] = noun
    table[2] = verb
    index = 0

    while index < len(table):
        code = int(table[index])
        if code == 1:
            a = table[int(table[index + 1])]
            b = table[int(table[index + 2])]
            table[table[index + 3]] = a + b
            index += 4
            continue
        if code == 2:
            a = table[table[index + 1]]
            b = table[table[index + 2]]
            table[table[index + 3]] = a * b
            index += 4
            continue
        if code == 99:
            break
        else:
            raise Exception("Unidentified intcode encountered: " + str(code) + " for index: " + str(index))
    return table


def find_combination(target_output):
    noun = 0
    verb = 0
    while noun <= 99:
        verb = 0
        while verb <= 99:
            intcodes = parse_intcodes(noun, verb)
            if intcodes[0] == target_output:
                return [noun, verb]
            verb += 1
        noun += 1


combination = find_combination(19690720)
print(100*combination[0]+combination[1])
