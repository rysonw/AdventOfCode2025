def is_all_points_valid(rp1, rp2):
    return True

def solve(file_path):
    points = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            coords = (line.split(','))
            coords[0] = int(coords[0])
            coords[1] = int(coords[1])
            points.append(coords)

    # Calculate new area to work out of
    # Keep a set full of new green points
    # When calculating the area, check each coordinate in the border and inside to see if it is in the set
    # If all points are in set "green_points", it is a valid rec and can be used for max_area

    green_points = set()
    # Build green points set, add green points along the border first
    for i, (x1, y1) in enumerate(points):
        first_pair = points[i - 1]
        second_pair = points[i + 1]

        # One coord from each pair matches og pair
        if first_pair[0] == x1:
            for i in range(y1 + 1, first_pair[1] + 1):
                green_points.add((x1, i))
        else:
            for i in range(x1 + 1, first_pair[0] + 1):
                green_points.add((i, y1))
        if second_pair[0] == x1:
            for i in range(y1 + 1, second_pair[1] + 1):
                green_points.add((x1, i))
        else:
            for i in range(x1 + 1, second_pair[0] + 1):
                green_points.add((i, y1))

    # Fill area, add green points to set

    # max_area = 0
    # for (x1, y1) in points:
    #     for (x2, y2) in points:
    #         if (x1, y1) != (x2, y2) and is_all_points_valid((x1, y1), (y1, y2)):
    #             max_area = max(max_area, abs(x1 - x2) * abs(y1 - y2))
    
    # return max_area


if __name__ == "__main__":
    file_path = r""
    answer = solve(file_path)
    print(f"Max Area: {answer}")