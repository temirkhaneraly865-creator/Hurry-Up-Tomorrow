sequences = ["CCCATGAAAGGGTAA","ATGCGTAC","GGGATGCCCTGA","ATATAT"]
stop_codons = ["TAA", "TGA", "TAG"]

for dna in sequences:
  print("Sequence:", dna)
  print("=============")
  
  for frame in range(3):
    sequence = dna[frame:]
    codons = []
    
    for i in range(0, len(sequence) - 2, 3):
      codon = sequence[i:i+3]
      codons.append(codon)
      
    print("Frame:", frame)
    print("Codons:", codons)

    start_found = False
    stop_found = False

    for codon in codons:
      if codon == "ATG":
        start_found = True

      if codon in stop_codons:
        stop_found = True
        
    print("Start:", start_found)
    print("Stop:", stop_found)
    print("-------------")
    
  print()
