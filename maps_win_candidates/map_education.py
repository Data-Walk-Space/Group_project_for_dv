import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

geojson_path = "slovakia.json"
gdf = gpd.read_file(geojson_path)


excel_path = "output_education.xlsx"
df = pd.read_excel(excel_path)
df = df.iloc[:, [7,9]]

gdf['code'] = gdf['code'].astype(str).str[-6:].astype(int)
gdf = gdf.rename(columns={'code': "district code"})

df = df.rename(columns={"Kód obce": "district code", "Titul": "education"})
df['district code'] = df['district code'].astype(int)

def categorize_title(title):
    if pd.isna(title) or title == "":
        return "None"
    # Check highest qualifications first
    elif "PhD." in title or "Ph.D." in title or "DrSc." in title or "CSc." in title or "ArtD." in title:
        return "Doctorate"
    elif "MBA" in title or "LL.M" in title:
        return "Professional"
    elif "MUDr." in title or "MVDr." in title or "PharmDr." in title:
        return "Medical"
    elif "PaedDr." in title or "PhDr." in title or "RNDr." in title:
        return "Other Doctorate"
    elif "prof." in title.lower() or "doc." in title:
        return "Professor/Docent"
    elif "Mgr." in title:
        return "Master"
    elif "Ing." in title:
        return "Engineering"
    elif "JUDr." in title:
        return "Law"
    elif "Bc." in title:
        return "Bachelor"
    else:
        return "Other"

df['education'] = df['education'].apply(categorize_title)

new = gdf.merge(df, left_on="district code", right_on="district code", how="left")

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
new.plot(column="education", cmap='viridis', legend=True, linewidth=0.3, ax=ax)

ax.set_title("Slovakia Districts by Education Level", fontsize=14)
ax.axis("off")

plt.savefig("slovakia_education_map.png", dpi=300, bbox_inches="tight")
plt.show()