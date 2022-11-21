f = open("./input.txt", "r")

sum = 0
for line in f.readlines():
  parsed = list(map(int, line.split()))
  sum += max(parsed) - min(parsed)

print(sum)


