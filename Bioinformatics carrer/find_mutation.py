
def find_mutations(reference, sample):
    mutations = []

    for i, (base1, base2) in enumerate(zip(reference, sample)):
        if base1 != base2:
            mutations.append((i, base1, base2))

    return mutations

reference = "ATGCGTAC"
sample = "ATGAGTAT"

mutations = find_mutations(reference, sample)
print(mutations)