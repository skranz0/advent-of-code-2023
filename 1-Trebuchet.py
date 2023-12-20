import re

def main():
    with open("1-Trebuchet.txt") as file:
        print(f"Part 1: {part_one(file)}")
        print(f"Part 2: {part_two(file)}")

def part_one(file):
    sum = 0
    for line in file:
        numbers = re.sub('[a-z]', '', line)[0:-1]
        value = int(numbers[0] + numbers[-1])
        sum += value
    return sum

def part_two(file):
    number_strings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    sum = 0
    for line in file:
        for key, value in number_strings.items():
            new_line = re.sub(key, value, line)
        value = int(numbers[0] + numbers[-1])
        sum += value
    return sum

if __name__ == "__main__":
    main()
