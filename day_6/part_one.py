file_path = r""

total_sum = 0

number_map = []

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        number_map.append(line.split())

for i in range(len(number_map[0])):
    if number_map[4][i] == '+':
        total_sum += int(number_map[0][i]) + int(number_map[1][i]) + int(number_map[2][i]) + int(number_map[3][i])
    else:
        total_sum += int(number_map[0][i]) * int(number_map[1][i]) * int(number_map[2][i]) * int(number_map[3][i])
print(total_sum)
