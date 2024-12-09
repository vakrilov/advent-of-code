# %%
import os

file = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in file.readlines()]

# %%

line = lines[0]

id = 0
is_file = True
disk = []
for i in range(len(line)):
    file_size = int(line[i])
    if is_file:
        disk += [id] * file_size
        id += 1
    else:
        disk += [-1] * file_size

    is_file = not is_file


def p():
    for x in disk:
        print(x if x >= 0 else ".", end="")
    print()


p()
# %%
write_idx = 0
read_idx = len(disk) - 1

while write_idx <= read_idx:
    while disk[read_idx] == -1:
        read_idx -= 1

    while disk[write_idx] != -1:
        write_idx += 1

    if write_idx >= read_idx:
        p()
        print("DONE!")
        break

    disk[write_idx] = disk[read_idx]
    disk[read_idx] = -1

# %%
part1_result = 0
for i in range(len(disk)):
    if disk[i] == -1:
        break
    part1_result += disk[i] * i


print("part1", part1_result)

# %%

free_blocks = []
files = []

idx = 0
file_idx = 0
is_file = True

for ch in line:
    size = int(ch)

    if is_file:
        files.append([idx, size, file_idx])
        file_idx += 1
    else:
        free_blocks.append([idx, size])

    idx += size
    is_file = not is_file

# %%
for file in reversed(files):
    file_idx, file_size, file_name = file

    for i, free in enumerate(free_blocks):
        free_idx, free_size = free
        if free_size >= file_size and free_idx < file_idx:
            file[0] = free_idx
            free[0] = free_idx + file_size
            free[1] = free_size - file_size
            break

# %%
part2_result = 0
for idx, size, name in files:
    part2_result += sum([i * name for i in range(idx, idx + size)])

print("part2", part2_result)
# %%
