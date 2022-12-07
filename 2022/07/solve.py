import os
f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="utf-8")


class File:
    def __init__(self, name, parent, file_type="dir", size=-1):
        self.name = name
        self.size_cache = size
        self.file_type = file_type
        self.parent = parent
        self.level = 0 if parent is None else parent.level + 1
        self.children = []

    def add(self, file):
        self.children.append(file)
        self.size_cache = -1

    def get_size(self):
        if self.file_type == "file":
            return self.size_cache

        if self.size_cache == -1:
            self.size_cache = sum(map(lambda f: f.get_size(), self.children))

        return self.size_cache

    def __str__(self):
        return "  " * self.level + f'{self.name} ({self.file_type}) {self.get_size()}\n'

    def visit(self):
        yield self
        for child in self.children:
            yield from child.visit()


current = root = File("/", None, "dir")
for line in f.readlines():
    split = line.split()

    if split[0] == "$":
        if split[1] == "cd":
            arg = split[2]
            if arg == "/":
                current = root
            elif arg == "..":
                current = current.parent
            else:
                current = next(f for f in current.children if f.name == arg)
    elif line.startswith("dir"):
        current.add(File(split[1], current))
    else:
        current.add(File(split[1], current, "file", int(split[0])))

print(*root.visit())

dir_sizes = [f.get_size() for f in root.visit() if f.file_type == "dir"]
target = root.get_size() - 40000000

print("Part 1:", sum(s for s in dir_sizes if s <= 100000))
print("Part 2:", min(s for s in dir_sizes if s >= target))
