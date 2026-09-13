
dna = "AGTCGGTAAC"
print(f"dna sequence: {dna}")
print(f"length of dna: {len(dna)}")
valid = True
for base in dna:
    if base not in "AGTC":
        valid = False
        
if valid:
    print("dna looks valid")
else:
    print("invalid dna\t\ninvalid base detected: X ")
        