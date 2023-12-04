import os
import string

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")


lines = [l.removesuffix("\n") for l in f.readlines()]


def parse_round(str):
    result = [0, 0, 0]
    for val_str in str.split(","):
        value = int(val_str.strip(string.ascii_letters + string.whitespace))
        if val_str.find("red") != -1:
            result[0] = value
        elif val_str.find("green") != -1:
            result[1] = value
        else:
            result[2] = value

    return result


def parse_game(line):
    return [parse_round(round_str.strip()) for round_str in line.split(";")]


def is_valid(game, constraint):
    for round in game:
        if (
            round[0] > constraint[0]
            or round[1] > constraint[1]
            or round[2] > constraint[2]
        ):
            return False
    return True



games = [ parse_game(line[line.index(":") + 2 :]) for line in lines]

res = 0
for game_num, game in enumerate(games):
    if is_valid(game, [12, 13, 14]):
        res += game_num + 1


print("part1:", res)


games = [parse_game(line[line.index(":") + 2 :]) for line in lines]

res2 = 0
for game in games:
    min_red = max([r[0] for r in game])
    min_green = max([r[1] for r in game])
    min_blue = max([r[2] for r in game])
    res2 += min_red * min_green * min_blue
print("part2:", res2)
