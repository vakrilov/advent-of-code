f = open("./input.txt", "r")
str = f.read()
l = len(str)

sum = 0
for i in range(l):
  if str[i] == str[(i + l//2)%l]:
    sum += int(str[i])

print(sum)