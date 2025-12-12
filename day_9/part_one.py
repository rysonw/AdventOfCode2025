def solve(file_path):
    points = []
    max_area = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            coords = (line.split(','))
            coords[0] = int(coords[0])
            coords[1] = int(coords[1])
            points.append(coords)

    for (x1, y1) in points:
        for (x2, y2) in points:
            if (x1, y1) != (x2, y2):
                max_area = max(max_area, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
    
    return max_area


if __name__ == "__main__":
    file_path = r""
    answer = solve(file_path)
    print(f"Max Area: {answer}")
