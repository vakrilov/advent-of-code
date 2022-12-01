import os
f = open(os.path.dirname(__file__) + "/input.txt", "r")

top4 = [0, 0, 0, 0]
for line in f.readlines():
    if line == '\n':
        top4.sort()
        top4[0] = 0
    else:
        top4[0] += int(line)

print(top4[-1])
print(sum(top4[-3:-1]))
