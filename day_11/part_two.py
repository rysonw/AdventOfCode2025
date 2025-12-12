def dfs(key, has_dac, has_fft, graph, memo):
    # DFS + Memo
    state = (key, has_dac, has_fft)
    if state in memo:
        return memo[state]

    if key == "out":
        if has_dac and has_fft:
            return 1
        else:
            return 0

    count = 0
    for step in graph[key]:
        count += dfs(
            step,
            has_dac or key == "dac",
            has_fft or key == "fft",
            graph,
            memo
        )

    # State in map = from this node down, there are X amount of valid paths -> Pop up to next node
    memo[state] = count
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

    return dfs("svr", False, False, word_map, {})

if __name__ == "__main__":
    file_path = r""
    answer = solve(file_path)
    print(f"Number of Valid Paths: {answer}")
