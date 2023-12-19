import re

with open("1-Trebuchet.txt", "r") as file:
    sum = 0
    for line in file:
        numbers = re.sub('[a-z]', '', line)[0:-1]
        value = int(numbers[0] + numbers[-1])
        sum += value

print(sum)