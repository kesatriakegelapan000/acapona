import pandas as pd
df = pd.read_excel("kasjanuari.xlsx")

df.to_excel("kasjanuari_cleaned.xlsx", index=False)

df = df.drop(labels = [1,2,3,4,5,6,7,8,9,10,11], axis = 1)

print(df["DAFTAR NAMA"])


