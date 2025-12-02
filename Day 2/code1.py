with open('input.txt', 'r') as f:
    data = f.read().split(',')

count = 0
for num in data:
    start, end = num.split('-')
    for i in range(int(start), int(end) + 1):
        curr = str(i)
        if len(curr) % 2 == 0:
            mid = len(curr) // 2
            if curr[:mid] == curr[mid:]:  
                print(curr, " -> invalid (", curr[:mid], curr[mid:], ")")
                count += i  
print("Sum of invalid IDs:", count)
