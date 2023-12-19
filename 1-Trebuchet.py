import re

with open("1-Trebuchet.txt", "r") as file:
    sum = 0
    for line in file:
        numbers = re.sub('[a-z]+', '', line)
        # TODO get first and last digit

print(sum)