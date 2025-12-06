with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Transpose the data to read columns instead of rows
# First, split each row by spaces (handling multiple spaces)
rows = []
for line in data:
    rows.append(list(line))

# Find number of columns
num_cols = max(len(row) for row in rows) if rows else 0

# Read columns
columns = []
for col_idx in range(num_cols):
    column = []
    for row in rows:
        if col_idx < len(row):
            column.append(row[col_idx])
    columns.append(column)

problems = []
current_problem_cols = []

for col in columns:
    # Check if column is all spaces
    if all(c == ' ' for c in col):
        if current_problem_cols:
            problems.append(current_problem_cols)
            current_problem_cols = []
    else:
        current_problem_cols.append(col)

if current_problem_cols:
    problems.append(current_problem_cols)

# Extract numbers and operations from each problem (reading right-to-left)
results = []
for problem_cols in problems:
    # Read each column from right to left to form numbers
    numbers = []
    operation = None
    
    # Process columns right to left
    for col_idx in range(len(problem_cols) - 1, -1, -1):
        col = problem_cols[col_idx]
        # Extract the digits from this column (top to bottom forms the number)
        digits = []
        op_char = None
        for char in col:
            if char.isdigit():
                digits.append(char)
            elif char in ['+', '*', '-', '/']:
                op_char = char
        
        # Form the number from digits (top to bottom)
        if digits:
            number = int(''.join(digits))
            numbers.append(number)
        
        # Store the operation (should be same for all columns in a problem)
        if op_char:
            operation = op_char
    
    # Perform the operation
    if numbers and operation:
        if operation == '+':
            result = sum(numbers)
        elif operation == '*':
            result = 1
            for n in numbers:
                result *= n
        results.append(result)

print(sum(results))
