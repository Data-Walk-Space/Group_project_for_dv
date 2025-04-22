import pandas as pd
import matplotlib.pyplot as plt


file_path = "Students_Studying_Abroad_OECD_2022_2020.xlsx"
df = pd.read_excel(file_path)


plt.figure(figsize=(12, 6))
plt.bar(df["Country"], df["2020 (%)"], color='lightblue')
plt.xticks(rotation=90)
plt.title("Share of Students Studying Abroad in 2020 (%)")
plt.ylabel("Percentage (%)")
plt.tight_layout()
plt.savefig("slovak_students_abroad_2020.png")
plt.show()


plt.figure(figsize=(12, 6))
plt.bar(df["Country"], df["2022 (%)"], color='coral')
plt.xticks(rotation=90)
plt.title("Share of Students Studying Abroad in 2022 (%)")
plt.ylabel("Percentage (%)")
plt.tight_layout()
plt.savefig("slovak_students_abroad_2022.png")
plt.show()
