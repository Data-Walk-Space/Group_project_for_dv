import pandas as pd

education_df = pd.read_excel("output_education_final.xlsx")
job_df = pd.read_excel("output_job_final.xlsx")

education_df['education_info_missing'] = education_df[['Titul']].isnull().all(axis=1)
education_missing_df = education_df[education_df['education_info_missing']].drop(columns=['education_info_missing'])
job_df_reduced = job_df[['Meno', 'Priezvisko', 'Zamestnanie']]

merged_df = pd.merge(
    education_missing_df,
    job_df_reduced,
    on=['Meno', 'Priezvisko'],
    how='left'
)

merged_df.to_excel("merged_by_name_and_surname.xlsx", index=False)
print("✅ Файл успешно сохранён: 'merged_by_name_and_surname.xlsx'")




polit_df = pd.read_excel("output_polit_part_final.xlsx")
polit_df_reduced = polit_df[['Meno', 'Priezvisko', 'Politický subjekt']]

merged_df = pd.merge(
    education_missing_df,
    polit_df_reduced,
    on=['Meno', 'Priezvisko'],
    how='left'
)

merged_df.to_excel("merged_by_name_and_surname_polit_and_titul.xlsx", index=False)
print("✅ Файл успешно сохранён: 'merged_by_name_and_surname_polit_and_titul.xlsx'")


import pandas as pd
import matplotlib.pyplot as plt

merged_df = pd.read_excel("merged_by_name_and_surname.xlsx")

merged_df['is_starosta'] = merged_df['Zamestnanie'].fillna('').str.contains('starosta', case=False, na=False)
starosta_count = merged_df['is_starosta'].sum()
other_count = len(merged_df) - starosta_count

labels = ['Starosta', 'Iné']
sizes = [starosta_count, other_count]
colors = ['#ffcc00', '#9999ff']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Koľko ľudí bez vyššieho vzdelania bolo starostami?') # круглая диаграмма
plt.legend()
plt.savefig("Koľko ľudí bez vyššieho vzdelania bolo starostami.png")
plt.show()






merged_df = pd.read_excel("merged_by_name_and_surname_polit_and_titul.xlsx")

merged_df['is_neka'] = merged_df['Politický subjekt'].fillna('').str.contains('NEKA', case=False, na=False)
starosta_count = merged_df['is_neka'].sum()
other_count = len(merged_df) - starosta_count

labels = ['NEKA', 'Iné']
sizes = [starosta_count, other_count]
colors = ['#ffcc00', '#9999ff']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Koľko ľudí bez vyššieho vzdelania bolo považovaných\nza nezávislých kandidátov?') # круглая диаграмма
plt.legend()
plt.savefig("Koľko ľudí bez akéhokoľvek vzdelania bolo považovaných za nezávislých kandidátov.png")
plt.show()





