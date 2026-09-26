sequences = ["ATGCGTAC","GGGCCC","ATATAT","CGCGCG", "ATGCATGC"]

def gc_content(dna):
  g = dna.count("G")
  c = dna.count("C")
  gc_percent = (g + c) / len(dna) * 100
  return round(gc_percent, 2)


for dna in sequences:
  length = len(dna)
  gc = gc_content(dna)

  a = dna.count("A")
  t = dna.count("T")
  c = dna.count("C")
  g = dna.count("G")
  print("Sequence:", dna)
  print("Length:", length)
  print("GC%:", gc)
  print("A:", a)
  print("T:", t)
  print("C:", c)
  print("G:", g)
  print("---------")

gc_values = []
for dna in sequences:
  gc = gc_content(dna)
  gc_values.append(gc)

print("Highest GC:", max(gc_values))
print("Lowest GC:", min(gc_values))
print("Average GC:", sum(gc_values) / len(gc_values))



