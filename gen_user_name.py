#!/usr/bin/env python3



import random
import string
import sys
import argparse

# List of characters to exclude
excluded_chars = ['j']

# Function to generate random sequences
def generate_random_sequences(num_sequences=10, length=6, substring='', position='any'):
    # Check the length of the substring
    if len(substring) >= length:
        print("Error: The length of the substring must be less than the length of the generated string.")
        sys.exit(1)

    # Form the set of allowed characters, excluding specified letters
    allowed_chars = ''.join(c for c in string.ascii_lowercase if c not in excluded_chars)
    vowels = 'aeiou'
    
    sequences = []
    while len(sequences) < num_sequences:
        # Generate a random sequence
        sequence = ''.join(random.choices(allowed_chars, k=length - len(substring)))
        
        # Ensure the sequence contains at least two vowels
        if sum(1 for char in sequence if char in vowels) < 2:
            continue
        
        # Determine the insert position based on the specified option
        if position == 'left':
            final_sequence = substring + sequence
        elif position == 'middle':
            insert_position = length // 2 - len(substring) // 2
            final_sequence = sequence[:insert_position] + substring + sequence[insert_position:]
        elif position == 'right':
            final_sequence = sequence + substring
        else:  # 'any'
            insert_position = random.randint(0, length - len(substring))
            final_sequence = sequence[:insert_position] + substring + sequence[insert_position:]
        
        sequences.append(final_sequence)
    return sequences

# Generate and print the sequences
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random sequences.")
    parser.add_argument('-s', '--str', type=str, default='', help="String to be included in the sequence.")
    parser.add_argument('-l', '--length', type=int, default=6, help="Length of the generated sequence (default is 6).")
    parser.add_argument('-p', '--position', type=str, choices=['left', 'middle', 'right', 'any'], default='any', help="Position of the substring in the sequence (default is any).")
    
    args = parser.parse_args()

    random_sequences = generate_random_sequences(length=args.length, substring=args.str, position=args.position)
    for seq in random_sequences:
        print(seq)







