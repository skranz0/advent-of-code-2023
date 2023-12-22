import re

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class Game:
    def __init__(self, id: int, rounds):
        self.id = id
        self.rounds = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in rounds:
            for pull in round:
                if re.match("[0-9]red", pull) is not None:
                    new_red = int(re.sub("red", "", pull))
                    self.rounds["red"] += new_red
                elif re.match("[0-9]blue", pull) is not None:
                    new_blue = int(re.sub("blue", "", pull))
                    self.rounds["blue"] += new_blue
                elif re.match("[0-9]green", pull) is not None:
                    new_green = int(re.sub("green", "", pull))
                    self.rounds["green"] += new_green


games = []
with open("2-tiny.txt", "r") as file:
    for line in file:
        line = re.sub("\n| |Game", "", line)
        id = int(line.split(":")[0])
        line = re.sub("[0-9]:", "", line)
        sets = line.split(";")
        rounds = []
        for s in sets:
            s = s.split(",")
            rounds.append(s)
        new_game = Game(id, rounds)
        games.append(new_game)

possible = 0
for game in games:
    if game.rounds["red"] > bag["red"] or game.rounds["green"] > bag["green"] or game.rounds["blue"] > bag["blue"]:
        print(f"Game {game.id} not possible")
        break
    possible += game.id
print(possible)
