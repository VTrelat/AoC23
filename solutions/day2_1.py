with open('/Users/vincent/Documents/AoC23/inputs/input2.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

lines = [l[l.index(": ")+1:].strip() for l in data]

max_cubes = {
    "red":12,
    "green":13,
    "blue":14
}
valid_line_sum = 0
impossible = []
for idx in range(len(lines)):
    l = lines[idx]
    handfuls = l.split(';')
    valid = True
    for h in handfuls:
        if not valid:
            break
        cubes = [c.strip() for c in h.split(',')]
        for c in cubes:
            num = int(c.split(' ')[0])
            color = c.split(' ')[1]
            if num > max_cubes[color]:
                impossible.append(idx + 1)
                valid = False
                break

    if valid:
        valid_line_sum += idx + 1
print(valid_line_sum)
print(impossible)