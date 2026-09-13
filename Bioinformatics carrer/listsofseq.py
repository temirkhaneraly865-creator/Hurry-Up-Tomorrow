sequences = ["ATGCGTAC", "GGCTAACG", "TTAGCGTA", "ATATATGC"]

for dna in sequences:
  print(f"Dna: {dna}")
  print(f"length: {len(dna)}")
  print(f"A: {dna.count("A")}")
  print(f"T: {dna.count("T")}")
  print(f"G: {dna.count("G")}")
  print(f"C: {dna.count("C")}")