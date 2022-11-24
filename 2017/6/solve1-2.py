f = open("./6/input.txt", "r")

banks = list(map(int, f.read().split()))


def gerHash(b: list[int]) -> str:
    return "-".join(map(str, b))


def step(b: list[int], idx: int):
    num = b[idx]
    b[idx] = 0
    for i in range(idx+1, num+idx+1):
        b[i % len(b)] += 1


hashes = {""}
steps = 0
while not gerHash(banks) in hashes:
    # print(gerHash(banks))
    hashes.add(gerHash(banks))
    steps += 1
    idx = banks.index(max(banks))
    step(banks, idx)

print("steps till first duplicate: ", steps)


hashes = {""}
steps = 0
while not gerHash(banks) in hashes:
    # print(gerHash(banks))
    hashes.add(gerHash(banks))
    steps += 1
    idx = banks.index(max(banks))
    step(banks, idx)

print("steps in loop: ", steps)

