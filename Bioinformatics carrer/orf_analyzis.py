sequences = [
    "CCCATGAAAGGGTAA",
    "GGGATGCCCTGA",
    "ATATAT",
    "CCCATGCGTTAG",
    "ATGAAATGA"
]


def find_orf(dna):
    start = dna.find("ATG")
    stop = dna.find("TAA")

    if start == -1 or stop == -1:
        return None

    if stop < start:
        return None

    return dna[start:stop + 3]


total_sequences = len(sequences)
orf_count = 0

longest_orf = ""
longest_length = 0


for dna in sequences:

    start = dna.find("ATG")
    stop = dna.find("TAA")
    orf = find_orf(dna)

    print("Sequence:", dna)
    print("DNA length:", len(dna))
    print("Start position:", start)
    print("Stop position:", stop)

    if orf is not None:

        print("ORF:", orf)
        print("ORF length:", len(orf))
        print("G count:", orf.count("G"))
        print("C count:", orf.count("C"))

        orf_count += 1

        if len(orf) > longest_length:
            longest_length = len(orf)
            longest_orf = orf

    else:
        print("ORF: None")

    print("----------------")


print("=== SUMMARY ===")
print("Total sequences:", total_sequences)
print("Sequences with ORF:", orf_count)
print("Longest ORF:", longest_orf)
print("Longest ORF length:", longest_length)


  




  
