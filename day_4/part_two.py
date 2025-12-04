file_path = r""
valid_walls = 0
grid = []
changed = True

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        grid.append(list(line))

ROWS, COLS = len(grid), len(grid[0])

def if_valid(r, c):
    wall_count = 0

    neighbors = [
        (r + 1, c),     # North
        (r - 1, c),     # South
        (r, c + 1),     # East
        (r, c - 1),     # West
        (r - 1, c + 1), # Northwest
        (r + 1, c + 1), # Northeast
        (r - 1, c - 1), # Southwest
        (r + 1, c - 1), # Southeast      
    ]

    for nr, nc in neighbors:
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != '.':
            wall_count += 1

            if wall_count > 3:
                return False
        
    return True

while changed:
    changed = False
    cells_to_change = set()

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '@' and if_valid(r, c):
                cells_to_change.add((r, c))
                valid_walls += 1

    if cells_to_change:
        changed = True
        for r, c in cells_to_change:
            grid[r][c] = '.'

print(f"\nValid Wall Count: {valid_walls}")
