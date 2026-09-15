rna = "AUGGCUUUUGAAGGU"
codon_table = {"AUG": "Methionine", "GCU": "Alanine", "UUU": "Phenylalanine", "GAA": "Glutamic acid", "GGU": "Glycine"}
for i in range(0, len(rna), 3):
  codon = rna[i:i+3]
  amino_acid = codon_table[codon]
  print(codon, "→", amino_acid)