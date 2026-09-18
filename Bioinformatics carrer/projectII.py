import pandas as pd
import numpy as np

data = {
    "Gene": ["BRCA1", "TP53", "MYC", "EGFR", "PTEN"],
    "Length": [6, 7, 8, 10, 9],
    "GC": [50.0, 57.14, 50.0, 60.0, 55.56],
    "Expression": [12, 35, 48, 27, 19]
}

df = pd.DataFrame(data)

print(df)
print("Average length:", df["Length"].mean())
print("Max Expression:", df["Expression"].max())
print("Min GC:", df["GC"].min())
print("Expression > 25:", df[df["Expression"] > 25])
print("------------------")
lengths = np.array(df["Length"])
print("Length:", lengths)
print("Doubled:", lengths * 2)
print("Mean:", np.mean(lengths))

