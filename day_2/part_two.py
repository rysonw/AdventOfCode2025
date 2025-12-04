count = 0

file_path = r""

def is_repeating(s) -> bool:
    s = str(s)
    if len(s) < 2:
        return False
    
    for size in range(1, len(s) // 2 + 1):
        if len(s) % size != 0:
            continue
        
        part = s[:size]
        if part * (len(s) // size) == s:
            return True
    
    return False

sum = 0

with open(file_path, "r") as f:
    for line in f:
        ranges = line.split(",")

    for r in ranges:
        lower_bound = (int)(r.split("-")[0])
        upper_bound = (int)(r.split("-")[1])

        for i in range(lower_bound, upper_bound + 1):
            is_number_repeat = is_repeating(i)

            if is_number_repeat:
                sum += i
            
print(f"\nFinal Sum of Invalid Ids (Part 2): {sum}")


