import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("table of age and job of slovak people.xlsx")
df = pd.DataFrame(data)

age_counts = df['Vekové skupiny'].value_counts().reset_index()
age_counts.columns = ['Veková skupina', 'Pocet']
age_counts['Procent'] = (age_counts['Pocet'] / len(df) * 100).round(1)

age_counts = age_counts.loc[:, ['Veková skupina', 'Procent']]
age_counts = age_counts.sort_values(by='Veková skupina')
age_counts['Veková skupina'] = age_counts['Veková skupina'].replace('60 a viac rokov', '60+')
print(age_counts)

fig, axs = plt.subplots(figsize=(12, 10))
fig.suptitle("Age groups of the Slovak population", fontsize=20)
axs.pie(x = age_counts['Procent'], autopct='%1.1f%%', textprops={'fontsize': 14})
axs.legend(age_counts['Veková skupina'], title="Age groups", title_fontsize=16, bbox_to_anchor=(1, 1.0), fontsize=16)

plt.savefig('pie_diagram_age_groups_population.png')

plt.show()