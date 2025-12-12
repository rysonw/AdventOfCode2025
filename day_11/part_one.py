def dfs(key, visited, map):
    # Cycle
    if key in visited:
        return 0
    if key == "out":
        return 1
    
    visited.add(key)
    steps = map[key]

    count = 0
    
    for step in steps:
        count += dfs(step, visited, map)
    
    visited.remove(key)
    return count

def solve(file_path):
    with open(file_path, "r") as f:
        word_map = {}
        for line in f:
            line = line.strip()
            if not line:
                continue

            parsed_line = line.split()
            word_map[parsed_line[0][0:3]] = tuple(parsed_line[1:])

    return dfs("you", set(), word_map)

if __name__ == "__main__":
    file_path = r""
    answer = solve(file_path)
    print(f"Number of Valid Paths: {answer}")
