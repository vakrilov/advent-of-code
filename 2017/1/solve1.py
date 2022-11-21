f = open("./input.txt", "r")
str = f.read()
str = str + str[0]

sum =0
for i in range(len(str)-1):
  if str[i] == str[i+1]:
    sum += int(str[i])

print(sum)