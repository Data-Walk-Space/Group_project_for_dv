import pandas as pd
import geopandas as gpd
import plotly.express as px
import re
import json

def normalize_name(name):
    if pd.isna(name):
        return name
    return re.sub(r'\s*-\s*.+', '', str(name)).strip()

def load_geodata():
    regions = gpd.read_file("slovakia.json", layer="obce")
    
    regions['norm_name'] = regions['name'].apply(normalize_name)
    
    regions = regions.set_crs("EPSG:5514", allow_override=True).to_crs(epsg=4326)
    return regions

def load_candidates(file_paths):
    
    base_cols = ['Kód obce', 'Názov obce', 'Meno', 'Priezvisko']
    additional_cols = ['Politický subjekt', 'Titul', 'Zamestnanie']
    
    dfs = []
    for f in file_paths:
        df = pd.read_excel(f)
        
        if 'Názov obce' not in df.columns:
            continue
        
        df['norm_name'] = df['Názov obce'].apply(normalize_name)
        
        for col in additional_cols:
            if col not in df.columns:
                df[col] = None
       
        df['candidate_key'] = df[base_cols].astype(str).agg('_'.join, axis=1)
        df = df.set_index('candidate_key')
        
        dfs.append(df)
    
    if not dfs:
        return pd.DataFrame()
   
    merged_candidates = dfs[0]
    for df in dfs[1:]:
        merged_candidates = merged_candidates.combine_first(df)
    
    merged_candidates = merged_candidates.reset_index(drop=True)
 
    merged_candidates = merged_candidates.drop_duplicates(subset=base_cols)
    
    for col in additional_cols:
        merged_candidates[col] = merged_candidates[col].fillna('-')
    
    return merged_candidates

def create_map(merged_data):

    merged_data['Politický subjekt'] = merged_data['Politický subjekt'].fillna('Neurčená strana')
    
    for col in ['Meno', 'Priezvisko', 'Vek', 'Názov obce', 'Titul', 'Zamestnanie']:
        if col in merged_data.columns:
            merged_data[col] = merged_data[col].fillna('-')
    
    valid_data = merged_data[~merged_data.geometry.is_empty].copy()
    
    valid_data['id'] = valid_data.index.astype(str)
      
    valid_data["geometry"] = valid_data["geometry"].simplify(
        tolerance=0.1, 
        preserve_topology=True
        )
    
    valid_data["geometry"] = valid_data["geometry"].buffer(0)


    geojson_obj = json.loads(valid_data.to_json())
    
    fig = px.choropleth(
        valid_data,
        geojson=geojson_obj,
        locations='id',               
        featureidkey='properties.id',
        color='Politický subjekt',
        hover_name='norm_name',
        hover_data={
            'Meno': True,
            'Priezvisko': True,
            'Vek': True,
            'Politický subjekt': True,
            'Titul': True,
            'Zamestnanie': True
        },
        color_discrete_map={'Neurčená strana': 'lightgray'},
        color_discrete_sequence=px.colors.qualitative.Vivid,
        title='Kandidáti podľa obcí'
    )
    
    fig.update_geos(
        fitbounds='locations',
        visible=False
    )
    
    fig.update_layout(
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        legend_title_text='Politické strany'
    )
    
    return fig

def main():
    file_paths = [
        'output_age_final (1).xlsx',
        'output_polit_part_final.xlsx',
        'output_job_final.xlsx',
        'output_education_final.xlsx'
    ]
 
    regions = load_geodata()
    candidates = load_candidates(file_paths)
 
    merged = regions.merge(
        candidates,
        on='norm_name',
        how='left'
    )

    print("Успешно сопоставлено:", merged[~merged['Kód obce'].isna()].shape[0])
    print("Пример данных:", merged[['name', 'Názov obce', 'Meno', 'Politický subjekt', 'Titul', 'Zamestnanie']])

    fig = create_map(merged)
    #fig.write_html("final_map.html")
    fig.show()

if __name__ == "__main__":
    main()
