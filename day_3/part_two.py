file_path = r""

def best_12_digit_joltage(line):
    need = 12 # MAX LENGTH
    drop = len(line) - need
    stack = []

    for ch in line:
        while drop > 0 and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)

    stack = stack[:need]
    return int("".join(stack))


total_sum = 0

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        val = best_12_digit_joltage(line)
        print(line, "->", val)
        total_sum += val

print("\nFinal Sum:", total_sum)
