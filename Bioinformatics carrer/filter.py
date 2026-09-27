sequences = ["ATGCGTAC", "CCCATGGG", "ATATAT", "GGGCGCTA", "TTATGCGA", "CGCGCG"]


def gc_content(dna):
    gc = dna.count("G") + dna.count("C")
    return round(gc / len(dna) * 100, 2)


for dna in sequences:

    if len(dna) < 6:
        continue

    if "ATG" not in dna:
        continue

    gc = gc_content(dna)

    if gc <= 50:
        continue

    print("Sequence:", dna)
    print("Length:", len(dna))
    print("GC%:", gc)
    print("-------")



