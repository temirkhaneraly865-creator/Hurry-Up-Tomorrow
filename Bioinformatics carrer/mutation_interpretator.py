sample = "ATGAGTAC"
reference= "ATGCGTAC"

def find_mutations(reference, sample):
  mutations = []

  for i, (base1, base2) in enumerate(zip(reference, sample)):
    if base1 != base2:
      mutations.append((i, base1, base2))

  return mutations

mutations = find_mutations(reference, sample)

for position, base1, base2 in mutations:
  print("Position:", position)
  print("Reference:", base1)
  print("Sample:", base2)


  




  
