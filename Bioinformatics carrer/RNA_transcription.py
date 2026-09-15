def validate_dna(dna):
  valid = True
    
  for base in dna:
    if base not in "ATGC":
      valid = False

  return valid

def transcribe_dna(dna):
  dna = dna.upper()
  rna = dna.replace("T", "U")
  return rna

sequences = ["ATGCXTAC", "GGCTAACG", "TTAGCGTA", "ATATATGC"]
for dna in sequences:
  if validate_dna(dna):
    print(f"DNA: {dna}")
    rna = transcribe_dna(dna)
    print(f"RNA: {rna}")
    print(f"DNA length: {len(dna)}")
    print(f"RNA length: {len(rna)}\t\n")
  else:
    print(f"Dna: {dna}")
    print("Rna: Cannot Transcribed")
  
  