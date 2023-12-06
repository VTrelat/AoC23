with open('/Users/vincent/Documents/AoC23/inputs/input6.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

def ways_to_beat_record(t, d):
    ways = 0
    for hold_time in range(1, t+1):
        speed = hold_time
        remaining_time = t - hold_time
        curd = speed * remaining_time
        if curd > d:
            ways += 1
    return ways

races = []
for t,d in zip(list(filter(lambda x: len(x) > 0, data[0].split(":")[1].strip().split(" "))), list(filter(lambda x: len(x) > 0, data[1].split(":")[1].strip().split(" ")))):
    if t.isdigit() and d.isdigit():
        races.append({"t": int(t), "d": int(d)})

total_ways = 1
for race in races:
    ways = ways_to_beat_record(race["t"], race["d"])
    total_ways *= ways

print(total_ways)