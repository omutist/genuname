#!/usr/bin/env python3



import random
import string

# Function to generate random sequences
def generate_random_sequences(num_sequences=10, length=8):
    sequences = []
    for _ in range(num_sequences):
        sequence = ''.join(random.choices(string.ascii_lowercase, k=length))
        sequences.append(sequence)
    return sequences

# Generate and print the sequences
if __name__ == "__main__":
    random_sequences = generate_random_sequences()
    for seq in random_sequences:
        print(seq)




