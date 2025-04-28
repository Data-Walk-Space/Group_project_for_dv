import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

df = pd.read_csv('fw.csv', index_col=0)

df_numeric = df.applymap(lambda x: 1 if str(x).strip().lower() == 'yes' else 0).astype(float)

cmap = ListedColormap(['#C60000', 'green'])

plt.figure(figsize=(12, max(6, df_numeric.shape[0] * 0.3)))
sns.heatmap(df_numeric, cmap=cmap, linewidths=0.5, cbar=False, xticklabels=True, yticklabels=True)


plt.xticks(rotation=0, ha='right')
plt.yticks(rotation=0)
plt.title('Does factories from 1990\'s work nowdays? (yes = green, no = dark red)')
plt.tight_layout()
plt.show()
