def compare_sequences(BRCA1, TP53):
  matches = 0
  mismatches = 0

  for base1, base2 in zip(BRCA1, TP53):
    if base1 == base2:
      matches += 1
    else:
      mismatches += 1

  
  similarity = matches / len(BRCA1) * 100

  return matches, mismatches, similarity

BRCA1 = "CTGTCTCAAAACAAAACAAAACAAAACAAAACAAAAAACACCGGCTGGTATGTATGAGAGGATGGGACCT"
TP53 = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC"

matches, mismatches, similarity = compare_sequences(BRCA1, TP53)
print("Ұқсас нуклеотидтер саны:", matches)
print("Үқсас емес нуклеотидтер саны:", mismatches)
print("Ұқсастық пайызы:", similarity)




      