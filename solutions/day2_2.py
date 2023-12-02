with open('/Users/vincent/Documents/AoC23/inputs/input2.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

lines = [l[l.index(": ")+1:].strip() for l in data]

power_sum = 0

for idx in range(len(lines)):
    l = lines[idx]
    handfuls = l.split(';')

    maxs = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for h in handfuls:
        cubes = [c.strip() for c in h.split(',')]
    
        for c in cubes:
            num = int(c.split(' ')[0])
            color = c.split(' ')[1]
            maxs[color] = max(maxs[color], num)

    power = 1
    for val in maxs.values():
        power *= val
    power_sum += power
            
print(power_sum)