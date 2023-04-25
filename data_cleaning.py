import pandas as pd 
import csv
df = pd.read_csv("merged_dataset.csv")
print(df.shape)

del df["Luminosity"]
del df[""]