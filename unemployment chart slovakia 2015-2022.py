import pandas as pd
import matplotlib.pyplot as plt

file_path = "Nezamestnanosť_Slovensko_2015_2022.xlsx"
unemployment_data = pd.read_excel(file_path)

plt.figure(figsize=(10, 6))
plt.plot(unemployment_data['Rok'], unemployment_data['Západné Slovensko'], marker='*', label='Západné Slovensko')
plt.plot(unemployment_data['Rok'], unemployment_data['Stredné Slovensko'], marker='*', label='Stredné Slovensko')
plt.plot(unemployment_data['Rok'], unemployment_data['Východné Slovensko'], marker='*', label='Východné Slovensko')
plt.ylabel('%')
plt.xlabel('Rok')
plt.title('Nezamestnanosť na Slovensku (2015–2022)')
plt.grid(True)
plt.legend()
plt.savefig("unemployment chart slovakia 2015-2022.png")
plt.show()



file_path = "Nezamestnanost_mladi_15_29_Slovensko_2015_2022.xlsx"
unemployment_data = pd.read_excel(file_path)

plt.figure(figsize=(10, 6))
plt.plot(unemployment_data['Rok'], unemployment_data['Západné Slovensko'], marker='*', label='Západné Slovensko')
plt.plot(unemployment_data['Rok'], unemployment_data['Stredné Slovensko'], marker='*', label='Stredné Slovensko')
plt.plot(unemployment_data['Rok'], unemployment_data['Východné Slovensko'], marker='*', label='Východné Slovensko')
plt.ylabel('%')
plt.xlabel('Rok')
plt.title('Nezamestnanosť mladých ľudí (15 – 29 rokov) na Slovensku v rokoch 2015 – 2022')
plt.grid(True)
plt.legend()
plt.savefig("chart for unemployment of young people (15-29 years) in slovakia 2015-2022.png")
plt.show()

