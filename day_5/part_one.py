file_path = r""

ranges = []
good = 0

def add_range(new_range):
    ranges.append(new_range)
    ranges.sort()

    merged = []
    for r in ranges:
        if not merged or merged[-1][1] < r[0] - 1:
            merged.append(r)
        else:
            merged[-1][1] = max(merged[-1][1], r[1])

    ranges.clear()
    ranges.extend(merged)

def find_good_produce(value):
    global good
    for lo, hi in ranges:
        if value < lo:
            break
        if lo <= value <= hi:
            good += 1
            break

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        lo, hi = map(int, line.split('-'))
        add_range([lo, hi])

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if '-' in line or not line:
            continue
        input = int(line)
        find_good_produce(input)

print(good)
