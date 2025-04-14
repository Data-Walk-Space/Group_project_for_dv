import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

geojson_path = "slovakia.json"
gdf = gpd.read_file(geojson_path)


excel_path = "output_age.xlsx"
df = pd.read_excel(excel_path)
df = df.iloc[:, [7,10]]

df = df.rename(columns={"Kód obce": "district code", "Edu": "age"})
gdf['code'] = gdf['code'].astype(str).str[-6:].astype(int)
gdf = gdf.rename(columns={'code': "district code"})
df['district code'] = df['district code'].astype(int)
new = gdf.merge(df, left_on="district code", right_on="district code", how="left")

age_bins = [0, 30, 40, 50, 60, 70, 100]
age_labels = ["<30", "30-40", "40-50", "50-60", "60-70",  "70+"]

new["age_group"] = pd.cut(new["age"], bins=age_bins, labels=age_labels)

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
new.plot(column="age_group", cmap = 'coolwarm', legend=True, linewidth=0.3, ax=ax)


ax.set_title("Slovakia Districts by Age Group", fontsize=14)
ax.axis("off")

plt.savefig("slovakia_age_map.png", dpi=300, bbox_inches="tight")
plt.show()
