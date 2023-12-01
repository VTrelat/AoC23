with open('/Users/vincent/Documents/AoC23/inputs/input1.txt', 'r') as f:
    data = f.read().strip()

def part1(data : str) -> int:
    ans = 0

    for line in data.split():
        first = ""
        last = ""
        for c in line:
            if c.isdigit() and first == "":
                first = c
            if c.isdigit():
                last = c

        num = int(first + last)
        ans += num


    return ans

if __name__ == "__main__":
    print(part1(data))