import pandas as pd
# age
df = pd.read_excel("table of age and job of slovak people.xlsx")
df.columns = df.columns.str.strip()
df = df.rename(columns={"abs.": "Pocet"})
# only non-empty
age = df[
    (df["Kód obce"] != "") &
    (df["Názov obce"] != "") &
    (df["Vekové skupiny"] != "") &
    (df["Pocet"] != "")
]
# sum of vekove skupiny rows
age_group = age.groupby(["Kód obce", "Názov obce", "Vekové skupiny"], as_index=False)["Pocet"].sum()
age_group_sorted = age_group.sort_values(by="Pocet", ascending=False)
first_per_obec = age_group_sorted.groupby(["Kód obce", "Názov obce"]).first().reset_index()
final = first_per_obec.rename(columns={"Vekové skupiny": "Najčastejšia veková skupina"})

# delete column pocet
final = final.loc[:, ["Kód obce", "Názov obce", "Najčastejšia veková skupina"]]
final.to_excel("najcastejsia_vekova_skupina_obce.xlsx", index=False)


# job
job = df[
    (df["Kód obce"] != "") &
    (df["Názov obce"] != "") &
    (df["Postavenie v zamestnaní"] != "") &
    (df["Pocet"] != "")
]

job_group = job.groupby(["Kód obce", "Názov obce", "Postavenie v zamestnaní"], as_index=False)["Pocet"].sum()
job_group_sorted = job_group.sort_values(by="Pocet", ascending=False)
first_per_obec = job_group_sorted.groupby(["Kód obce", "Názov obce"]).first().reset_index()
final = first_per_obec.rename(columns={"Postavenie v zamestnaní": "Najčastejšia skupina zamestnania"})
final = final.loc[:, ["Kód obce", "Názov obce", "Najčastejšia skupina zamestnania"]]

final.to_excel("najcastejsia_skupina_zamestnavania_obce.xlsx", index=False)


# titul
df = pd.read_excel("table of titul of slovak people.xlsx")
df.columns = df.columns.str.strip()
df = df.rename(columns={"abs.": "Pocet"})

titul = df[
    (df["Kód obce"] != "") &
    (df["Názov obce"] != "") &
    (df["Vzdelanie"] != "") &
    (df["Pocet"] != "")
]

titul_group = titul.groupby(["Kód obce", "Názov obce", "Vzdelanie"], as_index=False)["Pocet"].sum()
titul_group_sorted = titul_group.sort_values(by="Pocet", ascending=False)
first_per_obec = titul_group_sorted.groupby(["Kód obce", "Názov obce"]).first().reset_index()
final = first_per_obec.rename(columns={"Vzdelanie": "Najčastejšie vzdelanie"})
final = final.loc[:, ["Kód obce", "Názov obce", "Najčastejšie vzdelanie"]]

final.to_excel("najcastejsie_vzdelanie_obce.xlsx", index=False)






