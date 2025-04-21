import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('pp.csv')

df.set_index('Politický subjekt', inplace=True)

colors = ["#2E0854", "#FFA500"]
cmap = sns.color_palette(colors)

plt.figure(figsize=(15, 8))

heatmap = sns.heatmap(
    df,
    cmap=cmap,
    annot=False,
    linewidths=0.5,
    cbar=False
)

plt.title("Politicke subjekty | yellow - 1, violet - 0", fontsize=14, pad=20)
plt.xticks(rotation=45, ha='right', fontsize=7)
plt.yticks(fontsize=10)
plt.tight_layout()

plt.savefig(
    "political_heatmap.png", 
    dpi=300,                 
    bbox_inches='tight',     
    transparent=False       
)

plt.show()