reference = "ATGCGTAC"

samples = ["ATGCGTAC","ATGAGTAC", "GGGCGTAC", "ATGCGTAA"]

def gc_content(dna):
  gc = dna.count("G") + dna.count("C")
  gc_percent = gc / len(dna) * 100
  return round(gc_percent, 2)

def calculate_identity(dna1, dna2):
  matches = 0

  for base1, base2 in zip(dna1, dna2):
    if base1 == base2:
      matches += 1

  return round(matches / len(dna1) * 100, 2)

def find_mutations(reference, dna):
  mutations = []

  for i, (base1, base2) in enumerate(zip(reference, dna)):
    if base1 != base2:
      mutations.append((i, base1, base2))

  return mutations

def find_motif(dna, motif):
    return dna.find(motif)

for dna in samples:
  print("Sample:", dna)
  print("Length:", len(dna))
  print("GC%:", gc_content(dna))
  print("Identity:", calculate_identity(reference, dna))
  print("Mutations:", find_mutations(reference, dna))
  print("ATG Position:", find_motif(dna, "ATG"))
  print("-------")



  
