import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

most_ages = pd.read_excel('najcastejsia_vekova_skupina_obce.xlsx')
most_jobs = pd.read_excel('najcastejsia_skupina_zamestnavania_obce.xlsx')
most_title = pd.read_excel('najcastejsie_vzdelanie_obce.xlsx')


most_ages.rename(columns={'Kód obce': 'code'}, inplace=True)
most_jobs.rename(columns={'Kód obce': 'code'}, inplace=True)
most_title.rename(columns={'Kód obce': 'code'}, inplace=True)


map_sl = gpd.read_file('slovakia.json')
map_ages_merge = map_sl.merge(most_ages, on='code')
map_jobs_merge = map_sl.merge(most_jobs, on='code')
map_title_merge = map_sl.merge(most_title, on='code')


fig1, ax1 = plt.subplots(figsize=(16, 8))
map_ages_merge.plot(column='Najčastejšia veková skupina', legend=True, cmap='plasma', ax=ax1)
ax1.axis('off')
ax1.set_title('Najčastejšia veková skupina')
legend = ax1.get_legend()
legend.set_bbox_to_anchor((1.08, 0.5))
legend.set_title("Vekové skupiny")
plt.savefig('map_ages_popul.png')


fig1, ax2 = plt.subplots(figsize=(16, 8))
map_jobs_merge.plot(column='Najčastejšia skupina zamestnania', legend=True, cmap='plasma', ax=ax2)
ax2.axis('off')
ax2.set_title('Najčastejšia skupina zamestnania')
legend = ax2.get_legend()
legend.set_bbox_to_anchor((1.08, 0.2))
legend.set_title("Zamestnanie")
plt.savefig('map_jobs_popul.png')


fig1, ax3 = plt.subplots(figsize=(16, 8))
map_title_merge.plot(column='Najčastejšie vzdelanie', legend=True, cmap='Spectral', ax=ax3)
ax3.axis('off')
ax3.set_title('Najčastejšie vzdelanie')
legend = ax3.get_legend()
legend.set_bbox_to_anchor((1.08, 0.2))
legend.set_title("Vzdelanie")


plt.savefig('map_title_popul.png')
plt.show()


