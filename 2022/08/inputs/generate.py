import os
from random import randrange

for n in [10, 50, 100, 500, 1000, 5000]:
    f = open(f'{os.path.dirname(__file__)}/input{n}.txt',
             "w", encoding="utf-8")
    for _ in range(n):
        print(_)
        line = [str(randrange(10)) for _ in range(n)]
        f.write("".join(line))
        f.write("\n")
    f.close()
