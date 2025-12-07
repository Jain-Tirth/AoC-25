with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Find the starting position 'S'
start_row, start_col = 0, 0
for i, line in enumerate(data):
    if 'S' in line:
        start_row = i
        start_col = line.index('S')
        break

# Count total splits
from collections import deque

split_count = 0
visited = set()

# Queue: (row, col) - each entry is a beam position
# All beams move downward, one row at a time
queue = deque([(start_row, start_col)])

while queue:
    row, col = queue.popleft()
    
    # Move down one row
    row += 1
    
    # Check bounds
    if row >= len(data) or col < 0 or col >= len(data[0]):
        continue
    
    # Avoid revisiting the same position
    if (row, col) in visited:
        continue
    visited.add((row, col))
    
    current = data[row][col]
    
    if current == '^':
        # Hit a splitter - count it
        split_count += 1
        # Create two new beams: one goes to the left, one to the right
        # Both continue moving downward from their new positions
        queue.append((row, col - 1))
        queue.append((row, col + 1))
    else:
        # Continue this beam downward
        queue.append((row, col))

print(split_count)
