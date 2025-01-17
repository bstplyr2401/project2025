import pandas as pd

#Read CSV file with ";" as separatoe and also skip rows in not readable format
df = pd.read_csv("Data/percentageRenewableElectricity-Esp.csv", sep=";", skiprows=list(range(6)) + list(range(11, 17)))

#As the file uses European number format with "," to separate decimals I will swap it with "." so file is compatible with Irish format
df = df.map(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)

#Eliminate 3º column
df = df.drop(df.columns[2], axis=1)

#Make new column names
df.columns = ["Year", "Mean"]

#Save as new CSV file
df.to_csv("Data/percentageRenewableElectricityFiltered-Esp.csv", index=False)
