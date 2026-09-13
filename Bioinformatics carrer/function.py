def validate_dna(dna):
  valid = True
    
  for base in dna:
    if base not in "AGTC":
      valid = False
    
  return valid

def dna_length(dna):
  return len(dna)

def nucleotides_count(dna):
  a = dna.count("A")
  t = dna.count("T")
  g = dna.count("G")
  c = dna.count("C")
  return a, t, g, c

dna = "ATGCGCGTAC"
print(f"valid: {validate_dna(dna)}")
print(f"length: {dna_length(dna)}")
a, t, g, c = nucleotides_count(dna)
print(f"A: {a}")
print(f"T: {t}")
print(f"G: {g}")
print(f"C: {c}")
