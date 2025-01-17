import pandas as pd

#Load CSV file
df = pd.read_csv("Data/percentageRenewableElectricity-Irl.csv")

#Delete irrelevant columns
df_filtered = df.drop(columns=["STATISTIC", "Statistic Label", "Month", "Time Bands"])

#Extracting the date from the colum which is in format YYYYMM
df_filtered["Year"] = df_filtered["TLIST(M1)"].astype(str).str[:4].astype(int)

#Calculate mean for each year
clean = df_filtered.groupby("Year")["VALUE"].agg(["mean"]).reset_index()

#Make new column names
clean.columns = ["Year", "Mean"]

#Show result
clean.to_csv("/Users/ciura/Documents/Project/Data/percentageRenewableElectricityFiltered-Irl.csv", index=False)