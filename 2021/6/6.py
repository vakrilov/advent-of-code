import functools
f = open("./2021/6/input.txt", "r")

@functools.cache
def calc(timeTillHatch: int, daysTillCount: int) -> int:
    hatchDay = daysTillCount - timeTillHatch - 1
    return 1 if hatchDay < 0 else calc(6, hatchDay) + calc(8, hatchDay)

fishes = [int(x) for x in f.read().split(",")]
print(sum([calc(fish, 256) for fish in fishes]))
