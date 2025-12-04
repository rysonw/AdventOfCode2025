file_path = r""

total_sum = 0

def find_first_number(line):
    max_digit = '-1'
    max_index = -1
    
    for i, ch in enumerate(line):
        if i == len(line) - 1:
            continue
        if ch > max_digit:
            max_digit = ch
            max_index = i
        if max_digit == '9':
            return max_index
    
    return max_index


def find_total(line, start_idx):
    subtotal = int(line[start_idx]) * 10

    curr_highest_idx = start_idx + 1

    if curr_highest_idx >= len(line):
        return subtotal

    for i in range(curr_highest_idx + 1, len(line)):
        if line[i] == '9':
            return subtotal + 9
        if line[i] > line[curr_highest_idx]:
            curr_highest_idx = i

    return subtotal + int(line[curr_highest_idx])


with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        print(line)
        if not line:
            continue

        highest_idx = find_first_number(line)
        total = find_total(line, highest_idx)
        print(total)
        total_sum += total

print(f"\nFinal Sum: {total_sum}")
