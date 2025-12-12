class Node:
    def __init__(self, steps, state):
        self.state = state
        self.steps = steps

from collections import deque
import re

def flip_switches(state, flip_map):
    state = list(state)

    for n in flip_map:
        if state[n] == '.':
            state[n] = '#'
        else:
            state[n] = '.'

    return tuple(state)

def bfs(start, end, possible_presses):
    start_node = Node(0, start)
    q = deque()
    q.append(start_node)
    visited = {start}  

    while q:
        node = q.popleft()

        current_steps = node.steps
        current_state = node.state
        for press in possible_presses:
            next_state = flip_switches(current_state, press)
            if next_state in visited:
                continue
            if next_state == end:
                return current_steps + 1
            visited.add(next_state)
            q.append(Node(current_steps + 1, next_state))
    return 0
            
def solve(file_path):
    moves_used = 0
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            tokens = line.split()

            raw = tokens[0]
            end = raw.strip("[]")
            end_tup = tuple(end)

            moves = []
            for token in tokens[1:]:
                if token.startswith("{"):
                    break

                nums = re.findall(r"\d+", token)
                moves.append([int(n) for n in nums])

            start = tuple("." for _ in end)

            moves_used += bfs(start, end_tup, moves)

    return moves_used

if __name__ == "__main__":
    file_path = r""
    answer = solve(file_path)
    print(f"Min Number of Moves Used: {answer}")
