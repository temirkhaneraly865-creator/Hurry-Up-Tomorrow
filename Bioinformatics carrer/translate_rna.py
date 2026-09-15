def translate_rna(rna):
  codon_table = {"AUG": "M", "GCU": "A", "UUU": "F", "GAA": "E", "GGU": "G"}
  protein = []
  for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    amino_acid = codon_table[codon]
    protein.append(amino_acid)
    
  return "-".join(protein)

rna = "AUGGCUUUUGAAGGU"
print(translate_rna(rna))

    