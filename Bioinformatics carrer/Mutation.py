sequences = ["ATGCGTAC", "GGCTAACG", "TTAGCGTA"]
backup = sequences.copy()
if "ATGCGTAC" in sequences:
  print("ATGCGTAC is here!")

sequences.append("ATGAGTAC")
sequences.remove("GGCTAACG")
sequences.sort()
print(f"original: {backup}")
print(f"modified: {sequences}")