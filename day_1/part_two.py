count = 0
DIAL_SIZE = 100

file_path = r""


with open(file_path, "r") as f:
    current_num = 50
    
    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        
        try:
            num = int(line[1:]) 
        except ValueError:
            continue 

        
        if direction == 'L':
            if current_num - num < 0:
                count += 1
            current_num = (current_num - num) % DIAL_SIZE

        elif direction == 'R':
            if current_num + num > 99:
                count += 1
            current_num = (current_num + num) % DIAL_SIZE
        
        if current_num == 0:
            count += 1
        
    print(f"\nFinal Password (total times at 0): {count}")
