
def mix(secret, value):
    return value ^ secret

def prune(secret):
    return secret % 16777216

def generate_secrets(initial, num = 2000):
    secret = initial
    secrets = [(secret, secret % 10, -99)]
    for i in range(0, num):
        previous_secret = secret

        # Step 1
        next = secret * 64
        secret = mix(secret, next)
        secret = prune(secret)

        # Step 2
        next = int(secret / 32)
        secret = mix(secret, next)
        secret = prune(secret)

        # Step 3
        next = secret * 2048
        secret = mix(secret, next)
        secret = prune(secret)

        secrets.append((secret, secret % 10, (secret % 10) - (previous_secret % 10)))

    return secrets

secrets = []
with open("day22-data.txt") as f:
    initial_secrets = [int(line) for line in f.readlines()]
    
    sum = 0
    for s in initial_secrets:
        new_secrets = generate_secrets(s, 2000)
        secrets.append(new_secrets)
        sum+=new_secrets[-1][0]
    
    print("Day22 part 1:", sum)

    sequences = {}
    for s in secrets:
        buyer_sequences = set()
        for i in range(1, len(s)-3):
            sequence = (s[i][2], s[i+1][2], s[i+2][2], s[i+3][2])
            price = s[i+3][1]
            if sequence not in buyer_sequences: # only add a sequence once for each buyer
                buyer_sequences.add(sequence)
                if sequence not in sequences:
                    sequences[sequence] = price
                else:
                    sequences[sequence] += price
    
    sorted_sequences = sorted(sequences.items(), key=lambda x:x[1])

    print("Day22 part 2:", sorted_sequences[-1][1])