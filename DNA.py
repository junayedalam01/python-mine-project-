# Define the text
text = "Junayed Alam Biswas"

# Convert to binary
binary_str = ''.join(format(ord(c), '08b') for c in text)

# Map 2 bits to 1 nucleotide: 00->A, 01->C, 10->G, 11->T
mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
dna_seq = ''.join(mapping[binary_str[i:i+2]] for i in range(0, len(binary_str), 2))

print(f"Binary length: {len(binary_str)}")
print(f"Binary: {binary_str}")
print(f"DNA length: {len(dna_seq)}")
print(f"DNA: {dna_seq}")
