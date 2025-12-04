with open("input.txt") as f:
    # Small changes from code1 of Day 4
    # Each line.strip() is string, they are immutable and cannot be changed in place.
    # Converting them into list so they can be changed in place.
    data = [list(line.strip()) for line in f.readlines()]
accessed = 0
while True:
    removed = []
    for row_idx in range(len(data)):
        for col_idx in range(len(data[row_idx])):
            if data[row_idx][col_idx] != '@':
                continue

            count_neighbors = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                new_row = row_idx + dr
                new_col = col_idx + dc
                if 0 <= new_row < len(data) and 0 <= new_col < len(data[row_idx]):
                    if data[new_row][new_col] == '@':
                        count_neighbors += 1
                

            if count_neighbors < 4:
                removed.append((row_idx, col_idx))
    if len(removed) == 0:
        break
    for row, col in removed:
        data[row][col] = '.'
    accessed += len(removed)
print(accessed)
