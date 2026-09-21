def calculate_identity(dna1, dna2):
  matches = 0

  for base1, base2 in zip(dna1, dna2):
    if base1 == base2:
      matches += 1

  identity = matches / len(dna1) * 100
  return identity

query = "ATGCGTAC"

subjects = ["ATGCGTAC", "ATGAGTAC", "GGGCGTAC"]

best_identity = 0
best_subject = ""

for dna in subjects:
    identity = calculate_identity(dna, query)

    if identity > best_identity:
        best_identity = identity
        best_subject = dna

print("Best subject:", best_subject)
print("Identity:", best_identity)