def check_sequence(seq):
    return (
        all(0 < seq[i+1] - seq[i] <= 3 for i in range(len(seq)-1)) or
        all(-3 <= seq[i+1] - seq[i] < 0 for i in range(len(seq)-1)))

with open('day2-data.txt') as file:
    sequences = [list(map(int, line.strip().split())) for line in file]

num_valid = sum(check_sequence(seq) for seq in sequences)

num_valid_2 = sum( any(check_sequence(seq[:i] + seq[i+1:]) for i in range(len(seq)+1)) for seq in sequences)

print("Part 1:", num_valid)
print("Part 2:", num_valid_2)