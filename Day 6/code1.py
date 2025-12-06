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

# Identify problems by finding columns that are all spaces (separators)
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

# Extract numbers and operations from each problem
results = []
for problem_cols in problems:
    # Combine columns for this problem and extract numbers/operation
    problem_lines = []
    for row_idx in range(len(problem_cols[0])):
        line = ''.join(col[row_idx] if row_idx < len(col) else ' ' for col in problem_cols).strip()
        if line:
            problem_lines.append(line)
    
    # Last line is operation, previous lines are numbers
    if problem_lines:
        operation = problem_lines[-1]
        numbers = [int(n) for n in problem_lines[:-1]]
        
        # Perform the operation
        if operation == '+':
            result = sum(numbers)
        elif operation == '*':
            result = 1
            for n in numbers:
                result *= n
        results.append(result)

print(sum(results))

