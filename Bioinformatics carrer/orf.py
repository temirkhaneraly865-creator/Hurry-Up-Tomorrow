dna = "CCCATGCGTTAA"

orf = []
started = False

for i in range(0, len(dna), 3):
  codon = dna[i:i+3]

  if codon == "ATG":
    started = True

  if started:
    orf.append(codon)

  if codon in ["TAA", "TAG", "TGA"]:
    break

print("ORF:", "-".join(orf))