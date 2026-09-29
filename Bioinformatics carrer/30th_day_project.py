reference = "ATGCGTAC"

samples = [
    "ATGCGTAC",
    "ATGAGTAC",
    "GGGCGTAC",
    "ATGCGTAA"
]


def gc_content(dna):
    gc = dna.count("G") + dna.count("C")
    return round(gc / len(dna) * 100, 2)


def calculate_identity(dna1, dna2):
    matches = 0

    for base1, base2 in zip(dna1, dna2):
        if base1 == base2:
            matches += 1

    return round(matches / len(dna1) * 100, 2)


def find_mutations(reference, dna):
    mutations = []

    for i, (base1, base2) in enumerate(zip(reference, dna)):
        if base1 != base2:
            mutations.append((i, base1, base2))

    return mutations


def find_motif(dna, motif):
    return dna.find(motif)


best_identity = 0
best_sample = ""

highest_gc = 0
highest_gc_sequence = ""

for dna in samples:

    length = len(dna)
    gc = gc_content(dna)
    identity = calculate_identity(reference, dna)
    mutations = find_mutations(reference, dna)
    atg_position = find_motif(dna, "ATG")

    print("Sequence:", dna)
    print("Length:", length)
    print("GC%:", gc)
    print("Identity:", identity)
    print("Mutations:", mutations)
    print("Mutation count:", len(mutations))
    print("ATG position:", atg_position)
    print("----------------")

    if identity > best_identity:
        best_identity = identity
        best_sample = dna

    if gc > highest_gc:
        highest_gc = gc
        highest_gc_sequence = dna


print("=== SUMMARY ===")
print("Best Identity:", best_identity)
print("Best Sample:", best_sample)
print("Highest GC:", highest_gc)
print("Highest GC Sequence:", highest_gc_sequence)
print("Total Samples:", len(samples))


  




  
