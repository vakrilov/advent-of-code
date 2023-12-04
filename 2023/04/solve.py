import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

cards = [line[line.index(":") + 2 :].strip() for line in f.readlines()]


def get_points(card: str):
    [win, draw] = card.split("|")
    win_nums = set(int(n) for n in win.strip().split(" ") if len(n) > 0)
    draw_nums = set(int(n) for n in draw.strip().split(" ") if len(n) > 0)

    return len(win_nums.intersection(draw_nums))


matches = [get_points(card) for card in cards]
part1 = sum([2 ** (power - 1) if power > 0 else 0 for power in matches])
print("part1:", part1)

card_counts = [1] * len(matches)

for i in range(0, len(matches)):
    for j in range(1, matches[i] + 1):
        card_counts[i + j] += card_counts[i]

part2 = sum(card_counts)
print("part2:", part2)
