file_path = r"C:\Users\ryson\Desktop\Anything CS\Advent Of Code\2025\day_6\input.txt"

total_sum = 0

number_map = []

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        number_map.append(line.split())

def create_new_number(nums, operator):
    divisor = 1
    if operator == '+':
        output = 0
    else:
        output = 1

    # 2 loops, first loop checks to see the number of actual ints that are not 0, then we set the multiplier based on this number (10^n)
    # Next loop, iterate and check if the number is 0, if not multiply then divide
    
    for _ in range(4):
        if operator == '+':
            output += (int(nums[0]) // divisor % 10 * 1000) + (int(nums[1]) // divisor % 10 * 100) + (int(nums[2]) // divisor % 10 * 10) + (int(nums[3]) // divisor % 10 * 1)
        else:
            if (int(nums[0]) // divisor % 10 * 1000) + (int(nums[1]) // divisor % 10 * 100) + (int(nums[2]) // divisor % 10 * 10) + (int(nums[3]) // divisor % 10 * 1) == 0:
                continue
            output *= (int(nums[0]) // divisor % 10 * 1000) + (int(nums[1]) // divisor % 10 * 100) + (int(nums[2]) // divisor % 10 * 10) + (int(nums[3]) // divisor % 10 * 1)
        divisor *= 10

    print(output)
    return output

for i in range(len(number_map[0])):
    if number_map[4][i] == '+':
        total_sum += create_new_number([number_map[0][i], number_map[1][i], number_map[2][i], number_map[3][i]], '+')
    else:
        total_sum += create_new_number([number_map[0][i], number_map[1][i], number_map[2][i], number_map[3][i]], '*')

print(total_sum)

