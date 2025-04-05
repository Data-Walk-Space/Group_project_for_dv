import pandas as pd
import openpyxl as xl

all = pd.read_excel("all_candidates.xlsx", header=2)
won = pd.read_excel("won_candidates.xlsx", header=2)
all.columns = all.columns.str.strip()
won.columns = won.columns.str.strip()
merge_table = won.merge(
    all,
    on=[
        'Priezvisko', 'Kód kraja', 'Názov kraja', 'Kód územného obvodu',
        'Kód okresu', 'Názov okresu', 'Kód obce', 'Názov obce',
        'Meno', 'Politický subjekt'], how="left")

common_cols = ['Kód kraja', 'Názov kraja', 'Kód územného obvodu',
               'Kód okresu', 'Názov okresu', 'Kód obce', 'Názov obce',
               'Meno', 'Priezvisko']

#from all_candidates fetch 4 last colums
inform_colims = merge_table.columns[-4:]
table_age = merge_table.loc[:, common_cols + [inform_colims[1]]]
table_education = merge_table.loc[:, common_cols + [inform_colims[0]]]
table_job = merge_table.loc[:, common_cols + [inform_colims[2]]]

#not from all_candidates but from merge table from common colums(№10)
table_polit = merge_table.loc[:, common_cols + [merge_table.columns[10]]]

table_age.to_excel("output_age_final.xlsx", index=False)
table_education.to_excel("output_education_final.xlsx", index=False)
table_job.to_excel("output_job_final.xlsx", index=False)
table_polit.to_excel("output_polit_part_final.xlsx", index=False)






