# NOT FINISHED

file_path = r"C:\Users\ryson\Desktop\Anything CS\Advent Of Code\2025\day_7\input.txt"

grid = []

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        row = []
        for c in line:
            row.append(c)

        grid.append(row)

s_col = -1

ROWS = len(grid)
COLS = len(grid[0])
path_count = 0
starting_col = 0

for i, c in enumerate(grid[0]):
    if c == 'S':
        grid[1][i] = '|'
        starting_col = i

def dfs(r, c, grid):
    global path_count
    
    if r == ROWS - 1:
        path_count += 1
        return
    
    original = grid[r][c]
    grid[r][c] = '|'
    
    if r + 1 < ROWS:
        if grid[r + 1][c] == '^':
            if c - 1 >= 0 and grid[r + 1][c - 1] != '|':
                dfs(r + 1, c - 1, grid)
            if c + 1 < COLS and grid[r + 1][c + 1] != '|':
                dfs(r + 1, c + 1, grid)
        else:
            if grid[r + 1][c] != '|':
                dfs(r + 1, c, grid)
    
    grid[r][c] = original

dfs(1, starting_col, grid)
    
print(f"Split Count: {path_count}")
