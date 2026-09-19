def compare_sequences(dna1, dna2):
  matches = 0
  mismatches = 0
  
  for base1, base2 in zip(dna1, dna2):
    if base1 == base2:
      matches += 1
    else:
      mismatches += 1


  similarity = matches / len(dna1) * 100

  return matches, mismatches, similarity



dna1 = "ATGCGTAC"
dna2 = "ATGCGTTC"

sequences = [
    "ATGCGTAC",
    "ATGAGTAC",
    "GGGCGTAC"
]

matches, mismatches, similarity = compare_sequences(dna1, dna2)

