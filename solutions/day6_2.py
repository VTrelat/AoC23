with open('/Users/vincent/Documents/AoC23/inputs/input6.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

def ways_to_beat_record_single_race(time, record_distance):
    ways = 0
    for hold_time in range(time - 14):
        boat_speed = hold_time + 15
        remaining_time = time - hold_time - 15
        total_distance = boat_speed * remaining_time
        if total_distance > record_distance:
            ways += 1
    return ways

races = []
for t,d in zip(list(filter(lambda x: len(x) > 0, data[0].split(":")[1].strip().split(" "))), list(filter(lambda x: len(x) > 0, data[1].split(":")[1].strip().split(" ")))):
    if t.isdigit() and d.isdigit():
        races.append({"t": int(t), "d": int(d)})

t = int("".join([str(t["t"]) for t in races]))
d = int("".join([str(d["d"]) for d in races]))

ways = ways_to_beat_record_single_race(t,d)
print(ways)