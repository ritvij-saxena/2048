import random

GRID_SIZE = 4

def reset_game():
    return [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

def spawn_tile(grid):
    empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = 2 if random.random() < 0.9 else 4

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (GRID_SIZE - len(new_row))
    return new_row

def merge(row):
    for i in range(GRID_SIZE - 1):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row

def move(grid, direction):
    def move_left(grid):
        new_grid = []
        for row in grid:
            compressed = compress(row)
            merged = merge(compressed)
            new_grid.append(compress(merged))
        return new_grid

    if direction == 'left':
        return move_left(grid)
    elif direction == 'right':
        return [row[::-1] for row in move_left([row[::-1] for row in grid])]
    elif direction == 'up':
        transposed = list(map(list, zip(*grid)))
        moved = move_left(transposed)
        return [list(row) for row in zip(*moved)]
    elif direction == 'down':
        transposed = list(map(list, zip(*grid)))
        moved = [row[::-1] for row in move_left([row[::-1] for row in transposed])]
        return [list(row) for row in zip(*moved)]
    return grid

def check_game_over(grid):
    if any(2048 in row for row in grid):
        return "win"
    if not any(0 in row for row in grid):
        for row in grid:
            for i in range(GRID_SIZE - 1):
                if row[i] == row[i + 1]:
                    return None
        for col in range(GRID_SIZE):
            for row in range(GRID_SIZE - 1):
                if grid[row][col] == grid[row + 1][col]:
                    return None
        return "lose"
    return None
