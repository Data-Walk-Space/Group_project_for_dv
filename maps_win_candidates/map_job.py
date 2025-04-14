import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

geojson_path = "slovakia.json"
gdf = gpd.read_file(geojson_path)

excel_path = "output_job.xlsx"
df = pd.read_excel(excel_path)
df = df.iloc[:, [7,9]]

gdf['code'] = gdf['code'].astype(str).str[-6:].astype(int)
gdf = gdf.rename(columns={'code': "district code"})

df = df.rename(columns={"Kód obce": "district code", "Zamestnanie": "job"})
df['district code'] = df['district code'].astype(int)

def categorize_job(job):
    job = job.lower()
    # Administrative/Government positions
    if 'starost' in job or 'primátor' in job:
        return 'Municipal Leader'
    # Education
    elif any(term in job for term in ['učiteľ', 'pedagóg', 'vychovávateľ', 'riaditeľ škol']):
        return 'Education'
    # Business/Management
    elif any(term in job for term in ['manažér', 'riaditeľ', 'podnikateľ', 'konateľ']):
        return 'Business/Management'
    # Technical
    elif any(term in job for term in ['technik', 'inžinier', 'informatik']):
        return 'Technical'
    # Finance/Economy
    elif any(term in job for term in ['ekonóm', 'účtovn', 'finančn']):
        return 'Finance/Economy'
    # Public Service
    elif any(term in job for term in ['policajt', 'hasič', 'štátny zamestnan']):
        return 'Public Service'
    # Other
    else:
        return 'Other'

df['job'] = df['job'].apply(categorize_job)

new = gdf.merge(df, left_on="district code", right_on="district code", how="left")

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
new.plot(column="job", cmap='viridis', legend=True, linewidth=0.3, ax=ax)

ax.set_title("Slovakia Districts by Occupation Level", fontsize=14)
ax.axis("off")

plt.savefig("slovakia_occupation_map.png", dpi=300, bbox_inches="tight")
plt.show()


