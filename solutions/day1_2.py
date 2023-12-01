from day1_1 import part1

with open('/Users/vincent/Documents/AoC23/inputs/input1.txt', 'r') as f:
    data = f.read().strip().replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine')

print(part1(data))