def parse_fasta(fasta):
  lines = fasta.splitlines()

  sequences = {}
  current_gene = None
    
  for line in lines:
    if line.startswith(">"):
      current_gene = line.strip(">")
    else:
      sequences[current_gene] = line
    
  
  
  return sequences



fasta = """>BRCA1
ATGGCCATTGTA
>TP53
CCATGGG
>MYC
ATGCGTAC
>EGFR
GGGATCCGTA"""


result = parse_fasta(fasta)

print(result)

def count_base(dna, base):
  return dna.count(base)

def find_start(dna):
  return dna.find("ATG")

for gene, dna in result.items():
  print("Gene:", gene)
  print("DNA:", dna)
  print("Length:", len(dna))
  print("A:", count_base(dna, "A"))
  print("T:", count_base(dna, "T"))
  print("G:", count_base(dna, "G"))
  print("C:", count_base(dna, "C"))
  print("Start ATG:", find_start(dna))
  print("\t\n")