file_path = r""

total_sum = 0

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
split_count = 0

for i, c in enumerate(grid[0]):
    if c == 'S':
        grid[1][i] = '|'

for r in range(1, ROWS):
    for c in range(COLS):
        if grid[r][c] == '|':
            if 0 <= r + 1 <= ROWS - 1: # Check in-bounds
                if grid[r + 1][c] == '^': # Check if carrot
                    split_count += 1
                    if 0 <= c + 1 <= COLS - 1 and grid[r + 1][c + 1] != '|':
                        grid[r + 1][c + 1] = '|'
                    if 0 <= c - 1 <= COLS - 1 and grid[r + 1][c - 1] != '|':
                        grid[r + 1][c - 1] = '|'
                else:
                    grid[r + 1][c] = '|'

print(f"Split Count: {split_count}")


