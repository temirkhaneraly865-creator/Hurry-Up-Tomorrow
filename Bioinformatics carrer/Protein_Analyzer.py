def translate_rna(rna):
  codon_table = {"AUG": "M", "GCU": "A", "UUU": "F", "GAA": "E", "GGU": "G"}
  protein = []
  for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    amino_acid = codon_table[codon]
    protein.append(amino_acid)
    
  return "".join(protein)

rna = "AUGGCUUUUGAAGGU"
print(translate_rna(rna))


def analyze_protein(protein):
  print(f"===Protein ANALYZER===")
  print(f"Protein: {protein}")
  print(f"Protein length: {len(protein)}")
  print(f"Uniq Amino_Acids: {len(set(protein))}")
  print(f"M: {protein.count('M')}")
  print(f"A: {protein.count('A')}")
  print(f"F: {protein.count('F')}")
  print(f"E: {protein.count('E')}")
  print(f"G: {protein.count('G')}")
  return 
protein = translate_rna(rna)
analyze_protein(protein)