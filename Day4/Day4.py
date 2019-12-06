import sys

input = [172851, 675869]


def cond_3(digit):
    dig = str(digit)
    index = 0
    while index < len(dig)-1:
        if dig[index] == dig[index + 1]:
            return True
        index += 1
        continue
    return False


def cond_4(digit):
    dig = str(digit)
    index = 0
    while index < len(dig)-1:
        if int(dig[index]) > int(dig[index + 1]):
            return False
        index += 1
        continue
    return True


allowed_combinations = []
i = input[0]
for x in range(input[1] - input[0]):
    condition_1 = len(str(i)) == 6
    condition_2 = input[0] <= i <= input[1]
    condition_3 = cond_3(i)
    condition_4 = cond_4(i)
    if condition_1 and condition_2 and condition_3 and condition_4:
        allowed_combinations.append(i)
    i += 1

print(len(allowed_combinations))
