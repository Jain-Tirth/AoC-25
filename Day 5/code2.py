with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Parse ranges until blank line
ranges = []
i = 0
while i < len(data) and data[i] != '':
    ranges.append(data[i])
    i += 1

# Parse ranges into (start, end) tuples and sort them
range_list = []
for range_str in ranges:
    start, end = map(int, range_str.split('-'))
    range_list.append((start, end))

# Sort ranges by start position
range_list.sort()

# Merge overlapping ranges
merged_ranges = []
for start, end in range_list:
    if merged_ranges and start <= merged_ranges[-1][1] + 1:
        # Overlapping or adjacent, merge them
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
    else:
        # Non-overlapping, add new range
        merged_ranges.append((start, end))

# Count total fresh ingredients (inclusive ranges)
total_fresh = 0
for start, end in merged_ranges:
    total_fresh += (end - start + 1)

print(total_fresh)
