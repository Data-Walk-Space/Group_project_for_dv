import pandas as pd
import matplotlib.pyplot as plt

data_2011 = pd.read_excel("Obyvateľstvo podľa miesta sčítania, pohlavia, veku_2011.xlsx")
data_2021 = pd.read_excel("table of age and job of slovak people.xlsx")

filtered_2011 = data_2011[data_2011['Vek'].str.contains("15") & data_2011['Vek'].str.contains("29")]

presov_2011 = filtered_2011["Prešovský kraj"].sum()
kosice_2011 = filtered_2011["Košický kraj"].sum()
youth_groups = ['15 - 24', '25 - 29']
filtered_2021 = data_2021[data_2021['Vekové skupiny'].isin(youth_groups)]

presov_regions = [
    "Okres Bardejov", "Okres Humenné", "Okres Kežmarok", "Okres Levoča",
    "Okres Medzilaborce", "Okres Poprad", "Okres Prešov", "Okres Sabinov",
    "Okres Snina", "Okres Stará Ľubovňa", "Okres Stropkov", "Okres Svidník",
    "Okres Vranov nad Topľou"
]
kosice_regions = [
    "Okres Gelnica", "Okres Košice I", "Okres Košice II", "Okres Košice III",
    "Okres Košice IV", "Okres Košice-okolie", "Okres Michalovce",
    "Okres Rožňava", "Okres Sobrance", "Okres Spišská Nová Ves",
    "Okres Trebišov"
]

presov_2021 = filtered_2021[filtered_2021['Názov okresu'].isin(presov_regions)]['abs.'].sum()
kosice_2021 = filtered_2021[filtered_2021['Názov okresu'].isin(kosice_regions)]['abs.'].sum()


years = ["2011", "2021"]
x = range(len(years))

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar([i - 0.2 for i in x], [presov_2011, presov_2021], width=0.4, label='Prešovský kraj', color='gold')
ax.bar([i + 0.2 for i in x], [kosice_2011, kosice_2021], width=0.4, label='Košický kraj', color='orangered')
ax.set_ylabel('Počet mladých obyvateľov (15–29 rokov)')
ax.set_title('Zmena počtu mladých v Prešovskom a Košickom kraji (2011–2021)')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig("migration of the young generation of slovakians from eastern slovakia(2011-2021).png")
plt.show()



presov_drop = str(round(100 * (1 - presov_2021 / presov_2011), 1)) + '%'
kosice_drop = str(round(100 * (1 - kosice_2021 / kosice_2011), 1)) + '%'

print('Prešovsky kraj:', '2011:', presov_2011, 'a 2021:', presov_2021, 'strata ->', presov_drop)
print('Košicky kraj:', '2011:', kosice_2011, 'a 2021:', kosice_2021, 'strata ->', kosice_drop)
