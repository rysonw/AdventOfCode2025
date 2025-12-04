count = 0

file_path = r""

def is_repeat(input):
    input = str(input)
    if len(input) % 2 != 0:
        return False
    
    mid = len(input) // 2
    return input[:mid] == input[mid:]

sum = 0

with open(file_path, "r") as f:
    for line in f:
        ranges = line.split(",")

    for r in ranges:
        lower_bound = (int)(r.split("-")[0])
        upper_bound = (int)(r.split("-")[1])

        for i in range(lower_bound, upper_bound + 1):
            is_number_repeat = is_repeat(i)

            if is_number_repeat:
                sum += i
            
print(f"\nFinal Sum of Invalid Ids: {sum}")


