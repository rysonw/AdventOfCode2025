def solve(file_path):
    space_map = {
        0 : 7,
        1 : 5,
        2 : 7,
        3 : 7,
        4 : 6,
        5 : 7
    }

    valid = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or len(line) < 5:
                continue

            parsed_line = line.split()
            total_area = int(parsed_line[0][0:2]) * int(parsed_line[0][3:5])
            boxes = parsed_line[1:]
            
            total_box_area = 0
            for i, box in enumerate(boxes):
                total_box_area += int(box) * space_map[i]
            if total_area >= total_box_area:
                valid += 1

        return valid

if __name__ == "__main__":
    file_path = r""
    answer = solve(file_path)
    print(f"Valid Regions : {answer}")
