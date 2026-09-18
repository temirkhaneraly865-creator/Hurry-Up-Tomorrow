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
ATGGCC
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

data = {"Gene": [],
       "Dna": [],
       "Length": [],
       "A": [],
       "T": [],
       "G": [],
       "C": []}

for gene, dna in result.items():
  data["Gene"].append(gene)
  data["Dna"].append(dna)
  data["Length"].append(len(dna))
  data["A"].append(count_base(dna, "A"))
  data["T"].append(count_base(dna, "T"))
  data["G"].append(count_base(dna, "G"))
  data["C"].append(count_base(dna, "C"))

import pandas as pd

df = pd.DataFrame(data)
print(df)



      