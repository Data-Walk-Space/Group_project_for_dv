import pandas as pd
path_all = r'/Users/xkrasnah/Downloads/all_candidates.xlsx'
path_won = (r'/Users/xkrasnah/Downloads/won_candidates.xlsx')

all = pd.read_excel(path_all)
won = pd.read_excel(path_won)
new = won.merge(all, on=['Priezvisko','Kód kraja', 'Názov kraja', 'Kód územného obvodu', 'Kód okresu', 'Názov okresu',
                'Kód obce', 'Názov obce', 'Meno', 'Politický subjekt'] ,how='left')

new_age = new.iloc[:, [1,3,5,7,14]]
print(new_age.max())
print(new_age.min())
age_20_30 = len(new_age[(new_age['Vek'] >= 20) & (new_age['Vek'] < 30)])
age_30_40 = len(new_age[(new_age['Vek'] >= 30) & (new_age['Vek'] < 40)])
age_40_50 = len(new_age[(new_age['Vek'] >= 40) & (new_age['Vek'] < 50)])
age_50_60 = len(new_age[(new_age['Vek'] >= 50)& (new_age['Vek'] < 60)])
age_60_70 = len(new_age[(new_age['Vek'] >= 60) & (new_age['Vek'] < 70)])
age_70_80 = len(new_age[(new_age['Vek'] >= 70) & (new_age['Vek'] < 80)])
print(age_20_30,age_30_40,age_40_50,age_50_60,age_60_70,age_70_80, new_age.size)
# new_age.to_excel("output_age.xlsx")

new_education = new.iloc[:, [0,1,2,3,4,5,6,7,13]]
category_counts = new_education['Titul'].value_counts()
filtered_counts = category_counts[category_counts > 1]
print(filtered_counts)
# print(new_education.groupby('Titul').size())

new_party = new.iloc[:, [0,1,2,3,4,5,6,7,10]]
category_counts = new_party['Politický subjekt'].value_counts()
filtered_counts = category_counts[category_counts > 2]
print(filtered_counts)
# print(new_party.groupby('Politický subjekt').size())
#
# new_education.to_excel("output_education.xlsx")
new_job = new.iloc[:, [0,1,2,3,4,5,6,7,15]]

new_job.loc[new_job['Zamestnanie'] == 'starosta obce', 'Zamestnanie'] = 'starosta'
new_job.loc[new_job['Zamestnanie'] == 'starostka', 'Zamestnanie'] = 'starosta'
new_job.loc[new_job['Zamestnanie'] == 'starostka obce', 'Zamestnanie'] = 'starosta'
new_job.loc[new_job['Zamestnanie'] == 'primátor mesta', 'Zamestnanie'] = 'primátor'
new_job.loc[new_job['Zamestnanie'] == 'nezamestnaná', 'Zamestnanie'] = 'nezamestnaný'
new_job.loc[new_job['Zamestnanie'] == 'učiteľka', 'Zamestnanie'] = 'učiteľ'

category_counts = new_job['Zamestnanie'].value_counts()
filtered_counts = category_counts[category_counts > 3]
print(filtered_counts)


# new_job = new_job.rename({"živnostníčka": "Pete","živnostník"
# new_job.to_excel("output_job.xlsx")

