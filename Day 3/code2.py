with open('input.txt', 'r') as f:
    banks = f.read().split()

res = 0
for bank in banks:
    if len(bank) < 12:
        continue
    
    selected_positions = []
    available = list(range(len(bank)))
    
    for digit_pos in range(12):
        max_val = -1
        max_idx = -1
        
        for i, pos in enumerate(available):
            # Check if there are enough positions left after this one
            remaining_after = len(available) - i - 1
            if remaining_after >= (11 - digit_pos):
                if int(bank[pos]) > max_val:
                    max_val = int(bank[pos])
                    max_idx = i
        
        if max_idx != -1:
            selected_positions.append(available[max_idx])
            available = available[max_idx + 1:]
    
    # Form the 12-digit number
    max_jolt = int(''.join(bank[pos] for pos in selected_positions))
    res += max_jolt

print(res)