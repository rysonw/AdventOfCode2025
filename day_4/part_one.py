file_path = r""

valid_walls = 0

grid = []

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        grid.append(line)

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

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == "@":
            is_valid = if_valid(r, c)

            if is_valid:
                valid_walls += 1


print(f"\nValid Wall Count: {valid_walls}")
