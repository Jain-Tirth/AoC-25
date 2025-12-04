with open("input.txt") as f:
    data = [line.strip() for line in f]

accessed = 0
for row_idx in range(len(data)):
    for col_idx in range(len(data[0])):
        if data[row_idx][col_idx] != '@':
            continue

        count_neighbors = 0
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            new_row = row_idx + dr
            new_col = col_idx + dc
            if 0 <= new_row < len(data) and 0 <= new_col < len(data[0]):
                if data[new_row][new_col] == '@':
                    count_neighbors += 1

        if count_neighbors < 4:
            accessed += 1

print(accessed)
