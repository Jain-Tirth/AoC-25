with open('input.txt', 'r') as f:
    banks = f.read().split()

res = 0
for bank in banks:
    max_jolt = 0
    # For each position as the first digit
    for i in range(len(bank) - 1):
        first_digit = int(bank[i])
        # Find the maximum digit after position i
        max_second = max(int(bank[j]) for j in range(i + 1, len(bank)))
        curr_jolt = first_digit * 10 + max_second
        max_jolt = max(curr_jolt, max_jolt)
    res += max_jolt

print(res)