import pandas as pd
import matplotlib.pyplot as plt
path_all = (r'all_candidates.xlsx')
path_won = (r'won_candidates.xlsx')

def others(counts, top_n=5, label='Iné'):
    top = counts.nlargest(top_n)
    other = counts.sum() - top.sum()
    if other > 0:
        top[label] = other
    return top

def procent(threshold=4):
    def inner_autopct(pct):
        return f'{pct:.1f}%' if pct >= threshold else ''
    return inner_autopct


all = pd.read_excel(path_all, header=2)
won = pd.read_excel(path_won, header=2)
new = won.merge(all, on=['Priezvisko','Kód kraja', 'Názov kraja', 'Kód územného obvodu', 'Kód okresu', 'Názov okresu',
                'Kód obce', 'Názov obce', 'Meno', 'Politický subjekt'] ,how='left')

fig, axs = plt.subplots(2, 2, figsize=(18, 10))
fig.suptitle("Analýza víťazov podľa veku, titulu, zamestnania a strany", fontsize=20)

new_age = new.iloc[2:, [1,3,5,7,14]]
print(new_age.max())
print(new_age.min())
age_20_30 = len(new_age[(new_age['Vek'] >= 20) & (new_age['Vek'] < 30)])
age_30_40 = len(new_age[(new_age['Vek'] >= 30) & (new_age['Vek'] < 40)])
age_40_50 = len(new_age[(new_age['Vek'] >= 40) & (new_age['Vek'] < 50)])
age_50_60 = len(new_age[(new_age['Vek'] >= 50) & (new_age['Vek'] < 60)])
age_60_70 = len(new_age[(new_age['Vek'] >= 60) & (new_age['Vek'] < 70)])
age_70_80 = len(new_age[(new_age['Vek'] >= 70) & (new_age['Vek'] < 80)])

ages = {
    '20–30': age_20_30,
    '30–40': age_30_40,
    '40–50': age_40_50,
    '50–60': age_50_60,
    '60–70': age_60_70,
    '70–80': age_70_80
}
axs[0, 0].pie(x = ages.values(), autopct=procent(4))
axs[0, 0].set_title('Vek')
axs[0, 0].legend(ages.keys(), title="Vek", bbox_to_anchor=(1.1, 0.9))

new_education = new.iloc[:, [0,1,2,3,4,5,6,7,13]]
category_counts = new_education['Titul'].value_counts()
#filtered_counts = category_counts[category_counts > 1]

filtered_counts = others(category_counts, 7)
axs[0, 1].pie(x = filtered_counts, autopct=procent(7))
axs[0, 1].set_title('Titul')
axs[0, 1].legend(filtered_counts.index, title="Titul", bbox_to_anchor=(1.1, 0.9))


new_party = new.iloc[:, [0,1,2,3,4,5,6,7,10]]
new_party.loc[new_party['Politický subjekt'] == 'Hlas - sociálna demokracia, SMER - SD', 'Politický subjekt'] = 'SMER - SD, Hlas - sociálna demokracia'
new_party['Politický subjekt'] = new_party['Politický subjekt'].str.upper()
category_counts = new_party['Politický subjekt'].value_counts()
#filtered_counts = category_counts[category_counts > 2]
#print(filtered_counts)


filtered_counts = others(category_counts, 9)
axs[1, 0].pie(x = filtered_counts, autopct=procent(5))
axs[1, 0].set_title('Politický subjekt')
axs[1, 0].legend(filtered_counts.index, title="Politický subjekt", bbox_to_anchor=(1.0, 0.9))


new_job = new.iloc[:, [0,1,2,3,4,5,6,7,15]]

new_job.loc[new_job['Zamestnanie'] == 'starosta obce', 'Zamestnanie'] = 'starosta'
new_job.loc[new_job['Zamestnanie'] == 'starostka', 'Zamestnanie'] = 'starosta'
new_job.loc[new_job['Zamestnanie'] == 'starostka obce', 'Zamestnanie'] = 'starosta'
new_job.loc[new_job['Zamestnanie'] == 'primátor mesta', 'Zamestnanie'] = 'primátor'
new_job.loc[new_job['Zamestnanie'] == 'nezamestnaná', 'Zamestnanie'] = 'nezamestnaný'
new_job.loc[new_job['Zamestnanie'] == 'učiteľka', 'Zamestnanie'] = 'učiteľ'

category_counts = new_job['Zamestnanie'].value_counts()
#filtered_counts = category_counts[category_counts > 3]

filtered_counts = others(category_counts, 7)
axs[1, 1].pie(x = filtered_counts, autopct=procent(4))
axs[1, 1].set_title('Zamestnanie')
axs[1, 1].legend(filtered_counts.index, title="Zamestnanie", bbox_to_anchor=(1.0, 0.9))

plt.savefig('pie_diagram.png')

plt.show()