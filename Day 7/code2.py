with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Find the starting position 'S'
start_row, start_col = 0, 0
for i, line in enumerate(data):
    if 'S' in line:
        start_row = i
        start_col = line.index('S')
        break

# Use memoization to avoid recomputing paths from same positions
from functools import lru_cache

@lru_cache(maxsize=None)
def count_paths(row, col):
    row += 1
    
    # If reached bottom, this is one complete path
    if row >= len(data):
        return 1
    
    # If out of bounds horizontally, no valid path
    if col < 0 or col >= len(data[0]):
        return 0
    
    current = data[row][col]
    
    if current == '^':
        # Split: count paths from both left and right
        return count_paths(row, col - 1) + count_paths(row, col + 1)
    else:
        # Continue down
        return count_paths(row, col)

timeline_count = count_paths(start_row, start_col)

print(timeline_count)
