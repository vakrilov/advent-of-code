import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

card_powers = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

card_powers_jokers = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

def hand_power(hand):
    power = 0
    for i in range(0, 5):
        for j in range(i + 1, 5):
            if hand[i] == hand[j]:
                power += 1
    return power


def hand_power_jokers(hand):
    replacements = "23456789TQKA"
    return max([hand_power(hand.replace("J", i)) for i in replacements])


def card_power(hand):
    power = 0
    for i in range(0, 5):
        power = power * 100 + card_powers[hand[i]]
    return power

def card_power_jokers(hand):
    power = 0
    for i in range(0, 5):
        power = power * 100 + card_powers_jokers[hand[i]]
    return power

lines = [l.removesuffix("\n") for l in f.readlines()]
hands = []
for line in lines:
    [hand, bid] = line.split(" ")
    hands.append(
        (
            hand,
            int(bid),
            hand_power(hand),
            card_power(hand),
            hand_power_jokers(hand),
            card_power_jokers(hand),
        )
    )

hands.sort(key=lambda x: (x[2], x[3]), reverse=False)
print("part1", sum((r + 1) * hand[1] for r, hand in enumerate(hands)))

hands.sort(key=lambda x: (x[4], x[5]), reverse=False)
print("part2", sum((r + 1) * hand[1] for r, hand in enumerate(hands)))
