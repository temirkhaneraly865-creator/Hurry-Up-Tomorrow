def analyze_fasta(fasta):
  lines = fasta.splitlines()
  for line in lines:
    if line.startswith(">"):
      print("Gene:", line)
    else:
      print("DNA:", line)
      print(f"length: {len(line)}")
      print(f"A: {line.count('A')}")
      print(f"T: {line.count('T')}")
      print(f"G: {line.count('G')}")
      print(f"C: {line.count('C')}")
      print(f"Start ATG: {line.find("ATG")}")
      


fasta = """>BRCA1
ATGGCCATTGTA
>TP53
CCATGGG
>MYC
ATGCGTAC
>EGFR
GGGATCCGTA"""
analyze_fasta(fasta)