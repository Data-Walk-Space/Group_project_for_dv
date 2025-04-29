import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

pop = pd.read_excel('all_pop_obce.xlsx')

pop.rename(columns={'Kód': 'code'}, inplace=True)

map_sl = gpd.read_file('slovakia.json')
pop_merge = map_sl.merge(pop, on='code')

fig1, ax1 = plt.subplots(figsize=(16, 8))
pop_merge.plot(column='Spolu', legend=True, cmap='plasma', ax=ax1)
ax1.axis('off')
ax1.set_title('Počet obyvateľov')
plt.savefig('all_popul_sl.png')
plt.show()