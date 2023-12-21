import re

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class game:
    def __init__(self, id, games):
        self.id = id
        self.games = games



with open("2-tiny.txt", "r") as file:
    games = []
    for line in file:
        line = re.sub("\n| |Game", "", line)
        id = int(line.split(":")[0])
        line = re.sub("[0-9]:", "", line)
        sets = line.split(";")
        for s in sets:
            s = s.split(",")
