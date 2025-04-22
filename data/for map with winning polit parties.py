import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

gdf = gpd.read_file("slovakia.json", layer="obce")

df = pd.read_excel("output_polit_part_final.xlsx")
df = df[["Kód obce", "Politický subjekt"]]
df = df.rename(columns={"Kód obce": "district code", "Politický subjekt": "party"})

def simplify_party(name):
    name = str(name).lower()
    if "hlas" in name:
        return "Hlas"
    elif "smer" in name:
        return "SMER"
    elif "progresívne" in name:
        return "Progresívne Slovensko"
    elif "kdh" in name:
        return "KDH"
    elif "sas" in name:
        return "SaS"
    elif "nase slovensko" in name or "lsns" in name:
        return "ĽSNS"
    elif "repub" in name:
        return "REPUBLIKA"
    elif "team" in name:
        return "Team"
    elif "sns" in name:
        return "SNS"
    elif "modrí" in name:
        return "MODRÍ"
    elif "aliancia" in name:
        return "Aliancia"
    elif "nka" in name or "neka" in name:
        return "NEKA"
    else:
        return name.split(",")[0].strip().title()

df["party_simple"] = df["party"].apply(simplify_party)
df = df.drop_duplicates(subset="district code")

#Preparing codes in geodata
gdf["code"] = gdf["code"].astype(str).str[-6:].astype(int)
gdf = gdf.rename(columns={"code": "district code"})
df["district code"] = df["district code"].astype(int)

merged = gdf.merge(df, on="district code", how="left")

#Assignment of colors
unique_parties = merged["party_simple"].dropna().unique()
cmap = plt.get_cmap("tab20", len(unique_parties))
colors = {party: cmap(i) for i, party in enumerate(unique_parties)}

merged["color"] = merged["party_simple"].map(colors)
merged["color"] = merged["color"].fillna("#cccccc")  # grey for None

#Map visualization
fig, ax = plt.subplots(1, 1, figsize=(18, 10))
merged.plot(color=merged["color"], linewidth=0.2, ax=ax)

#Creating a legend on the side
legend_elements = [Line2D([0], [0], marker='o', color='w', label=party,
                          markerfacecolor=colors[party], markersize=10)
                   for party in sorted(unique_parties)]

ax.legend(handles=legend_elements, title="Political Parties",
          loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, title_fontsize=12)

ax.set_title("Slovakia Districts by Dominant Political Party", fontsize=16)
ax.axis("off")

plt.subplots_adjust(right=0.78)  # expand the space on the right
plt.savefig("slovakia_map_political_parties.png", dpi=300, bbox_inches="tight")
plt.show()






