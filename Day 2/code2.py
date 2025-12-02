with open('input.txt', 'r') as f:
    data = f.read().split()

count = 0
for num in data:
    start, end = num.split('-')
    for i in range(int(start), int(end) + 1):
        curr = str(i)
        length = len(curr)
        for j in range(1, length // 2 + 1):
            if (length % j == 0):
                substr = curr[:j]
                repeated = substr * (length // j)
                if repeated == curr:
                    count += i   
                    break
print("Sum of invalid IDs:", count)
