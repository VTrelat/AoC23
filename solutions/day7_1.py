import collections
with open('/Users/vincent/Documents/AoC23/inputs/input7.txt', 'r') as f:
    data = [i for i in f.read().split('\n') if i.strip()]

cards = '23456789TJQKA'
def hand(h):
    h2 = [cards.index(i)for i in h]
    ts = []
    for r in cards:
        c = collections.Counter(h)
        p = tuple(sorted(c.values()))
        t = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(p)
        ts.append(t)
    return (max(ts), *h2)
h = sorted((hand(h), int(b)) for h, b in (l.split() for l in data))
t = 0
for i,(_,b) in enumerate(h):
    t+=i*b+b
print(t)