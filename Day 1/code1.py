with open('input.txt', 'r') as f:
    data = f.read().split(',')
curr = 50
count = 0
for num in data:
    direction = num[0]
    clicks = int(num[1:])
    if direction == 'R':
        curr += clicks
    else:
        curr -= clicks
    curr %= 100
    if curr == 0:
        count+= 1
print(count)