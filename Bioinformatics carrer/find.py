

sequences = ["CCCATGCGTTAA","GGGATGCCCTGA","ATATAT","TTCCCGGG","ATGCGTAG"]

for dna in sequences:
  print("Sequence:", dna)
  print("Length:", len(dna))
  print("ATG:", dna.find("ATG"))
  print("TAA:", dna.find("TAA"))
  print("TGA:", dna.find("TGA"))
  print("TAG:", dna.find("TAG"))
  if "ATG" in dna:
    print("START CODON FOUND")
  else:
    print("No Start Codon")
    
  print("--------")
  
