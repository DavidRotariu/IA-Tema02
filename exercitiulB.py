import pandas as pd
import seaborn as sns
import numpy as np

# 1. optiuni de afisare pentru pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.float_format', '{:.2f}'.format)


tips = sns.load_dataset('tips')

print(f"Primele 5 înregistrări:")
print(tips.head())

# Dimensiunea
print(f"\nDimensiunea dataset-ului:")
print(f"   - Număr de rânduri (înregistrări): {tips.shape[0]}")
print(f"   - Număr de coloane (variabile): {tips.shape[1]}")
print(f"   - Total celule: {tips.size}")

# Tipurile
print(f"\nTipurile de date pentru fiecare coloană:")
print(tips.dtypes.to_string())

# Statistici descriptive
print(f"\nStatistici descriptive pentru coloanele numerice:")
descriere = tips.describe().round(2)
print(descriere)


# Bacșișul mediu per zi
bacsis_mediu_zi = tips.groupby('day', observed=True)['tip'].mean().round(2)
print(f"\nBacșișul mediu per zi a săptămânii:")
for zi, medie in bacsis_mediu_zi.items():
    print(f"   {zi}: ${medie}")

# Bacșișul mediu per sex
bacsis_mediu_sex = tips.groupby('sex', observed=True)['tip'].mean().round(2)
print(f"\nBacșișul mediu per sex:")
for sex, medie in bacsis_mediu_sex.items():
    print(f"   {sex}: ${medie}")


tips_extins = tips.copy()
tips_extins['procent_bacsis'] = (tips_extins['tip'] / tips_extins['total_bill'] * 100).round(2)

print(f"\nPrimele 5 înregistrări cu noua coloană 'procent_bacsis':")
coloane_relevante = ['total_bill', 'tip', 'procent_bacsis', 'day', 'time', 'size']
print(tips_extins[coloane_relevante].head())


top_5_generoase = tips_extins.nlargest(5, 'procent_bacsis')[['total_bill', 'tip', 'procent_bacsis', 'day', 'time', 'sex', 'smoker']]

print(f"\nTop 5 cele mai generoase mese (procent bacșiș):")
print(top_5_generoase.to_string(index=False))



numar_mese = tips_extins.groupby(['day', 'smoker'], observed=True).size().reset_index(name='numar_mese')

print(f"\nDistribuția meselor în funcție de zi și statutul de fumător:")
print(numar_mese.to_string(index=False))