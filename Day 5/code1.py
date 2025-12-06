with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Parse ranges until blank line
ranges = []
i = 0
while i < len(data) and data[i] != '':
    ranges.append(data[i])
    i += 1

# Skip the blank line
i += 1

# Parse the remaining numbers
numbers = []
while i < len(data):
    if data[i] != '':
        numbers.append(int(data[i]))
    i += 1

fresh_inregdients = 0
for ingredient in numbers:
    is_fresh = False
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        if start <= ingredient <= end:
            is_fresh = True
            break
    
    if is_fresh:
        fresh_inregdients += 1

print(fresh_inregdients)

