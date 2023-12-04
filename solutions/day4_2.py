with open('/Users/vincent/Documents/AoC23/inputs/input4.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

p2 = 0
multiplier = [1 for i in data]
for i,l in enumerate(data):
	winning = set([int(x) for x in l.split(":")[1].split("|")[0].strip().split()])
	have = set([int(x) for x in l.split("|")[1].strip().split()]).intersection(winning)
	curmult = multiplier[i]
	for j in range(i+1,min(i+len(have)+1, len(data))):
		multiplier[j]+=curmult
	p2 += curmult
print(p2)