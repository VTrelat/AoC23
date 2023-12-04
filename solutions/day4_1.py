with open('/Users/vincent/Documents/AoC23/inputs/input4.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

p1 = 0
for i,l in enumerate(data):
	winning = set([int(x) for x in l.split(":")[1].split("|")[0].strip().split()])
	have = set([int(x) for x in l.split("|")[1].strip().split()]).intersection(winning)
	if len(have):
		p1 += 2**(len(have)-1)

print(p1)