sequences = ["ATGCGTAC", "GGCTAACG", "TTAGCGTA", "ATATATGC"]
for dna in sequences:
  print(f"DNA: {dna}")
  rna = dna.replace("T", "U")
  print(f"RNA: {rna}")
  print(f"RNA length: {len(rna)}")
  print(f"A: {rna.count("A")}")
  print(f"U: {rna.count("A")}")
  print(f"G: {rna.count("A")}")
  print(f"C: {rna.count("A")}")
  print(f"position of G: {rna.find("G")}")
  if rna.startswith("AUG"):
    print("Start codon detected")
  else:
    print("rna has no start codon\t\n")
    
  
  